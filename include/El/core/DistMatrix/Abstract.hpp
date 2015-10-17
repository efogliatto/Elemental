/*
   Copyright (c) 2009-2015, Jack Poulson
   All rights reserved.

   This file is part of Elemental and is under the BSD 2-Clause License, 
   which can be found in the LICENSE file in the root directory, or at 
   http://opensource.org/licenses/BSD-2-Clause
*/
#pragma once
#ifndef EL_DISTMATRIX_ABSTRACT_HPP
#define EL_DISTMATRIX_ABSTRACT_HPP

namespace El {

struct DistData;
struct ElementalData;

template<typename scalarType> 
class AbstractDistMatrix
{
public:
    // Typedefs
    // ========
    typedef AbstractDistMatrix<scalarType> type;

    // Constructors and destructors
    // ============================
    // Move constructor
    AbstractDistMatrix( type&& A ) EL_NO_EXCEPT;

    virtual ~AbstractDistMatrix();

    // Assignment and reconfiguration
    // ==============================
    virtual void Empty();
    virtual void SoftEmpty();
    void EmptyData();
    void SoftEmptyData();
    void SetGrid( const El::Grid& grid );

    virtual void AlignWith
    ( const El::DistData& data,
      bool constrain=true, bool allowMismatch=false ) = 0;
    virtual void AlignColsWith
    ( const El::DistData& data,
      bool constrain=true, bool allowMismatch=false ) = 0;
    virtual void AlignRowsWith
    ( const El::DistData& data,
      bool constrain=true, bool allowMismatch=false ) = 0;
    virtual void FreeAlignments();

    virtual void Resize( Int height, Int width ) = 0;
    virtual void Resize( Int height, Int width, Int ldim ) = 0;

    void MakeSizeConsistent( bool includingViewers=false );

    void SetRoot( int root, bool constrain=true );

    // Operator overloading
    // ====================

    // Move assignment
    // ---------------
    type& operator=( type&& A );

    // Rescaling
    // ---------
    const type& operator*=( scalarType alpha );

    // Basic queries
    // =============

    // Global matrix information
    // -------------------------
    Int  Height()                       const EL_NO_EXCEPT;
    Int  Width()                        const EL_NO_EXCEPT;
    Int  DiagonalLength( Int offset=0 ) const EL_NO_EXCEPT;
    bool Viewing()                      const EL_NO_EXCEPT;
    bool Locked()                       const EL_NO_EXCEPT;

    // Local matrix information
    // ------------------------
          Int         LocalHeight() const EL_NO_EXCEPT;
          Int         LocalWidth()  const EL_NO_EXCEPT;
          Int         LDim()        const EL_NO_EXCEPT;

          size_t      AllocatedMemory() const EL_NO_EXCEPT;

          scalarType* Buffer()                     EL_NO_RELEASE_EXCEPT;
          scalarType* Buffer( Int iLoc, Int jLoc ) EL_NO_RELEASE_EXCEPT;

    const scalarType* LockedBuffer()                     const EL_NO_EXCEPT;
    const scalarType* LockedBuffer( Int iLoc, Int jLoc ) const EL_NO_EXCEPT;

          El::Matrix<scalarType>& Matrix()             EL_NO_EXCEPT;
    const El::Matrix<scalarType>& LockedMatrix() const EL_NO_EXCEPT;

    // Distribution information
    // ------------------------
    const El::Grid& Grid() const EL_NO_EXCEPT;

    virtual Int BlockHeight() const EL_NO_EXCEPT = 0;
    virtual Int BlockWidth()  const EL_NO_EXCEPT = 0;
    virtual Int ColCut()      const EL_NO_EXCEPT = 0;
    virtual Int RowCut()      const EL_NO_EXCEPT = 0;

    int  ColAlign()        const EL_NO_EXCEPT;
    int  RowAlign()        const EL_NO_EXCEPT;
    int  ColShift()        const EL_NO_EXCEPT;
    int  RowShift()        const EL_NO_EXCEPT;
    bool ColConstrained()  const EL_NO_EXCEPT;
    bool RowConstrained()  const EL_NO_EXCEPT;
    bool RootConstrained() const EL_NO_EXCEPT;
    bool Participating()   const EL_NO_RELEASE_EXCEPT;
    int  Root()            const EL_NO_EXCEPT;

    virtual int  RowOwner( Int i )       const EL_NO_EXCEPT = 0;
    virtual int  ColOwner( Int j )       const EL_NO_EXCEPT = 0;
    virtual Int  LocalRowOffset( Int i ) const EL_NO_EXCEPT = 0;
    virtual Int  LocalColOffset( Int j ) const EL_NO_EXCEPT = 0;
    virtual Int  GlobalRow( Int iLoc )   const EL_NO_EXCEPT = 0;
    virtual Int  GlobalCol( Int jLoc )   const EL_NO_EXCEPT = 0;

