/*
   Copyright (c) 2009-2014, Jack Poulson
   All rights reserved.

   This file is part of Elemental and is under the BSD 2-Clause License, 
   which can be found in the LICENSE file in the root directory, or at 
   http://opensource.org/licenses/BSD-2-Clause
*/
#pragma once
#ifndef EL_CHOLESKY_LVAR3PIVOTED_HPP
#define EL_CHOLESKY_LVAR3PIVOTED_HPP

namespace El {
namespace cholesky {

namespace pivot {

template<typename F>
inline LDLPivot
Full( const Matrix<F>& A )
{
    DEBUG_ONLY(CallStackEntry cse("cholesky::pivot::Full"))
    const auto diagMax = VectorMaxAbs( A.GetDiagonal() );
    LDLPivot pivot;
    pivot.nb = 1;
    pivot.from[0] = diagMax.index;
    return pivot;
}

template<typename F>
inline LDLPivot
Full( const DistMatrix<F>& A )
{
    DEBUG_ONLY(CallStackEntry cse("cholesky::pivot::Full"))
    const auto diagMax = VectorMaxAbs( A.GetDiagonal() );
    LDLPivot pivot;
    pivot.nb = 1;
    pivot.from[0] = diagMax.index;
    return pivot;
}

template<typename F>
inline LDLPivot
PanelFull( const Matrix<F>& A, const Matrix<F>& X, const Matrix<F>& Y )
{
    DEBUG_ONLY(CallStackEntry cse("cholesky::pivot::PanelFull"))
    // Form updated diagonal
    auto d = A.GetDiagonal();
    const Int height = d.Height();
    const Int k = X.Width();
    for( Int i=0; i<height; ++i )
        for( Int j=0; j<k; ++j )
            d.Update( i, 0, -X.Get(i,j)*Y.Get(i,j) );

    // Return maximum from it
    auto diagMax = VectorMaxAbs( d );
    LDLPivot pivot;
    pivot.nb = 1;
    pivot.from[0] = diagMax.index;
    return pivot;
}

template<typename F>
inline LDLPivot
PanelFull
( const DistMatrix<F>& A, 
  const DistMatrix<F,MC,STAR>& X, const DistMatrix<F,MR,STAR>& Y )
{
    DEBUG_ONLY(
        CallStackEntry cse("cholesky::pivot::PanelFull");
        if( A.ColAlign() != X.ColAlign() || A.RowAlign() != Y.ColAlign() )
            LogicError("A, X, and Y are not properly aligned");
    )
    // Form updated diagonal
    auto d = A.GetDiagonal();
    if( d.Participating() )
    {
        const Int dLocalHeight = d.LocalHeight();
        const Int k = X.Width();
        for( Int iLoc=0; iLoc<dLocalHeight; ++iLoc )
        {
            const Int i = d.GlobalRow(iLoc);
            const Int iLocX = X.LocalRow(i);
            const Int iLocY = Y.LocalRow(i);
            for( Int j=0; j<k; ++j )
                d.UpdateLocal
                ( iLoc, 0, -X.GetLocal(iLocX,j)*Y.GetLocal(iLocY,j) );
            d.MakeReal( iLoc, 0 );
        }
    }

    // Return maximum from it
    auto diagMax = VectorMaxAbs( d );
    LDLPivot pivot;
    pivot.nb = 1;
    pivot.from[0] = diagMax.index;
    return pivot;
}

} // namespace pivot

template<typename F>
inline void
LUnblockedPivoted( Matrix<F>& A, Matrix<Int>& p )
{
    DEBUG_ONLY(
        CallStackEntry cse("cholesky::LUnblockedPivoted");
        if( A.Height() != A.Width() )
            LogicError("A must be square");
    )
    const Int n = A.Height();

    // Initialize the permutation to the identity
    p.Resize( n, 1 );
    for( Int i=0; i<n; ++i ) 
        p.Set( i, 0, i );
     
    for( Int k=0; k<n; ++k )
    {
        const IndexRange ind1( k,   k+1 ),
                         ind2( k+1, n   ),
                         indB( k,   n   ),
                         indR( k,   n   );

        auto a21 = View( A, ind2, ind1 );
        auto A22 = View( A, ind2, ind2 );
        auto ABR = View( A, indB, indR );

        // Determine the pivot
        const LDLPivot pivot = pivot::Full( ABR );

        // Apply the pivot
        const Int from = k + pivot.from[0];
        HermitianSwap( LOWER, A, k, from );
        RowSwap( p, k, from );

        // a21 := a21 / sqrt(alpha11)
        const Base<F> delta11 = Sqrt(ABR.GetRealPart(0,0));
        const Base<F> delta11Inv = Base<F>(1)/delta11;
        ABR.Set(0,0,delta11);
        Scale( delta11Inv, a21 );

        // A22 -= a21 a21'
        Her( LOWER, F(-1), a21, A22 );
    }
}

template<typename F>
inline void
LUnblockedPivoted
( AbstractDistMatrix<F>& APre, AbstractDistMatrix<Int>& p )
{
    DEBUG_ONLY(
        CallStackEntry cse("cholesky::LUnblockedPivoted");
        if( APre.Height() != APre.Width() )
            LogicError("A must be square");
        AssertSameGrids( APre, p );
    )
    const Int n = APre.Height();
    const Grid& g = APre.Grid();

    DistMatrix<F> A(g);
    Copy( APre, A, READ_WRITE_PROXY );

    // Initialize the permutation to the identity
    p.Resize( n, 1 );
    if( p.IsLocalCol(0) )
        for( Int iLoc=0; iLoc<p.LocalHeight(); ++iLoc )
            p.SetLocal( iLoc, 0, p.GlobalRow(iLoc) );

    for( Int k=0; k<n; ++k )
    {
        const IndexRange ind1( k,   k+1 ),
                         ind2( k+1, n   ),
                         indB( k,   n   ),
                         indR( k,   n   );

        auto a21 = View( A, ind2, ind1 );
        auto A22 = View( A, ind2, ind2 );
        auto ABR = View( A, indB, indR );

        // Determine the pivot
        const LDLPivot pivot = pivot::Full( ABR );

        // Apply the pivot
        const Int from = k + pivot.from[0];
        HermitianSwap( LOWER, A, k, from );
        RowSwap( p, k, from );

        // a21 := a21 / sqrt(alpha11)
        const Base<F> delta11 = Sqrt(ABR.GetRealPart(0,0));
        const Base<F> delta11Inv = Base<F>(1)/delta11;
        ABR.Set(0,0,delta11);
        Scale( delta11Inv, a21 );

        // A22 -= a21 a21'
        Her( LOWER, F(-1), a21, A22 );
    }
    Copy( A, APre, RESTORE_READ_WRITE_PROXY );
}

// We must use a lazy algorithm so that the symmetric pivoting does not move
// data from a fully-updated to partially-updated region (and vice-versa)
template<typename F>
inline void
LPanelPivoted
( Matrix<F>& AFull, Matrix<Int>& p, 
  Matrix<F>& X, Matrix<F>& Y, Int bsize, Int off )
{
    DEBUG_ONLY(CallStackEntry cse("cholesky::LPanelPivoted"))
    const Int nFull = AFull.Height();
    auto A = View( AFull, IndexRange(off,nFull), IndexRange(off,nFull) );
    const Int n = A.Height();
    DEBUG_ONLY(
        if( A.Width() != n )
            LogicError("A must be square");
        if( p.Height() != n || p.Width() != 1 )
            LogicError("permutation vector is the wrong size");
    )
    Zeros( X, n, bsize );
    Zeros( Y, n, bsize );

    for( Int k=0; k<bsize; ++k )
    {
        const IndexRange ind0( 0,   k   ),
                         ind1( k,   k+1 ),
                         ind2( k+1, n   ),
                         indB( k,   n   ),
                         indR( k,   n   );

        auto a21 = View( A, ind2, ind1 );
        auto aB1 = View( A, indB, ind1 );
        auto ABR = View( A, indB, indR );

        auto x21 = View( X, ind2, ind1 );
        auto XB0 = View( X, indB, ind0 );

        auto y10 = LockedView( Y, ind1, ind0 );
        auto y21 =       View( Y, ind2, ind1 );
        auto YB0 =       View( Y, indB, ind0 );

        // Determine the pivot 
        const auto pivot = pivot::PanelFull( ABR, XB0, YB0 );
        const Int from = k + pivot.from[0];

        // Apply the pivot
        HermitianSwap( LOWER, AFull, k+off, from+off );
        RowSwap( p, k, from );
        RowSwap( XB0, 0, pivot.from[0] );
        RowSwap( YB0, 0, pivot.from[0] );

        // Update A(k:end,k) -= X(k:end,0:k-1) Y(k,0:k-1)^T
        Gemv( NORMAL, F(-1), XB0, y10, F(1), aB1 );
        aB1.MakeReal(0,0);

        // a21 := a21 / sqrt(alpha11)
        const Base<F> delta11 = Sqrt(A.GetRealPart(k,k));
        const Base<F> delta11Inv = Base<F>(1)/delta11;
        A.SetRealPart(k,k,delta11);
        Scale( delta11Inv, a21 );

        // Store x21 := a21 and y21 := conj(a21)
        Conjugate( a21, y21 );
        x21 = a21;
    }
}

template<typename F>
inline void
LPanelPivoted
( DistMatrix<F>& AFull, AbstractDistMatrix<Int>& p, 
  DistMatrix<F,MC,STAR>& X, DistMatrix<F,MR,STAR>& Y, Int bsize, Int off )
{
    DEBUG_ONLY(CallStackEntry cse("cholesky::LPanelPivoted"))
    const Int nFull = AFull.Height();
    auto A = View( AFull, IndexRange(off,nFull), IndexRange(off,nFull) );
    const Int n = A.Height();
    DEBUG_ONLY(
        if( A.Width() != n )
            LogicError("A must be square");
        if( p.Height() != n || p.Width() != 1 )
            LogicError("permutation vector is the wrong size");
    )
    X.AlignWith( A );
    Y.AlignWith( A );
    Zeros( X, n, bsize );
    Zeros( Y, n, bsize );

    for( Int k=0; k<bsize; ++k )
    {
        const IndexRange ind0( 0,   k   ),
                         ind1( k,   k+1 ),
                         ind2( k+1, n   ),
                         indB( k,   n   ),
                         indR( k,   n   );

        auto a21 = View( A, ind2, ind1 );
        auto aB1 = View( A, indB, ind1 );
        auto ABR = View( A, indB, indR );

        auto x21 = View( X, ind2, ind1 );
        auto XB0 = View( X, indB, ind0 );

        auto y10 = LockedView( Y, ind1, ind0 );
        auto y21 =       View( Y, ind2, ind1 );
        auto YB0 =       View( Y, indB, ind0 );

        // Determine the pivot
        const auto pivot = pivot::PanelFull( ABR, XB0, YB0 );
        const Int from = k + pivot.from[0];

        // Apply the pivot
        HermitianSwap( LOWER, AFull, k+off, from+off );
        RowSwap( p, k, from );
        RowSwap( XB0, 0, pivot.from[0] );
        RowSwap( YB0, 0, pivot.from[0] );

        // A(k:end,k) -= X(k:end,0:k-1) Y(k,0:k-1)^T
        if( aB1.RowAlign() == aB1.RowRank() )
            LocalGemv( NORMAL, F(-1), XB0, y10, F(1), aB1 );
        aB1.MakeReal(0,0);

        // a21 := a21 / sqrt(alpha11)
        const Base<F> delta11 = Sqrt(A.GetRealPart(k,k));
        const Base<F> delta11Inv = Base<F>(1)/delta11;
        A.SetRealPart(k,k,delta11);
        Scale( delta11Inv, a21 );

        // Store x21 := a21 and y21 := conj(a21)
        Conjugate( a21, y21 );
        x21 = a21;
    }
}

template<typename F>
inline void
LVar3( Matrix<F>& A, Matrix<Int>& p )
{
    DEBUG_ONLY(
        CallStackEntry cse("cholesky::LVar3");
        if( A.Height() != A.Width() )
            LogicError("A must be square");
    )
    const Int n = A.Height();

    // Initialize the permutation to the identity
    p.Resize( n, 1 );
    for( Int i=0; i<n; ++i )
        p.Set( i, 0, i );

    Matrix<F> XB1, YB1;
    const Int bsize = Blocksize();
    for( Int k=0; k<n; k+=bsize )
    {
        const Int nb = Min(bsize,n-k);

        const IndexRange indB( k, n );
        auto pB = View( p, indB, IndexRange(0,1) );
        LPanelPivoted( A, pB, XB1, YB1, nb, k );

        // Update the bottom-right panel
        const IndexRange ind2( k+nb, n ),
                         ind1Pan( 0,  nb  ),
                         ind2Pan( nb, n-k );
        auto A22 =       View( A,   ind2,    ind2    );
        auto X21 = LockedView( XB1, ind2Pan, ind1Pan );
        auto Y21 = LockedView( YB1, ind2Pan, ind1Pan );
        Trrk( LOWER, NORMAL, TRANSPOSE, F(-1), X21, Y21, F(1), A22 );
    }
}

template<typename F>
inline void
LVar3( AbstractDistMatrix<F>& APre, AbstractDistMatrix<Int>& pPre )
{
    DEBUG_ONLY(
        CallStackEntry cse("cholesky::LVar3");
        AssertSameGrids( APre, pPre );
        if( APre.Height() != APre.Width() )
            LogicError("A must be square");
    )
    const Int n = APre.Height();
    const Grid& g = APre.Grid();

    pPre.Resize( n, 1 );

    DistMatrix<F> A(g);
    DistMatrix<Int,VC,STAR> p(g);
    Copy( APre, A, READ_WRITE_PROXY );
    Copy( pPre, p, WRITE_PROXY      );

    // Initialize the permutation to the identity
    for( Int iLoc=0; iLoc<p.LocalHeight(); ++iLoc )
        p.SetLocal( iLoc, 0, p.GlobalRow(iLoc) );

    DistMatrix<F,MC,STAR> XB1(g);
    DistMatrix<F,MR,STAR> YB1(g);
    const Int bsize = Blocksize();
    for( Int k=0; k<n; k+=bsize )
    {
        const Int nb = Min(bsize,n-k);

        const IndexRange indB( k, n );
        auto pB = View( p, indB, IndexRange(0,1) );
        LPanelPivoted( A, pB, XB1, YB1, nb, k );

        // Update the bottom-right panel
        const IndexRange ind2( k+nb, n ),
                         ind1Pan( 0,  nb  ),
                         ind2Pan( nb, n-k );
        auto A22 =       View( A,   ind2,    ind2    );
        auto X21 = LockedView( XB1, ind2Pan, ind1Pan );
        auto Y21 = LockedView( YB1, ind2Pan, ind1Pan );
        LocalTrrk( LOWER, TRANSPOSE, F(-1), X21, Y21, F(1), A22 );
    }
    Copy( A, APre, RESTORE_READ_WRITE_PROXY );
    Copy( p, pPre, RESTORE_WRITE_PROXY      );
}

} // namespace cholesky
} // namespace El

#endif // ifndef EL_CHOLESKY_LVAR3PIVOTED_HPP
