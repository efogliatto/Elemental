#
#  Copyright (c) 2009-2014, Jack Poulson
#  All rights reserved.
#
#  This file is part of Elemental and is under the BSD 2-Clause License, 
#  which can be found in the LICENSE file in the root directory, or at 
#  http://opensource.org/licenses/BSD-2-Clause
#
from ..core import *
import ctypes

# Hermitian tridiagonal eigensolvers
# ==================================
class HermitianEigSubset_s(ctypes.Structure):
  _fields_ = [("indexSubset",bType),
              ("lowerIndex",iType),("upperIndex",iType),
              ("rangeSubset",bType),
              ("lowerBound",sType),("upperBound",sType)]
class HermitianEigSubset_d(ctypes.Structure):
  _fields_ = [("indexSubset",bType),
              ("lowerIndex",iType),("upperIndex",iType),
              ("rangeSubset",bType),
              ("lowerBound",dType),("upperBound",dType)]

lib.ElHermitianTridiagEig_s.argtypes = [c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEig_s.restype = c_uint
lib.ElHermitianTridiagEig_d.argtypes = [c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEig_d.restype = c_uint
lib.ElHermitianTridiagEig_c.argtypes = [c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEig_c.restype = c_uint
lib.ElHermitianTridiagEig_z.argtypes = [c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEig_z.restype = c_uint
lib.ElHermitianTridiagEigDist_s.argtypes = [c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEigDist_s.restype = c_uint
lib.ElHermitianTridiagEigDist_d.argtypes = [c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEigDist_d.restype = c_uint
lib.ElHermitianTridiagEigDist_c.argtypes = [c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEigDist_c.restype = c_uint
lib.ElHermitianTridiagEigDist_z.argtypes = [c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEigDist_z.restype = c_uint
lib.ElHermitianTridiagEigPair_s.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEigPair_s.restype = c_uint
lib.ElHermitianTridiagEigPair_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEigPair_d.restype = c_uint
lib.ElHermitianTridiagEigPair_c.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEigPair_c.restype = c_uint
lib.ElHermitianTridiagEigPair_z.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEigPair_z.restype = c_uint
lib.ElHermitianTridiagEigPairDist_s.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEigPairDist_s.restype = c_uint
lib.ElHermitianTridiagEigPairDist_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEigPairDist_d.restype = c_uint
lib.ElHermitianTridiagEigPairDist_c.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEigPairDist_c.restype = c_uint
lib.ElHermitianTridiagEigPairDist_z.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianTridiagEigPairDist_z.restype = c_uint

lib.ElHermitianTridiagEigPartial_s.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianTridiagEigPartial_s.restype = c_uint
lib.ElHermitianTridiagEigPartial_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianTridiagEigPartial_d.restype = c_uint
lib.ElHermitianTridiagEigPartial_c.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianTridiagEigPartial_c.restype = c_uint
lib.ElHermitianTridiagEigPartial_z.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianTridiagEigPartial_z.restype = c_uint
lib.ElHermitianTridiagEigPartialDist_s.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianTridiagEigPartialDist_s.restype = c_uint
lib.ElHermitianTridiagEigPartialDist_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianTridiagEigPartialDist_d.restype = c_uint
lib.ElHermitianTridiagEigPartialDist_c.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianTridiagEigPartialDist_c.restype = c_uint
lib.ElHermitianTridiagEigPartialDist_z.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianTridiagEigPartialDist_z.restype = c_uint
lib.ElHermitianTridiagEigPairPartial_s.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianTridiagEigPairPartial_s.restype = c_uint
lib.ElHermitianTridiagEigPairPartial_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianTridiagEigPairPartial_d.restype = c_uint
lib.ElHermitianTridiagEigPairPartial_c.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianTridiagEigPairPartial_c.restype = c_uint
lib.ElHermitianTridiagEigPairPartial_z.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianTridiagEigPairPartial_z.restype = c_uint
lib.ElHermitianTridiagEigPairPartialDist_s.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianTridiagEigPairPartialDist_s.restype = c_uint
lib.ElHermitianTridiagEigPairPartialDist_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianTridiagEigPairPartialDist_d.restype = c_uint
lib.ElHermitianTridiagEigPairPartialDist_c.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianTridiagEigPairPartialDist_c.restype = c_uint
lib.ElHermitianTridiagEigPairPartialDist_z.argtypes = \
  [c_void_p,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianTridiagEigPairPartialDist_z.restype = c_uint
def HermitianTridiagEig(d,dSub,vectors=False,sort=ASCENDING,subset=None):
  if type(d) is Matrix:
    w = Matrix(d.tag)
    if vectors:
      X = Matrix(dSub.tag)
      if subset == None:
        if   dSub.tag == sTag: 
          lib.ElHermitianTridiagEigPair_s(d.obj,dSub.obj,w.obj,X.obj,sort)
        elif dSub.tag == dTag:
          lib.ElHermitianTridiagEigPair_d(d.obj,dSub.obj,w.obj,X.obj,sort)
        elif dSub.tag == cTag:
          lib.ElHermitianTridiagEigPair_c(d.obj,dSub.obj,w.obj,X.obj,sort)
        elif dSub.tag == zTag:
          lib.ElHermitianTridiagEigPair_z(d.obj,dSub.obj,w.obj,X.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   dSub.tag == sTag: 
          lib.ElHermitianTridiagEigPairPartial_s \
          (d.obj,dSub.obj,w.obj,X.obj,sort,subset)
        elif dSub.tag == dTag:
          lib.ElHermitianTridiagEigPairPartial_d \
          (d.obj,dSub.obj,w.obj,X.obj,sort,subset)
        elif dSub.tag == cTag:
          lib.ElHermitianTridiagEigPairPartial_c \
          (d.obj,dSub.obj,w.obj,X.obj,sort,subset)
        elif dSub.tag == zTag:
          lib.ElHermitianTridiagEigPairPartial_z \
          (d.obj,dSub.obj,w.obj,X.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w, X
    else:
      if subset == None:
        if   dSub.tag == sTag: 
          lib.ElHermitianTridiagEigPair_s(d.obj,dSub.obj,w.obj,sort)
        elif dSub.tag == dTag:
          lib.ElHermitianTridiagEigPair_d(d.obj,dSub.obj,w.obj,sort)
        elif dSub.tag == cTag:
          lib.ElHermitianTridiagEigPair_c(d.obj,dSub.obj,w.obj,sort)
        elif dSub.tag == zTag:
          lib.ElHermitianTridiagEigPair_z(d.obj,dSub.obj,w.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   dSub.tag == sTag: 
          lib.ElHermitianTridiagEigPairPartial_s \
          (d.obj,dSub.obj,w.obj,sort,subset)
        elif dSub.tag == dTag:
          lib.ElHermitianTridiagEigPairPartial_d \
          (d.obj,dSub.obj,w.obj,sort,subset)
        elif dSub.tag == cTag:
          lib.ElHermitianTridiagEigPairPartial_c \
          (d.obj,dSub.obj,w.obj,sort,subset)
        elif dSub.tag == zTag:
          lib.ElHermitianTridiagEigPairPartial_z \
          (d.obj,dSub.obj,w.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w
  elif type(d) is DistMatrix:
    w = DistMatrix(d.tag,STAR,STAR,d.Grid())
    if vectors:
      X = DistMatrix(dSub.tag,STAR,VR,dSub.Grid())
      if subset == None:
        if   dSub.tag == sTag: 
          lib.ElHermitianTridiagEigPairDist_s(d.obj,dSub.obj,w.obj,X.obj,sort)
        elif dSub.tag == dTag:
          lib.ElHermitianTridiagEigPairDist_d(d.obj,dSub.obj,w.obj,X.obj,sort)
        elif dSub.tag == cTag:
          lib.ElHermitianTridiagEigPairDist_c(d.obj,dSub.obj,w.obj,X.obj,sort)
        elif dSub.tag == zTag:
          lib.ElHermitianTridiagEigPairDist_z(d.obj,dSub.obj,w.obj,X.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   dSub.tag == sTag: 
          lib.ElHermitianTridiagEigPairPartialDist_s \
          (d.obj,dSub.obj,w.obj,X.obj,sort,subset)
        elif dSub.tag == dTag:
          lib.ElHermitianTridiagEigPairPartialDist_d \
          (d.obj,dSub.obj,w.obj,X.obj,sort,subset)
        elif dSub.tag == cTag:
          lib.ElHermitianTridiagEigPairPartialDist_c \
          (d.obj,dSub.obj,w.obj,X.obj,sort,subset)
        elif dSub.tag == zTag:
          lib.ElHermitianTridiagEigPairPartialDist_z \
          (d.obj,dSub.obj,w.obj,X.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w, X
    else:
      if subset == None:
        if   dSub.tag == sTag: 
          lib.ElHermitianTridiagEigPairDist_s(d.obj,dSub.obj,w.obj,sort)
        elif dSub.tag == dTag:
          lib.ElHermitianTridiagEigPairDist_d(d.obj,dSub.obj,w.obj,sort)
        elif dSub.tag == cTag:
          lib.ElHermitianTridiagEigPairDist_c(d.obj,dSub.obj,w.obj,sort)
        elif dSub.tag == zTag:
          lib.ElHermitianTridiagEigPairDist_z(d.obj,dSub.obj,w.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   dSub.tag == sTag: 
          lib.ElHermitianTridiagEigPairPartialDist_s \
          (d.obj,dSub.obj,w.obj,sort,subset)
        elif dSub.tag == dTag:
          lib.ElHermitianTridiagEigPairPartialDist_d \
          (d.obj,dSub.obj,w.obj,sort,subset)
        elif dSub.tag == cTag:
          lib.ElHermitianTridiagEigPairPartialDist_c \
          (d.obj,dSub.obj,w.obj,sort,subset)
        elif dSub.tag == zTag:
          lib.ElHermitianTridiagEigPairPartialDist_z \
          (d.obj,dSub.obj,w.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w
  else: raise Exception('Unsupported matrix type')

# Hermitian eigensolvers
# ======================
lib.ElHermitianEig_s.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElHermitianEig_s.restype = c_uint
lib.ElHermitianEig_d.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElHermitianEig_d.restype = c_uint
lib.ElHermitianEig_c.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElHermitianEig_c.restype = c_uint
lib.ElHermitianEig_z.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElHermitianEig_z.restype = c_uint
lib.ElHermitianEigDist_s.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElHermitianEigDist_s.restype = c_uint
lib.ElHermitianEigDist_d.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElHermitianEigDist_d.restype = c_uint
lib.ElHermitianEigDist_c.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElHermitianEigDist_c.restype = c_uint
lib.ElHermitianEigDist_z.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElHermitianEigDist_z.restype = c_uint
lib.ElHermitianEigPair_s.argtypes = [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianEigPair_s.restype = c_uint
lib.ElHermitianEigPair_d.argtypes = [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianEigPair_d.restype = c_uint
lib.ElHermitianEigPair_c.argtypes = [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianEigPair_c.restype = c_uint
lib.ElHermitianEigPair_z.argtypes = [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianEigPair_z.restype = c_uint
lib.ElHermitianEigPairDist_s.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianEigPairDist_s.restype = c_uint
lib.ElHermitianEigPairDist_d.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianEigPairDist_d.restype = c_uint
lib.ElHermitianEigPairDist_c.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianEigPairDist_c.restype = c_uint
lib.ElHermitianEigPairDist_z.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianEigPairDist_z.restype = c_uint

lib.ElHermitianEigPartial_s.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianEigPartial_s.restype = c_uint
lib.ElHermitianEigPartial_d.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianEigPartial_d.restype = c_uint
lib.ElHermitianEigPartial_c.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianEigPartial_c.restype = c_uint
lib.ElHermitianEigPartial_z.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianEigPartial_z.restype = c_uint
lib.ElHermitianEigPartialDist_s.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianEigPartialDist_s.restype = c_uint
lib.ElHermitianEigPartialDist_d.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianEigPartialDist_d.restype = c_uint
lib.ElHermitianEigPartialDist_c.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianEigPartialDist_c.restype = c_uint
lib.ElHermitianEigPartialDist_z.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianEigPartialDist_z.restype = c_uint
lib.ElHermitianEigPairPartial_s.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianEigPairPartial_s.restype = c_uint
lib.ElHermitianEigPairPartial_d.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianEigPairPartial_d.restype = c_uint
lib.ElHermitianEigPairPartial_c.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianEigPairPartial_c.restype = c_uint
lib.ElHermitianEigPairPartial_z.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianEigPairPartial_z.restype = c_uint
lib.ElHermitianEigPairPartialDist_s.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianEigPairPartialDist_s.restype = c_uint
lib.ElHermitianEigPairPartialDist_d.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianEigPairPartialDist_d.restype = c_uint
lib.ElHermitianEigPairPartialDist_c.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianEigPairPartialDist_c.restype = c_uint
lib.ElHermitianEigPairPartialDist_z.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianEigPairPartialDist_z.restype = c_uint
def HermitianEig(uplo,A,vectors=False,sort=ASCENDING,subset=None):
  if type(A) is Matrix:
    w = Matrix(A.tag)
    if vectors:
      X = Matrix(Base(A.tag))
      if subset == None:
        if   A.tag == sTag: 
          lib.ElHermitianEigPair_s(uplo,A.obj,w.obj,X.obj,sort)
        elif A.tag == dTag:
          lib.ElHermitianEigPair_d(uplo,A.obj,w.obj,X.obj,sort)
        elif A.tag == cTag:
          lib.ElHermitianEigPair_c(uplo,A.obj,w.obj,X.obj,sort)
        elif A.tag == zTag:
          lib.ElHermitianEigPair_z(uplo,A.obj,w.obj,X.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   A.tag == sTag: 
          lib.ElHermitianEigPairPartial_s(uplo,A.obj,w.obj,X.obj,sort,subset)
        elif A.tag == dTag:
          lib.ElHermitianEigPairPartial_d(uplo,A.obj,w.obj,X.obj,sort,subset)
        elif A.tag == cTag:
          lib.ElHermitianEigPairPartial_c(uplo,A.obj,w.obj,X.obj,sort,subset)
        elif A.tag == zTag:
          lib.ElHermitianEigPairPartial_z(uplo,A.obj,w.obj,X.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w, X
    else:
      if subset == None:
        if   A.tag == sTag: lib.ElHermitianEigPair_s(uplo,A.obj,w.obj,sort)
        elif A.tag == dTag: lib.ElHermitianEigPair_d(uplo,A.obj,w.obj,sort)
        elif A.tag == cTag: lib.ElHermitianEigPair_c(uplo,A.obj,w.obj,sort)
        elif A.tag == zTag: lib.ElHermitianEigPair_z(uplo,A.obj,w.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   A.tag == sTag: 
          lib.ElHermitianEigPairPartial_s(uplo,A.obj,w.obj,sort,subset)
        elif A.tag == dTag:
          lib.ElHermitianEigPairPartial_d(uplo,A.obj,w.obj,sort,subset)
        elif A.tag == cTag:
          lib.ElHermitianEigPairPartial_c(uplo,A.obj,w.obj,sort,subset)
        elif A.tag == zTag:
          lib.ElHermitianEigPairPartial_z(uplo,A.obj,w.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w
  elif type(A) is DistMatrix:
    w = DistMatrix(Base(A.tag),STAR,STAR,A.Grid())
    if vectors:
      X = DistMatrix(A.tag,MC,MR,dSub.Grid())
      if subset == None:
        if   A.tag == sTag: 
          lib.ElHermitianEigPairDist_s(uplo,A.obj,w.obj,X.obj,sort)
        elif A.tag == dTag:
          lib.ElHermitianEigPairDist_d(uplo,A.obj,w.obj,X.obj,sort)
        elif A.tag == cTag:
          lib.ElHermitianEigPairDist_c(uplo,A.obj,w.obj,X.obj,sort)
        elif A.tag == zTag:
          lib.ElHermitianEigPairDist_z(uplo,A.obj,w.obj,X.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   A.tag == sTag: 
          lib.ElHermitianEigPairPartialDist_s \
          (uplo,A.obj,w.obj,X.obj,sort,subset)
        elif A.tag == dTag:
          lib.ElHermitianEigPairPartialDist_d \
          (uplo,A.obj,w.obj,X.obj,sort,subset)
        elif A.tag == cTag:
          lib.ElHermitianEigPairPartialDist_c \
          (uplo,A.obj,w.obj,X.obj,sort,subset)
        elif A.tag == zTag:
          lib.ElHermitianEigPairPartialDist_z \
          (uplo,A.obj,w.obj,X.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w, X
    else:
      if subset == None:
        if   A.tag == sTag: lib.ElHermitianEigPairDist_s(uplo,A.obj,w.obj,sort)
        elif A.tag == dTag: lib.ElHermitianEigPairDist_d(uplo,A.obj,w.obj,sort)
        elif A.tag == cTag: lib.ElHermitianEigPairDist_c(uplo,A.obj,w.obj,sort)
        elif A.tag == zTag: lib.ElHermitianEigPairDist_z(uplo,A.obj,w.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   A.tag == sTag: 
          lib.ElHermitianEigPairPartialDist_s(uplo,A.obj,w.obj,sort,subset)
        elif A.tag == dTag:
          lib.ElHermitianEigPairPartialDist_d(uplo,A.obj,w.obj,sort,subset)
        elif A.tag == cTag:
          lib.ElHermitianEigPairPartialDist_c(uplo,A.obj,w.obj,sort,subset)
        elif A.tag == zTag:
          lib.ElHermitianEigPairPartialDist_z(uplo,A.obj,w.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w
  else: raise Exception('Unsupported matrix type')

# Skew-Hermitian eigensolvers
# ===========================
lib.ElSkewHermitianEig_s.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEig_s.restype = c_uint
lib.ElSkewHermitianEig_d.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEig_d.restype = c_uint
lib.ElSkewHermitianEig_c.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEig_c.restype = c_uint
lib.ElSkewHermitianEig_z.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEig_z.restype = c_uint
lib.ElSkewHermitianEigDist_s.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEigDist_s.restype = c_uint
lib.ElSkewHermitianEigDist_d.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEigDist_d.restype = c_uint
lib.ElSkewHermitianEigDist_c.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEigDist_c.restype = c_uint
lib.ElSkewHermitianEigDist_z.argtypes = [c_uint,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEigDist_z.restype = c_uint
lib.ElSkewHermitianEigPair_s.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEigPair_s.restype = c_uint
lib.ElSkewHermitianEigPair_d.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEigPair_d.restype = c_uint
lib.ElSkewHermitianEigPair_c.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEigPair_c.restype = c_uint
lib.ElSkewHermitianEigPair_z.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEigPair_z.restype = c_uint
lib.ElSkewHermitianEigPairDist_s.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEigPairDist_s.restype = c_uint
lib.ElSkewHermitianEigPairDist_d.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEigPairDist_d.restype = c_uint
lib.ElSkewHermitianEigPairDist_c.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEigPairDist_c.restype = c_uint
lib.ElSkewHermitianEigPairDist_z.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElSkewHermitianEigPairDist_z.restype = c_uint

lib.ElSkewHermitianEigPartial_s.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElSkewHermitianEigPartial_s.restype = c_uint
lib.ElSkewHermitianEigPartial_d.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElSkewHermitianEigPartial_d.restype = c_uint
lib.ElSkewHermitianEigPartial_c.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElSkewHermitianEigPartial_c.restype = c_uint
lib.ElSkewHermitianEigPartial_z.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElSkewHermitianEigPartial_z.restype = c_uint
lib.ElSkewHermitianEigPartialDist_s.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElSkewHermitianEigPartialDist_s.restype = c_uint
lib.ElSkewHermitianEigPartialDist_d.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElSkewHermitianEigPartialDist_d.restype = c_uint
lib.ElSkewHermitianEigPartialDist_c.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElSkewHermitianEigPartialDist_c.restype = c_uint
lib.ElSkewHermitianEigPartialDist_z.argtypes = \
  [c_uint,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElSkewHermitianEigPartialDist_z.restype = c_uint
lib.ElSkewHermitianEigPairPartial_s.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElSkewHermitianEigPairPartial_s.restype = c_uint
lib.ElSkewHermitianEigPairPartial_d.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElSkewHermitianEigPairPartial_d.restype = c_uint
lib.ElSkewHermitianEigPairPartial_c.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElSkewHermitianEigPairPartial_c.restype = c_uint
lib.ElSkewHermitianEigPairPartial_z.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElSkewHermitianEigPairPartial_z.restype = c_uint
lib.ElSkewHermitianEigPairPartialDist_s.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElSkewHermitianEigPairPartialDist_s.restype = c_uint
lib.ElSkewHermitianEigPairPartialDist_d.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElSkewHermitianEigPairPartialDist_d.restype = c_uint
lib.ElSkewHermitianEigPairPartialDist_c.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElSkewHermitianEigPairPartialDist_c.restype = c_uint
lib.ElSkewHermitianEigPairPartialDist_z.argtypes = \
  [c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElSkewHermitianEigPairPartialDist_z.restype = c_uint
def SkewHermitianEig(uplo,A,vectors=False,sort=ASCENDING,subset=None):
  if type(A) is Matrix:
    w = Matrix(A.tag)
    if vectors:
      X = Matrix(Base(A.tag))
      if subset == None:
        if   A.tag == sTag: 
          lib.ElSkewHermitianEigPair_s(uplo,A.obj,w.obj,X.obj,sort)
        elif A.tag == dTag:
          lib.ElSkewHermitianEigPair_d(uplo,A.obj,w.obj,X.obj,sort)
        elif A.tag == cTag:
          lib.ElSkewHermitianEigPair_c(uplo,A.obj,w.obj,X.obj,sort)
        elif A.tag == zTag:
          lib.ElSkewHermitianEigPair_z(uplo,A.obj,w.obj,X.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   A.tag == sTag: 
          lib.ElSkewHermitianEigPairPartial_s \
          (uplo,A.obj,w.obj,X.obj,sort,subset)
        elif A.tag == dTag:
          lib.ElSkewHermitianEigPairPartial_d \
          (uplo,A.obj,w.obj,X.obj,sort,subset)
        elif A.tag == cTag:
          lib.ElSkewHermitianEigPairPartial_c \
          (uplo,A.obj,w.obj,X.obj,sort,subset)
        elif A.tag == zTag:
          lib.ElSkewHermitianEigPairPartial_z \
          (uplo,A.obj,w.obj,X.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w, X
    else:
      if subset == None:
        if   A.tag == sTag: lib.ElSkewHermitianEigPair_s(uplo,A.obj,w.obj,sort)
        elif A.tag == dTag: lib.ElSkewHermitianEigPair_d(uplo,A.obj,w.obj,sort)
        elif A.tag == cTag: lib.ElSkewHermitianEigPair_c(uplo,A.obj,w.obj,sort)
        elif A.tag == zTag: lib.ElSkewHermitianEigPair_z(uplo,A.obj,w.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   A.tag == sTag: 
          lib.ElSkewHermitianEigPairPartial_s(uplo,A.obj,w.obj,sort,subset)
        elif A.tag == dTag:
          lib.ElSkewHermitianEigPairPartial_d(uplo,A.obj,w.obj,sort,subset)
        elif A.tag == cTag:
          lib.ElSkewHermitianEigPairPartial_c(uplo,A.obj,w.obj,sort,subset)
        elif A.tag == zTag:
          lib.ElSkewHermitianEigPairPartial_z(uplo,A.obj,w.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w
  elif type(A) is DistMatrix:
    w = DistMatrix(Base(A.tag),STAR,STAR,A.Grid())
    if vectors:
      X = DistMatrix(A.tag,MC,MR,dSub.Grid())
      if subset == None:
        if   A.tag == sTag: 
          lib.ElSkewHermitianEigPairDist_s(uplo,A.obj,w.obj,X.obj,sort)
        elif A.tag == dTag:
          lib.ElSkewHermitianEigPairDist_d(uplo,A.obj,w.obj,X.obj,sort)
        elif A.tag == cTag:
          lib.ElSkewHermitianEigPairDist_c(uplo,A.obj,w.obj,X.obj,sort)
        elif A.tag == zTag:
          lib.ElSkewHermitianEigPairDist_z(uplo,A.obj,w.obj,X.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   A.tag == sTag: 
          lib.ElSkewHermitianEigPairPartialDist_s \
          (uplo,A.obj,w.obj,X.obj,sort,subset)
        elif A.tag == dTag:
          lib.ElSkewHermitianEigPairPartialDist_d \
          (uplo,A.obj,w.obj,X.obj,sort,subset)
        elif A.tag == cTag:
          lib.ElSkewHermitianEigPairPartialDist_c \
          (uplo,A.obj,w.obj,X.obj,sort,subset)
        elif A.tag == zTag:
          lib.ElSkewHermitianEigPairPartialDist_z \
          (uplo,A.obj,w.obj,X.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w, X
    else:
      if subset == None:
        if   A.tag == sTag: 
          lib.ElSkewHermitianEigPairDist_s(uplo,A.obj,w.obj,sort)
        elif A.tag == dTag: 
          lib.ElSkewHermitianEigPairDist_d(uplo,A.obj,w.obj,sort)
        elif A.tag == cTag: 
          lib.ElSkewHermitianEigPairDist_c(uplo,A.obj,w.obj,sort)
        elif A.tag == zTag: 
          lib.ElSkewHermitianEigPairDist_z(uplo,A.obj,w.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   A.tag == sTag: 
          lib.ElSkewHermitianEigPairPartialDist_s(uplo,A.obj,w.obj,sort,subset)
        elif A.tag == dTag:
          lib.ElSkewHermitianEigPairPartialDist_d(uplo,A.obj,w.obj,sort,subset)
        elif A.tag == cTag:
          lib.ElSkewHermitianEigPairPartialDist_c(uplo,A.obj,w.obj,sort,subset)
        elif A.tag == zTag:
          lib.ElSkewHermitianEigPairPartialDist_z(uplo,A.obj,w.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w
  else: raise Exception('Unsupported matrix type')

# Hermitian generalized-definite eigensolvers
# ===========================================
lib.ElHermitianGenDefEig_s.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEig_s.restype = c_uint
lib.ElHermitianGenDefEig_d.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEig_d.restype = c_uint
lib.ElHermitianGenDefEig_c.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEig_c.restype = c_uint
lib.ElHermitianGenDefEig_z.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEig_z.restype = c_uint
lib.ElHermitianGenDefEigDist_s.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEigDist_s.restype = c_uint
lib.ElHermitianGenDefEigDist_d.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEigDist_d.restype = c_uint
lib.ElHermitianGenDefEigDist_c.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEigDist_c.restype = c_uint
lib.ElHermitianGenDefEigDist_z.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEigDist_z.restype = c_uint
lib.ElHermitianGenDefEigPair_s.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEigPair_s.restype = c_uint
lib.ElHermitianGenDefEigPair_d.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEigPair_d.restype = c_uint
lib.ElHermitianGenDefEigPair_c.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEigPair_c.restype = c_uint
lib.ElHermitianGenDefEigPair_z.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEigPair_z.restype = c_uint
lib.ElHermitianGenDefEigPairDist_s.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEigPairDist_s.restype = c_uint
lib.ElHermitianGenDefEigPairDist_d.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEigPairDist_d.restype = c_uint
lib.ElHermitianGenDefEigPairDist_c.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEigPairDist_c.restype = c_uint
lib.ElHermitianGenDefEigPairDist_z.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint]
lib.ElHermitianGenDefEigPairDist_z.restype = c_uint

lib.ElHermitianGenDefEigPartial_s.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianGenDefEigPartial_s.restype = c_uint
lib.ElHermitianGenDefEigPartial_d.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianGenDefEigPartial_d.restype = c_uint
lib.ElHermitianGenDefEigPartial_c.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianGenDefEigPartial_c.restype = c_uint
lib.ElHermitianGenDefEigPartial_z.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianGenDefEigPartial_z.restype = c_uint
lib.ElHermitianGenDefEigPartialDist_s.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianGenDefEigPartialDist_s.restype = c_uint
lib.ElHermitianGenDefEigPartialDist_d.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianGenDefEigPartialDist_d.restype = c_uint
lib.ElHermitianGenDefEigPartialDist_c.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_s]
lib.ElHermitianGenDefEigPartialDist_c.restype = c_uint
lib.ElHermitianGenDefEigPartialDist_z.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_uint,HermitianEigSubset_d]
lib.ElHermitianGenDefEigPartialDist_z.restype = c_uint
lib.ElHermitianGenDefEigPairPartial_s.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint,
   HermitianEigSubset_s]
lib.ElHermitianGenDefEigPairPartial_s.restype = c_uint
lib.ElHermitianGenDefEigPairPartial_d.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint,
   HermitianEigSubset_d]
lib.ElHermitianGenDefEigPairPartial_d.restype = c_uint
lib.ElHermitianGenDefEigPairPartial_c.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint,
   HermitianEigSubset_s]
lib.ElHermitianGenDefEigPairPartial_c.restype = c_uint
lib.ElHermitianGenDefEigPairPartial_z.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint,
   HermitianEigSubset_d]
lib.ElHermitianGenDefEigPairPartial_z.restype = c_uint
lib.ElHermitianGenDefEigPairPartialDist_s.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint,
   HermitianEigSubset_s]
lib.ElHermitianGenDefEigPairPartialDist_s.restype = c_uint
lib.ElHermitianGenDefEigPairPartialDist_d.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint,
   HermitianEigSubset_d]
lib.ElHermitianGenDefEigPairPartialDist_d.restype = c_uint
lib.ElHermitianGenDefEigPairPartialDist_c.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint,
   HermitianEigSubset_s]
lib.ElHermitianGenDefEigPairPartialDist_c.restype = c_uint
lib.ElHermitianGenDefEigPairPartialDist_z.argtypes = \
  [c_uint,c_uint,c_void_p,c_void_p,c_void_p,c_void_p,c_uint,
   HermitianEigSubset_d]
lib.ElHermitianGenDefEigPairPartialDist_z.restype = c_uint
def HermitianGenDefEig(uplo,A,vectors=False,sort=ASCENDING,subset=None):
  if type(A) is Matrix:
    w = Matrix(A.tag)
    if vectors:
      X = Matrix(Base(A.tag))
      if subset == None:
        if   A.tag == sTag: 
          lib.ElHermitianGenDefEigPair_s \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort)
        elif A.tag == dTag:
          lib.ElHermitianGenDefEigPair_d \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort)
        elif A.tag == cTag:
          lib.ElHermitianGenDefEigPair_c \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort)
        elif A.tag == zTag:
          lib.ElHermitianGenDefEigPair_z \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   A.tag == sTag: 
          lib.ElHermitianGenDefEigPairPartial_s \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort,subset)
        elif A.tag == dTag:
          lib.ElHermitianGenDefEigPairPartial_d \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort,subset)
        elif A.tag == cTag:
          lib.ElHermitianGenDefEigPairPartial_c \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort,subset)
        elif A.tag == zTag:
          lib.ElHermitianGenDefEigPairPartial_z \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w, X
    else:
      if subset == None:
        if   A.tag == sTag: 
          lib.ElHermitianGenDefEigPair_s(pencil,uplo,A.obj,B.obj,w.obj,sort)
        elif A.tag == dTag: 
          lib.ElHermitianGenDefEigPair_d(pencil,uplo,A.obj,B.obj,w.obj,sort)
        elif A.tag == cTag: 
          lib.ElHermitianGenDefEigPair_c(pencil,uplo,A.obj,B.obj,w.obj,sort)
        elif A.tag == zTag: 
          lib.ElHermitianGenDefEigPair_z(pencil,uplo,A.obj,B.obj,w.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   A.tag == sTag: 
          lib.ElHermitianGenDefEigPairPartial_s \
          (pencil,uplo,A.obj,B.obj,w.obj,sort,subset)
        elif A.tag == dTag:
          lib.ElHermitianGenDefEigPairPartial_d \
          (pencil,uplo,A.obj,B.obj,w.obj,sort,subset)
        elif A.tag == cTag:
          lib.ElHermitianGenDefEigPairPartial_c \
          (pencil,uplo,A.obj,B.obj,w.obj,sort,subset)
        elif A.tag == zTag:
          lib.ElHermitianGenDefEigPairPartial_z \
          (pencil,uplo,A.obj,B.obj,w.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w
  elif type(A) is DistMatrix:
    w = DistMatrix(Base(A.tag),STAR,STAR,A.Grid())
    if vectors:
      X = DistMatrix(A.tag,MC,MR,dSub.Grid())
      if subset == None:
        if   A.tag == sTag: 
          lib.ElHermitianGenDefEigPairDist_s \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort)
        elif A.tag == dTag:
          lib.ElHermitianGenDefEigPairDist_d \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort)
        elif A.tag == cTag:
          lib.ElHermitianGenDefEigPairDist_c \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort)
        elif A.tag == zTag:
          lib.ElHermitianGenDefEigPairDist_z \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   A.tag == sTag: 
          lib.ElHermitianGenDefEigPairPartialDist_s \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort,subset)
        elif A.tag == dTag:
          lib.ElHermitianGenDefEigPairPartialDist_d \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort,subset)
        elif A.tag == cTag:
          lib.ElHermitianGenDefEigPairPartialDist_c \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort,subset)
        elif A.tag == zTag:
          lib.ElHermitianGenDefEigPairPartialDist_z \
          (pencil,uplo,A.obj,B.obj,w.obj,X.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w, X
    else:
      if subset == None:
        if   A.tag == sTag: 
          lib.ElHermitianGenDefEigPairDist_s(pencil,uplo,A.obj,B.obj,w.obj,sort)
        elif A.tag == dTag: 
          lib.ElHermitianGenDefEigPairDist_d(pencil,uplo,A.obj,B.obj,w.obj,sort)
        elif A.tag == cTag: 
          lib.ElHermitianGenDefEigPairDist_c(pencil,uplo,A.obj,B.obj,w.obj,sort)
        elif A.tag == zTag: 
          lib.ElHermitianGenDefEigPairDist_z(pencil,uplo,A.obj,B.obj,w.obj,sort)
        else: raise Exception('Unsupported datatype')
      else:
        if   A.tag == sTag: 
          lib.ElHermitianGenDefEigPairPartialDist_s \
          (pencil,uplo,A.obj,B.obj,w.obj,sort,subset)
        elif A.tag == dTag:
          lib.ElHermitianGenDefEigPairPartialDist_d \
          (pencil,uplo,A.obj,B.obj,w.obj,sort,subset)
        elif A.tag == cTag:
          lib.ElHermitianGenDefEigPairPartialDist_c \
          (pencil,uplo,A.obj,B.obj,w.obj,sort,subset)
        elif A.tag == zTag:
          lib.ElHermitianGenDefEigPairPartialDist_z \
          (pencil,uplo,A.obj,B.obj,w.obj,sort,subset)
        else: raise Exception('Unsupported datatype')
      return w
  else: raise Exception('Unsupported matrix type')

# Hermitian SVD
# =============
lib.ElHermitianSingularValues_s.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianSingularValues_s.restype = c_uint
lib.ElHermitianSingularValues_d.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianSingularValues_d.restype = c_uint
lib.ElHermitianSingularValues_c.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianSingularValues_c.restype = c_uint
lib.ElHermitianSingularValues_z.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianSingularValues_z.restype = c_uint
lib.ElHermitianSingularValuesDist_s.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianSingularValuesDist_s.restype = c_uint
lib.ElHermitianSingularValuesDist_d.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianSingularValuesDist_d.restype = c_uint
lib.ElHermitianSingularValuesDist_c.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianSingularValuesDist_c.restype = c_uint
lib.ElHermitianSingularValuesDist_z.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianSingularValuesDist_z.restype = c_uint
lib.ElHermitianSVD_s.argtypes = [c_uint,c_void_p,c_void_p,c_void_p,c_void_p]
lib.ElHermitianSVD_s.restype = c_uint
lib.ElHermitianSVD_d.argtypes = [c_uint,c_void_p,c_void_p,c_void_p,c_void_p]
lib.ElHermitianSVD_d.restype = c_uint
lib.ElHermitianSVD_c.argtypes = [c_uint,c_void_p,c_void_p,c_void_p,c_void_p]
lib.ElHermitianSVD_c.restype = c_uint
lib.ElHermitianSVD_z.argtypes = [c_uint,c_void_p,c_void_p,c_void_p,c_void_p]
lib.ElHermitianSVD_z.restype = c_uint
lib.ElHermitianSVDDist_s.argtypes = [c_uint,c_void_p,c_void_p,c_void_p,c_void_p]
lib.ElHermitianSVDDist_s.restype = c_uint
lib.ElHermitianSVDDist_d.argtypes = [c_uint,c_void_p,c_void_p,c_void_p,c_void_p]
lib.ElHermitianSVDDist_d.restype = c_uint
lib.ElHermitianSVDDist_c.argtypes = [c_uint,c_void_p,c_void_p,c_void_p,c_void_p]
lib.ElHermitianSVDDist_c.restype = c_uint
lib.ElHermitianSVDDist_z.argtypes = [c_uint,c_void_p,c_void_p,c_void_p,c_void_p]
lib.ElHermitianSVDDist_z.restype = c_uint
def HermitianSVD(uplo,A,vectors=True):
  if type(A) is Matrix:
    s = Matrix(Base(A.tag))
    if vectors:
      U = Matrix(A.tag)
      V = Matrix(A.tag)
      if   A.tag == sTag: lib.ElHermitianSVD_s(uplo,A.obj,s.obj,U.obj,V.obj)
      elif A.tag == dTag: lib.ElHermitianSVD_d(uplo,A.obj,s.obj,U.obj,V.obj)
      elif A.tag == cTag: lib.ElHermitianSVD_c(uplo,A.obj,s.obj,U.obj,V.obj)
      elif A.tag == zTag: lib.ElHermitianSVD_z(uplo,A.obj,s.obj,U.obj,V.obj)
      else: raise Exception('Unsupported datatype')
      return U, s, V 
    else:
      if   A.tag == sTag: lib.ElHermitianSingularValues_s(uplo,A.obj,s.obj)
      elif A.tag == dTag: lib.ElHermitianSingularValues_d(uplo,A.obj,s.obj)
      elif A.tag == cTag: lib.ElHermitianSingularValues_c(uplo,A.obj,s.obj)
      elif A.tag == zTag: lib.ElHermitianSingularValues_z(uplo,A.obj,s.obj)
      else: raise Exception('Unsupported datatype')
    return s
  elif type(A) is DistMatrix:
    s = DistMatrix(Base(A.tag),STAR,STAR,A.Grid())
    if vectors:
      U = DistMatrix(A.tag,MC,MR,A.Grid())
      V = DistMatrix(A.tag,MC,MR,A.Grid())
      if   A.tag == sTag: lib.ElHermitianSVDDist_s(uplo,A.obj,s.obj,U.obj,V.obj)
      elif A.tag == dTag: lib.ElHermitianSVDDist_d(uplo,A.obj,s.obj,U.obj,V.obj)
      elif A.tag == cTag: lib.ElHermitianSVDDist_c(uplo,A.obj,s.obj,U.obj,V.obj)
      elif A.tag == zTag: lib.ElHermitianSVDDist_z(uplo,A.obj,s.obj,U.obj,V.obj)
      else: raise Exception('Unsupported datatype')
      return U, s, V 
    else:
      if   A.tag == sTag: lib.ElHermitianSingularValuesDist_s(uplo,A.obj,s.obj)
      elif A.tag == dTag: lib.ElHermitianSingularValuesDist_d(uplo,A.obj,s.obj)
      elif A.tag == cTag: lib.ElHermitianSingularValuesDist_c(uplo,A.obj,s.obj)
      elif A.tag == zTag: lib.ElHermitianSingularValuesDist_z(uplo,A.obj,s.obj)
      else: raise Exception('Unsupported datatype')
    return s
  else: raise Exception('Unsupported matrix type')

# Polar decomposition
# ===================
lib.ElPolar_s.argtypes = [c_void_p]
lib.ElPolar_s.restype = c_uint
lib.ElPolar_d.argtypes = [c_void_p]
lib.ElPolar_d.restype = c_uint
lib.ElPolar_c.argtypes = [c_void_p]
lib.ElPolar_c.restype = c_uint
lib.ElPolar_z.argtypes = [c_void_p]
lib.ElPolar_z.restype = c_uint
lib.ElPolarDist_s.argtypes = [c_void_p]
lib.ElPolarDist_s.restype = c_uint
lib.ElPolarDist_d.argtypes = [c_void_p]
lib.ElPolarDist_d.restype = c_uint
lib.ElPolarDist_c.argtypes = [c_void_p]
lib.ElPolarDist_c.restype = c_uint
lib.ElPolarDist_z.argtypes = [c_void_p]
lib.ElPolarDist_z.restype = c_uint
lib.ElPolarDecomp_s.argtypes = [c_void_p,c_void_p]
lib.ElPolarDecomp_s.restype = c_uint
lib.ElPolarDecomp_d.argtypes = [c_void_p,c_void_p]
lib.ElPolarDecomp_d.restype = c_uint
lib.ElPolarDecomp_c.argtypes = [c_void_p,c_void_p]
lib.ElPolarDecomp_c.restype = c_uint
lib.ElPolarDecomp_z.argtypes = [c_void_p,c_void_p]
lib.ElPolarDecomp_z.restype = c_uint
lib.ElPolarDecompDist_s.argtypes = [c_void_p,c_void_p]
lib.ElPolarDecompDist_s.restype = c_uint
lib.ElPolarDecompDist_d.argtypes = [c_void_p,c_void_p]
lib.ElPolarDecompDist_d.restype = c_uint
lib.ElPolarDecompDist_c.argtypes = [c_void_p,c_void_p]
lib.ElPolarDecompDist_c.restype = c_uint
lib.ElPolarDecompDist_z.argtypes = [c_void_p,c_void_p]
lib.ElPolarDecompDist_z.restype = c_uint
def Polar(A,fullDecomp=False):
  if type(A) is Matrix:
    if fullDecomp:
      P = Matrix(A.tag)
      if   A.tag == sTag: lib.ElPolarDecomp_s(A.obj,P.obj)
      elif A.tag == dTag: lib.ElPolarDecomp_d(A.obj,P.obj)
      elif A.tag == cTag: lib.ElPolarDecomp_c(A.obj,P.obj)
      elif A.tag == zTag: lib.ElPolarDecomp_z(A.obj,P.obj)
      else: raise Exception('Unsupported datatype')
      return P
    else:
      if   A.tag == sTag: lib.ElPolar_s(A.obj)
      elif A.tag == dTag: lib.ElPolar_d(A.obj)
      elif A.tag == cTag: lib.ElPolar_c(A.obj)
      elif A.tag == zTag: lib.ElPolar_z(A.obj)
      else: raise Exception('Unsupported datatype')
  elif type(A) is DistMatrix:
    if fullDecomp:
      P = DistMatrix(A.tag)
      if   A.tag == sTag: lib.ElPolarDecompDist_s(A.obj,P.obj)
      elif A.tag == dTag: lib.ElPolarDecompDist_d(A.obj,P.obj)
      elif A.tag == cTag: lib.ElPolarDecompDist_c(A.obj,P.obj)
      elif A.tag == zTag: lib.ElPolarDecompDist_z(A.obj,P.obj)
      else: raise Exception('Unsupported datatype')
      return P
    else:
      if   A.tag == sTag: lib.ElPolarDist_s(A.obj)
      elif A.tag == dTag: lib.ElPolarDist_d(A.obj)
      elif A.tag == cTag: lib.ElPolarDist_c(A.obj)
      elif A.tag == zTag: lib.ElPolarDist_z(A.obj)
      else: raise Exception('Unsupported datatype')
  else: raise Exception('Unsupported matrix type')

lib.ElHermitianPolar_s.argtypes = [c_uint,c_void_p]
lib.ElHermitianPolar_s.restype = c_uint
lib.ElHermitianPolar_d.argtypes = [c_uint,c_void_p]
lib.ElHermitianPolar_d.restype = c_uint
lib.ElHermitianPolar_c.argtypes = [c_uint,c_void_p]
lib.ElHermitianPolar_c.restype = c_uint
lib.ElHermitianPolar_z.argtypes = [c_uint,c_void_p]
lib.ElHermitianPolar_z.restype = c_uint
lib.ElHermitianPolarDist_s.argtypes = [c_uint,c_void_p]
lib.ElHermitianPolarDist_s.restype = c_uint
lib.ElHermitianPolarDist_d.argtypes = [c_uint,c_void_p]
lib.ElHermitianPolarDist_d.restype = c_uint
lib.ElHermitianPolarDist_c.argtypes = [c_uint,c_void_p]
lib.ElHermitianPolarDist_c.restype = c_uint
lib.ElHermitianPolarDist_z.argtypes = [c_uint,c_void_p]
lib.ElHermitianPolarDist_z.restype = c_uint
lib.ElHermitianPolarDecomp_s.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianPolarDecomp_s.restype = c_uint
lib.ElHermitianPolarDecomp_d.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianPolarDecomp_d.restype = c_uint
lib.ElHermitianPolarDecomp_c.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianPolarDecomp_c.restype = c_uint
lib.ElHermitianPolarDecomp_z.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianPolarDecomp_z.restype = c_uint
lib.ElHermitianPolarDecompDist_s.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianPolarDecompDist_s.restype = c_uint
lib.ElHermitianPolarDecompDist_d.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianPolarDecompDist_d.restype = c_uint
lib.ElHermitianPolarDecompDist_c.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianPolarDecompDist_c.restype = c_uint
lib.ElHermitianPolarDecompDist_z.argtypes = [c_uint,c_void_p,c_void_p]
lib.ElHermitianPolarDecompDist_z.restype = c_uint
def HermitianPolar(uplo,A,fullDecomp=False):
  if type(A) is Matrix:
    if fullDecomp:
      P = Matrix(A.tag)
      if   A.tag == sTag: lib.ElHermitianPolarDecomp_s(uplo,A.obj,P.obj)
      elif A.tag == dTag: lib.ElHermitianPolarDecomp_d(uplo,A.obj,P.obj)
      elif A.tag == cTag: lib.ElHermitianPolarDecomp_c(uplo,A.obj,P.obj)
      elif A.tag == zTag: lib.ElHermitianPolarDecomp_z(uplo,A.obj,P.obj)
      else: raise Exception('Unsupported datatype')
      return P
    else:
      if   A.tag == sTag: lib.ElHermitianPolar_s(uplo,A.obj)
      elif A.tag == dTag: lib.ElHermitianPolar_d(uplo,A.obj)
      elif A.tag == cTag: lib.ElHermitianPolar_c(uplo,A.obj)
      elif A.tag == zTag: lib.ElHermitianPolar_z(uplo,A.obj)
      else: raise Exception('Unsupported datatype')
  elif type(A) is DistMatrix:
    if fullDecomp:
      P = Matrix(A.tag)
      if   A.tag == sTag: lib.ElHermitianPolarDecompDist_s(uplo,A.obj,P.obj)
      elif A.tag == dTag: lib.ElHermitianPolarDecompDist_d(uplo,A.obj,P.obj)
      elif A.tag == cTag: lib.ElHermitianPolarDecompDist_c(uplo,A.obj,P.obj)
      elif A.tag == zTag: lib.ElHermitianPolarDecompDist_z(uplo,A.obj,P.obj)
      else: raise Exception('Unsupported datatype')
      return P
    else:
      if   A.tag == sTag: lib.ElHermitianPolarDist_s(uplo,A.obj)
      elif A.tag == dTag: lib.ElHermitianPolarDist_d(uplo,A.obj)
      elif A.tag == cTag: lib.ElHermitianPolarDist_c(uplo,A.obj)
      elif A.tag == zTag: lib.ElHermitianPolarDist_z(uplo,A.obj)
      else: raise Exception('Unsupported datatype')
  else: raise Exception('Unsupported matrix type')

# Schur decomposition
# ===================
lib.ElSchur_s.argtypes = [c_void_p,c_void_p,bType]
lib.ElSchur_s.restype = c_uint
lib.ElSchur_d.argtypes = [c_void_p,c_void_p,bType]
lib.ElSchur_d.restype = c_uint
lib.ElSchur_c.argtypes = [c_void_p,c_void_p,bType]
lib.ElSchur_c.restype = c_uint
lib.ElSchur_z.argtypes = [c_void_p,c_void_p,bType]
lib.ElSchur_z.restype = c_uint
lib.ElSchurDist_s.argtypes = [c_void_p,c_void_p,bType]
lib.ElSchurDist_s.restype = c_uint
lib.ElSchurDist_d.argtypes = [c_void_p,c_void_p,bType]
lib.ElSchurDist_d.restype = c_uint
lib.ElSchurDist_c.argtypes = [c_void_p,c_void_p,bType]
lib.ElSchurDist_c.restype = c_uint
lib.ElSchurDist_z.argtypes = [c_void_p,c_void_p,bType]
lib.ElSchurDist_z.restype = c_uint
lib.ElSchurDecomp_s.argtypes = [c_void_p,c_void_p,c_void_p,bType]
lib.ElSchurDecomp_s.restype = c_uint
lib.ElSchurDecomp_d.argtypes = [c_void_p,c_void_p,c_void_p,bType]
lib.ElSchurDecomp_d.restype = c_uint
lib.ElSchurDecomp_c.argtypes = [c_void_p,c_void_p,c_void_p,bType]
lib.ElSchurDecomp_c.restype = c_uint
lib.ElSchurDecomp_z.argtypes = [c_void_p,c_void_p,c_void_p,bType]
lib.ElSchurDecomp_z.restype = c_uint
lib.ElSchurDecompDist_s.argtypes = [c_void_p,c_void_p,c_void_p,bType]
lib.ElSchurDecompDist_s.restype = c_uint
lib.ElSchurDecompDist_d.argtypes = [c_void_p,c_void_p,c_void_p,bType]
lib.ElSchurDecompDist_d.restype = c_uint
lib.ElSchurDecompDist_c.argtypes = [c_void_p,c_void_p,c_void_p,bType]
lib.ElSchurDecompDist_c.restype = c_uint
lib.ElSchurDecompDist_z.argtypes = [c_void_p,c_void_p,c_void_p,bType]
lib.ElSchurDecompDist_z.restype = c_uint
def Schur(A,fullTriangle=True,vectors=False):
  if type(A) is Matrix:
    w = Matrix(Complexify(A.tag))
    if vectors:
      Q = Matrix(A.tag)
      if   A.tag == sTag: lib.ElSchurDecomp_s(A.obj,w.obj,Q.obj,fullTriangle)
      elif A.tag == dTag: lib.ElSchurDecomp_d(A.obj,w.obj,Q.obj,fullTriangle)
      elif A.tag == cTag: lib.ElSchurDecomp_c(A.obj,w.obj,Q.obj,fullTriangle)
      elif A.tag == zTag: lib.ElSchurDecomp_z(A.obj,w.obj,Q.obj,fullTriangle)
      else: raise Exception('Unsupported datatype')
      return w, Q
    else:
      if   A.tag == sTag: lib.ElSchur_s(A.obj,w.obj,fullTriangle)
      elif A.tag == dTag: lib.ElSchur_d(A.obj,w.obj,fullTriangle)
      elif A.tag == cTag: lib.ElSchur_c(A.obj,w.obj,fullTriangle)
      elif A.tag == zTag: lib.ElSchur_z(A.obj,w.obj,fullTriangle)
      else: raise Exception('Unsupported datatype')
      return w
  elif type(A) is DistMatrix:
    w = DistMatrix(Complexify(A.tag),STAR,STAR,A.Grid())
    if vectors:
      Q = DistMatrix(A.tag,MC,MR,A.Grid())
      if   A.tag == sTag: 
        lib.ElSchurDecompDist_s(A.obj,w.obj,Q.obj,fullTriangle)
      elif A.tag == dTag: 
        lib.ElSchurDecompDist_d(A.obj,w.obj,Q.obj,fullTriangle)
      elif A.tag == cTag: 
        lib.ElSchurDecompDist_c(A.obj,w.obj,Q.obj,fullTriangle)
      elif A.tag == zTag: 
        lib.ElSchurDecompDist_z(A.obj,w.obj,Q.obj,fullTriangle)
      else: raise Exception('Unsupported datatype')
      return w, Q
    else:
      if   A.tag == sTag: lib.ElSchurDist_s(A.obj,w.obj,fullTriangle)
      elif A.tag == dTag: lib.ElSchurDist_d(A.obj,w.obj,fullTriangle)
      elif A.tag == cTag: lib.ElSchurDist_c(A.obj,w.obj,fullTriangle)
      elif A.tag == zTag: lib.ElSchurDist_z(A.obj,w.obj,fullTriangle)
      else: raise Exception('Unsupported datatype')
      return w
  else: raise Exception('Unsupported matrix type')

# Singular value decomposition
# ============================
lib.ElSVD_s.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElSVD_s.restype = c_uint
lib.ElSVD_d.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElSVD_d.restype = c_uint
lib.ElSVD_c.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElSVD_c.restype = c_uint
lib.ElSVD_z.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElSVD_z.restype = c_uint
lib.ElSVDDist_s.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElSVDDist_s.restype = c_uint
lib.ElSVDDist_d.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElSVDDist_d.restype = c_uint
lib.ElSVDDist_c.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElSVDDist_c.restype = c_uint
lib.ElSVDDist_z.argtypes = [c_void_p,c_void_p,c_void_p]
lib.ElSVDDist_z.restype = c_uint
lib.ElSingularValues_s.argtypes = [c_void_p,c_void_p]
lib.ElSingularValues_s.restype = c_uint
lib.ElSingularValues_d.argtypes = [c_void_p,c_void_p]
lib.ElSingularValues_d.restype = c_uint
lib.ElSingularValues_c.argtypes = [c_void_p,c_void_p]
lib.ElSingularValues_c.restype = c_uint
lib.ElSingularValues_z.argtypes = [c_void_p,c_void_p]
lib.ElSingularValues_z.restype = c_uint
lib.ElSingularValuesDist_s.argtypes = [c_void_p,c_void_p]
lib.ElSingularValuesDist_s.restype = c_uint
lib.ElSingularValuesDist_d.argtypes = [c_void_p,c_void_p]
lib.ElSingularValuesDist_d.restype = c_uint
lib.ElSingularValuesDist_c.argtypes = [c_void_p,c_void_p]
lib.ElSingularValuesDist_c.restype = c_uint
lib.ElSingularValuesDist_z.argtypes = [c_void_p,c_void_p]
lib.ElSingularValuesDist_z.restype = c_uint
def SVD(A,vectors=False):
  if type(A) is Matrix:
    s = Matrix(Base(A.tag))
    if vectors:
      V = Matrix(A.tag)
      if   A.tag == sTag: lib.ElSVD_s(A.obj,s.obj,V.obj)
      elif A.tag == dTag: lib.ElSVD_d(A.obj,s.obj,V.obj)
      elif A.tag == cTag: lib.ElSVD_c(A.obj,s.obj,V.obj)
      elif A.tag == zTag: lib.ElSVD_z(A.obj,s.obj,V.obj)
      else: raise Exception('Unsupported datatype')
      return s, V
    else:
      if   A.tag == sTag: lib.ElSingularValues_s(A.obj,s.obj)
      elif A.tag == dTag: lib.ElSingularValues_d(A.obj,s.obj)
      elif A.tag == cTag: lib.ElSingularValues_c(A.obj,s.obj)
      elif A.tag == zTag: lib.ElSingularValues_z(A.obj,s.obj)
      else: raise Exception('Unsupported datatype')
      return s
  elif type(A) is DistMatrix:
    s = DistMatrix(Base(A.tag),STAR,STAR,A.Grid())
    if vectors:
      V = DistMatrix(A.tag,MC,MR,A.Grid())
      if   A.tag == sTag: lib.ElSVDDist_s(A.obj,s.obj,V.obj)
      elif A.tag == dTag: lib.ElSVDDist_d(A.obj,s.obj,V.obj)
      elif A.tag == cTag: lib.ElSVDDist_c(A.obj,s.obj,V.obj)
      elif A.tag == zTag: lib.ElSVDDist_z(A.obj,s.obj,V.obj)
      else: raise Exception('Unsupported datatype')
      return s, V
    else:
      if   A.tag == sTag: lib.ElSingularValuesDist_s(A.obj,s.obj)
      elif A.tag == dTag: lib.ElSingularValuesDist_d(A.obj,s.obj)
      elif A.tag == cTag: lib.ElSingularValuesDist_c(A.obj,s.obj)
      elif A.tag == zTag: lib.ElSingularValuesDist_z(A.obj,s.obj)
      else: raise Exception('Unsupported datatype')
      return s
  else: raise Exception('Unsupported matrix type')