    Int  LocalRow( Int i )       const EL_NO_RELEASE_EXCEPT;
    Int  LocalCol( Int j )       const EL_NO_RELEASE_EXCEPT;
    int  Owner( Int i, Int j )   const EL_NO_EXCEPT;
    bool IsLocalRow( Int i )     const EL_NO_RELEASE_EXCEPT;
    bool IsLocalCol( Int j )     const EL_NO_RELEASE_EXCEPT;
    bool IsLocal( Int i, Int j ) const EL_NO_RELEASE_EXCEPT;

    // NOTE: These are all clearly equivalent to composing mpi::Rank
    //       with ColComm(), RowComm(), etc., but it is not clear that
    //       they should be removed just yet.
    virtual int ColRank()             const EL_NO_RELEASE_EXCEPT = 0;
    virtual int RowRank()             const EL_NO_RELEASE_EXCEPT = 0;
    virtual int PartialColRank()      const EL_NO_RELEASE_EXCEPT = 0;
    virtual int PartialRowRank()      const EL_NO_RELEASE_EXCEPT = 0;
    virtual int PartialUnionColRank() const EL_NO_RELEASE_EXCEPT = 0;
    virtual int PartialUnionRowRank() const EL_NO_RELEASE_EXCEPT = 0;
    virtual int DistRank()            const EL_NO_RELEASE_EXCEPT = 0;
    virtual int CrossRank()           const EL_NO_RELEASE_EXCEPT = 0;
    virtual int RedundantRank()       const EL_NO_RELEASE_EXCEPT = 0;

    virtual Dist     ColDist()             const EL_NO_EXCEPT = 0;
    virtual Dist     RowDist()             const EL_NO_EXCEPT = 0;
    virtual Dist     CollectedColDist()    const EL_NO_EXCEPT = 0;
    virtual Dist     CollectedRowDist()    const EL_NO_EXCEPT = 0;
    virtual Dist     PartialColDist()      const EL_NO_EXCEPT = 0;
    virtual Dist     PartialRowDist()      const EL_NO_EXCEPT = 0;
    virtual Dist     PartialUnionColDist() const EL_NO_EXCEPT = 0;
    virtual Dist     PartialUnionRowDist() const EL_NO_EXCEPT = 0;
    virtual DistWrap Wrap()                const EL_NO_EXCEPT = 0;

    virtual mpi::Comm ColComm()             const EL_NO_EXCEPT = 0;
    virtual mpi::Comm RowComm()             const EL_NO_EXCEPT = 0;
    virtual mpi::Comm PartialColComm()      const EL_NO_EXCEPT = 0;
    virtual mpi::Comm PartialRowComm()      const EL_NO_EXCEPT = 0;
    virtual mpi::Comm PartialUnionColComm() const EL_NO_EXCEPT = 0;
    virtual mpi::Comm PartialUnionRowComm() const EL_NO_EXCEPT = 0;
    virtual mpi::Comm DistComm()            const EL_NO_EXCEPT = 0;
    virtual mpi::Comm CrossComm()           const EL_NO_EXCEPT = 0;
    virtual mpi::Comm RedundantComm()       const EL_NO_EXCEPT = 0;

    virtual int ColStride()             const EL_NO_EXCEPT = 0;
    virtual int RowStride()             const EL_NO_EXCEPT = 0;
    virtual int PartialColStride()      const EL_NO_EXCEPT = 0;
    virtual int PartialRowStride()      const EL_NO_EXCEPT = 0;
    virtual int PartialUnionColStride() const EL_NO_EXCEPT = 0;
    virtual int PartialUnionRowStride() const EL_NO_EXCEPT = 0;
    virtual int DistSize()              const EL_NO_EXCEPT = 0;
    virtual int CrossSize()             const EL_NO_EXCEPT = 0;
    virtual int RedundantSize()         const EL_NO_EXCEPT = 0;

    // Single-entry manipulation
    // =========================

    // Global entry manipulation 
    // -------------------------
    // NOTE: Local entry manipulation is often much faster and should be
    //       preferred in most circumstances where performance matters.

    scalarType Get( Int i, Int j ) const EL_NO_RELEASE_EXCEPT;

    Base<scalarType> GetRealPart( Int i, Int j ) const EL_NO_RELEASE_EXCEPT;
    Base<scalarType> GetImagPart( Int i, Int j ) const EL_NO_RELEASE_EXCEPT;

