/*
   Copyright (c) 2009-2014, Jack Poulson
   All rights reserved.

   This file is part of Elemental and is under the BSD 2-Clause License, 
   which can be found in the LICENSE file in the root directory, or at 
   http://opensource.org/licenses/BSD-2-Clause
*/
#pragma once
#ifndef ELEM_GRCAR_HPP
#define ELEM_GRCAR_HPP

#include ELEM_SETDIAGONAL_INC
#include ELEM_ZEROS_INC

namespace elem {

template<typename T> 
inline void
Grcar( Matrix<T>& A, Int n, Int k=3 )
{
    DEBUG_ONLY(CallStackEntry cse("Grcar"))
    if( k < 0 )
        LogicError("Number of superdiagonals of ones must be non-negative");
    Zeros( A, n, n );
    if( n > 1 )
        SetDiagonal( A, -1, -1 );
    for( Int j=0; j<Min(n,k+1); ++j )
        SetDiagonal( A, n-1-j, 1 );
}

template<typename T,Dist U,Dist V>
inline void
Grcar( DistMatrix<T,U,V>& A, Int n, Int k=3 )
{
    DEBUG_ONLY(CallStackEntry cse("Grcar"))
    if( k < 0 )
        LogicError("Number of superdiagonals of ones must be non-negative");
    Zeros( A, n, n );
    if( n > 1 )
        SetDiagonal( A, -1, -1 );
    for( Int j=0; j<Min(n,k+1); ++j )
        SetDiagonal( A, n-1-j, 1 );
}

template<typename T,Dist U,Dist V>
inline void
Grcar( BlockDistMatrix<T,U,V>& A, Int n, Int k=3 )
{
    DEBUG_ONLY(CallStackEntry cse("Grcar"))
    if( k < 0 )
        LogicError("Number of superdiagonals of ones must be non-negative");
    Zeros( A, n, n );
    if( n > 1 )
        SetDiagonal( A, -1, -1 );
    for( Int j=0; j<Min(n,k+1); ++j )
        SetDiagonal( A, n-1-j, 1 );
}

#ifndef SWIG
template<typename T> 
inline Matrix<T>
Grcar( Int n, Int k=3 )
{
    Matrix<T> A;
    Grcar( A, n, k );
    return A;
}

template<typename T,Dist U=MC,Dist V=MR>
inline DistMatrix<T,U,V>
Grcar( const Grid& g, Int n, Int k=3 )
{
    DistMatrix<T,U,V> A(g);
    Grcar( A, n, k );
    return A;
}
#endif

// TODO: MakeGrcar?

} // namespace elem

#endif // ifndef ELEM_GRCAR_HPP
