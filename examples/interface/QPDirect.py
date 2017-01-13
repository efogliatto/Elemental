#
#  Copyright (c) 2009-2016, Jack Poulson
#  All rights reserved.
#
#  This file is part of Elemental and is under the BSD 2-Clause License, 
#  which can be found in the LICENSE file in the root directory, or at 
#  http://opensource.org/licenses/BSD-2-Clause
#
import El

m = 2000
n = 4000
testIPM = True
manualInit = False
display = False
progress = True
worldRank = El.mpi.WorldRank()
worldSize = El.mpi.WorldSize()

# Make Q a sparse semidefinite matrix
def Semidefinite(height):
  Q = El.DistSparseMatrix()
  Q.Resize(height,height)
  localHeight = Q.LocalHeight()
  Q.Reserve(localHeight)
  for sLoc in xrange(localHeight):
    s = Q.GlobalRow(sLoc)
    Q.QueueLocalUpdate( sLoc, s, 1 );

  Q.ProcessQueues()
  return Q

# Make a sparse matrix with the last column dense
def Rectang(height,width):
  A = El.DistSparseMatrix()
  A.Resize(height,width)
  localHeight = A.LocalHeight()
  A.Reserve(5*localHeight)
  for sLoc in xrange(localHeight):
    s = A.GlobalRow(sLoc)
    if s < width: 
      A.QueueLocalUpdate( sLoc, s,        11 )
    if s >= 1 and s-1 < width:
      A.QueueLocalUpdate( sLoc, s-1,      -1 )
    if s+1 < width:
      A.QueueLocalUpdate( sLoc, s+1,       2 )
    if s >= height and s-height < width:
      A.QueueLocalUpdate( sLoc, s-height, -3 )
    if s+height < width: 
      A.QueueLocalUpdate( sLoc, s+height,  4 )
    # The dense last column
    A.QueueLocalUpdate( sLoc, width-1, -5/height );

  A.ProcessQueues()
  return A

Q = Semidefinite(n)
A = Rectang(m,n)

# Generate a b which implies a primal feasible x
# ==============================================
xGen = El.DistMultiVec()
El.Uniform(xGen,n,1,0.5,0.5)
b = El.DistMultiVec()
El.Zeros( b, m, 1 )
El.Multiply( El.NORMAL, 1., A, xGen, 0., b )

# Generate a c which implies a dual feasible (y,z)
# ================================================
yGen = El.DistMultiVec()
El.Gaussian(yGen,m,1)
c = El.DistMultiVec()
El.Uniform(c,n,1,0.5,0.5)
El.Multiply( El.NORMAL,    -1,  Q, xGen, 1., c )
El.Multiply( El.TRANSPOSE, -1., A, yGen, 1., c )

if display:
  El.Display( Q, "Q" )
  El.Display( A, "A" )
  El.Display( b, "b" )
  El.Display( c, "c" )

# Set up the control structure (and possibly initial guesses)
# ===========================================================
ctrl = El.QPDirectCtrl_d()
xOrig = El.DistMultiVec()
yOrig = El.DistMultiVec()
zOrig = El.DistMultiVec()
if manualInit:
  El.Uniform(xOrig,n,1,0.5,0.4999)
  El.Uniform(yOrig,m,1,0.5,0.4999)
  El.Uniform(zOrig,n,1,0.5,0.4999)
x = El.DistMultiVec()
y = El.DistMultiVec()
z = El.DistMultiVec()

if testIPM:
  ctrl.approach = El.QP_IPM
  ctrl.ipmCtrl.solveCtrl.progress = progress
  ctrl.ipmCtrl.primalInit = manualInit
  ctrl.ipmCtrl.dualInit = manualInit
  ctrl.ipmCtrl.progress = progress
  ctrl.ipmCtrl.time = True
  El.Copy( xOrig, x )
  El.Copy( yOrig, y )
  El.Copy( zOrig, z )
  startIPM = El.mpi.Time()
  El.QPDirect(Q,A,b,c,x,y,z,ctrl)
  endIPM = El.mpi.Time()
  if worldRank == 0:
    print('IPM time: {} seconds'.format(endIPM-startIPM))

  if display:
    El.Display( x, "x IPM" )
    El.Display( y, "y IPM" )
    El.Display( z, "z IPM" )

  d = El.DistMultiVec()
  El.Zeros( d, n, 1 )
  El.Multiply( El.NORMAL, 1., Q, x, 0., d )
  obj = El.Dot(x,d)/2 + El.Dot(c,x)
  if worldRank == 0:
    print('IPM (1/2) x^T Q x + c^T x = {}'.format(obj))

El.Finalize()