    void Set( Int i, Int j, scalarType alpha ) EL_NO_RELEASE_EXCEPT;
    void Set( const Entry<scalarType>& entry ) EL_NO_RELEASE_EXCEPT;

    void SetRealPart
    ( Int i, Int j, Base<scalarType> alpha ) EL_NO_RELEASE_EXCEPT;
    void SetImagPart
    ( Int i, Int j, Base<scalarType> alpha ) EL_NO_RELEASE_EXCEPT;

    void SetRealPart
    ( const Entry<Base<scalarType>>& entry ) EL_NO_RELEASE_EXCEPT;
    void SetImagPart
    ( const Entry<Base<scalarType>>& entry ) EL_NO_RELEASE_EXCEPT;

    void Update( Int i, Int j, scalarType alpha ) EL_NO_RELEASE_EXCEPT;
    void Update( const Entry<scalarType>& entry ) EL_NO_RELEASE_EXCEPT;

    void UpdateRealPart
    ( Int i, Int j, Base<scalarType> alpha ) EL_NO_RELEASE_EXCEPT;
    void UpdateImagPart
    ( Int i, Int j, Base<scalarType> alpha ) EL_NO_RELEASE_EXCEPT;

    void UpdateRealPart
    ( const Entry<Base<scalarType>>& entry ) EL_NO_RELEASE_EXCEPT;
    void UpdateImagPart
    ( const Entry<Base<scalarType>>& entry ) EL_NO_RELEASE_EXCEPT;

    void MakeReal( Int i, Int j ) EL_NO_RELEASE_EXCEPT;
    void Conjugate( Int i, Int j ) EL_NO_RELEASE_EXCEPT;

    // Batch updating of remote entries
    // ---------------------------------
    void Reserve( Int numRemoteEntries );
    void QueueUpdate( const Entry<scalarType>& entry ) EL_NO_RELEASE_EXCEPT;
    void QueueUpdate( Int i, Int j, scalarType value ) EL_NO_RELEASE_EXCEPT;
    void ProcessQueues();

    // Batch extraction of remote entries
    // ----------------------------------
    void ReservePulls( Int numPulls ) const;
    void QueuePull( Int i, Int j ) const EL_NO_RELEASE_EXCEPT;
    void ProcessPullQueue( scalarType* pullBuf ) const;
    void ProcessPullQueue( vector<scalarType>& pullBuf ) const;

    // Local entry manipulation
    // ------------------------
    // NOTE: Clearly each of the following routines could instead be performed
    //       via composing [Locked]Matrix() with the corresponding local
    //       routine, but a large amount of code might need to change if 
    //       these were removed.

    scalarType GetLocal( Int iLoc, Int jLoc ) const EL_NO_RELEASE_EXCEPT;

    Base<scalarType> GetLocalRealPart
    ( Int iLoc, Int jLoc ) const EL_NO_RELEASE_EXCEPT;
    Base<scalarType> GetLocalImagPart
    ( Int iLoc, Int jLoc ) const EL_NO_RELEASE_EXCEPT;

    void SetLocal( Int iLoc, Int jLoc, scalarType alpha ) EL_NO_RELEASE_EXCEPT;
    void SetLocal( const Entry<scalarType>& localEntry ) EL_NO_RELEASE_EXCEPT;

    void SetLocalRealPart( Int iLoc, Int jLoc, Base<scalarType> alpha )
    EL_NO_RELEASE_EXCEPT;
    void SetLocalImagPart( Int iLoc, Int jLoc, Base<scalarType> alpha )
    EL_NO_RELEASE_EXCEPT;

    void SetLocalRealPart( const Entry<Base<scalarType>>& localEntry )
    EL_NO_RELEASE_EXCEPT;
    void SetLocalImagPart( const Entry<Base<scalarType>>& localEntry )
    EL_NO_RELEASE_EXCEPT;

    void UpdateLocal
    ( Int iLoc, Int jLoc, scalarType alpha ) EL_NO_RELEASE_EXCEPT;
    void UpdateLocal
    ( const Entry<scalarType>& localEntry ) EL_NO_RELEASE_EXCEPT;

    void UpdateLocalRealPart( Int iLoc, Int jLoc, Base<scalarType> alpha )
    EL_NO_RELEASE_EXCEPT;
    void UpdateLocalImagPart( Int iLoc, Int jLoc, Base<scalarType> alpha )
    EL_NO_RELEASE_EXCEPT;

    void UpdateLocalRealPart( const Entry<Base<scalarType>>& localEntry )
    EL_NO_RELEASE_EXCEPT;
    void UpdateLocalImagPart( const Entry<Base<scalarType>>& localEntry )
    EL_NO_RELEASE_EXCEPT;

    void MakeLocalReal( Int iLoc, Int jLoc ) EL_NO_RELEASE_EXCEPT;
    void ConjugateLocal( Int iLoc, Int jLoc ) EL_NO_RELEASE_EXCEPT;

    // Diagonal manipulation
    // =====================
    virtual bool DiagonalAlignedWith
    ( const El::DistData& d, Int offset=0 ) const = 0;
    virtual int DiagonalRoot( Int offset=0 ) const EL_NO_EXCEPT = 0;
    virtual int DiagonalAlign( Int offset=0 ) const EL_NO_EXCEPT = 0;

    // Assertions
    // ==========
    void ComplainIfReal() const;
    void AssertNotLocked() const;
    void AssertNotStoringData() const;
    void AssertValidEntry( Int i, Int j ) const;
    void AssertValidSubmatrix( Int i, Int j, Int height, Int width ) const;
    void AssertSameSize( Int height, Int width ) const;

protected:
    // Member variables
    // ================
    bool colConstrained_=false,
         rowConstrained_=false,
         rootConstrained_=false;
    int colAlign_=0,
        rowAlign_=0,
        colShift_=0,
        rowShift_=0;
    int root_=0;

    // Global and local matrix information 
    // -----------------------------------
    ViewType viewType_=OWNER;
    Int height_=0, width_=0;
    El::Matrix<scalarType> matrix_=El::Matrix<scalarType>(0,0,true);
    const El::Grid* grid_;

    // Remote updates
    // --------------
    vector<Entry<scalarType>> remoteUpdates_;
    // NOTE: Using ValueInt<Int> is somewhat of a hack; it would be nice to 
    //       have a pair of integers as its own data structure that does not
    //       require separate MPI wrappers from ValueInt<Int>
    mutable vector<ValueInt<Int>> remotePulls_;

    // Protected constructors
    // ======================
    // Create a 0 x 0 distributed matrix
    AbstractDistMatrix( const El::Grid& g=DefaultGrid(), int root=0 );

    // Modify the distribution metadata
    // ================================
    virtual void SetShifts();
    virtual void SetColShift();
    virtual void SetRowShift();

private:
    // Exchange metadata with another matrix
    // =====================================
    void ShallowSwap( type& A );

    template<typename S,Dist J,Dist K,DistWrap wrap> friend class DistMatrix;
};

struct DistData
{
    Dist colDist, rowDist;
    Int blockHeight, blockWidth;
    int colAlign, rowAlign;
    Int colCut, rowCut;
    int root;  // relevant for [o ,o ]/[MD,* ]/[* ,MD]
    const Grid* grid;

    DistData() { }

    template<typename scalarType>
    DistData( const BlockMatrix<scalarType>& A )
    : colDist(A.ColDist()), rowDist(A.RowDist()),
      blockHeight(A.BlockHeight()), blockWidth(A.BlockWidth()),
      colAlign(A.ColAlign()), rowAlign(A.RowAlign()),
      colCut(A.ColCut()), rowCut(A.RowCut()),
      root(A.Root()), grid(&A.Grid())
    { }
};
inline bool operator==( const DistData& A, const DistData& B )
{ return A.colDist     == B.colDist &&
         A.rowDist     == B.rowDist &&
         A.blockHeight == B.blockHeight &&
         A.blockWidth  == B.blockWidth &&
         A.colAlign    == B.colAlign &&
         A.rowAlign    == B.rowAlign &&
         A.root        == B.root &&
         A.grid        == B.grid; }

struct ElementalData
{
    Dist colDist, rowDist;
    int colAlign, rowAlign;
    int root;  // relevant for [o ,o ]/[MD,* ]/[* ,MD]
    const Grid* grid;

    ElementalData() { }

    template<typename scalarType>
    ElementalData( const ElementalMatrix<scalarType>& A )
    : colDist(A.ColDist()), rowDist(A.RowDist()),
      colAlign(A.ColAlign()), rowAlign(A.RowAlign()),
      root(A.Root()), grid(&A.Grid())
    { }
};
inline bool operator==( const ElementalData& A, const ElementalData& B )
{ return A.colDist  == B.colDist &&
         A.rowDist  == B.rowDist &&
         A.colAlign == B.colAlign &&
         A.rowAlign == B.rowAlign &&
         A.root     == B.root &&
         A.grid     == B.grid; }

} // namespace El

#endif // ifndef EL_DISTMATRIX_ABSTRACT_HPP
