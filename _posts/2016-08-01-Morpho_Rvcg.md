---
layout: post
tags: 
- R 
- RvtkStatismo
- Statismo


date: 2016-08-01 11:45:00 +0200
title: New Releases of Rvcg and Morpho&#58; new features, performance improvements and bugfixes
---

I am proudly presenting new new CRAN releases of **[Rvcg](https://cran.r-project.org/package=Rvcg)** and **[Morpho](https://cran.r-project.org/package=Morpho)**: 
The most significant changes are the optional use of external pointers to allow [reusable KD-Trees](/2016/03/09/Rvcg-XPTr/) and different mesh subdivision routines in Rvcg, and im/export of 3DSlicer fiducials and functions to sort curve semilandmarks and to make them equidistant. Below is the complete list of changes:

## Morpho 2.4

#### New features 

 * added `sortCurve` and `equidistantCurve`
 * added kappa statistic to` print.classify`
 * added `read/write.fcsv` to read write landmark in 3DSlicer format
 * added `prcompfast`, a faster and more memory efficient version of prcomp
 * `slider3d`: now sliding without specifying surfaces is possible. Surface is estimated by computing normals from point clouds using vcgUpdateNormals
 * added `plot` method for `slider3d`
 * added `fastKmeans` a very fast and efficient way to compute k-means clustering for 2D and 3D data.

#### bugfixes and minor changes 

 * fixed C++14 standard requirements
 * made index in `rmVertex` unique
 * `showPC`: for single PCs vectors of length> 1 are coerced to matrix
 * added option `margin` in `deformGrid3d` and `deformGrid2d`
 * unified code for creating bending energy matrix
 * made `relWarps` more memory and speed efficient and added option getBasis to disable (computationally expensive) calculation of vector basis.
 * added dimnames from rownames in `vecx`
 * `groupPCA`: returns Grandmean and Groupmeans as matrix/array for landmark data
 * correct output in `find.outliers` if `mahalanobis=TRUE` and add probability
 * added `reflection=FALSE` in` find.outliers` and corrected reported distances
 * fixed `read.lmdta` for single configs
 * `slider3d`: fixed case where all file infos are stored in sur.name
 * removed dependency yaImpute using `vcgKDtree` instead
 * added unit testing for `slider3d`
 * made `CreateL` and `tps3d` multi-threaded
 * added options `silent` to `slider3d` and `relaxLM`
 * ignore missing values when calculating quantiles and mindist in `meshDist`
 * refactored `CVA` and added unit test
 * fixed `predictPLSfromScores` for `ncomp=1`
 * fixed correct `lwd` passing in `deformGrid3d`
 * fixed `procAOVsym` for 2D case (correct df)
 * added unit test for `pls2B`
 * speed up `pls2B` by some orders of magnitude, now suitable for very large landmark configurations

### Rvcg 0.14

#### new features 
 
 * added `vcgBallPivoting`: ball pivoting surface reconstruction
 * added `vcgKmeans` a fast k-means clustering for 2D and 3D point clouds
 * added `vcgClostOnKDtreeFromBarycenters`, `vcgCreateKDtree, vcgCreateKDtreeFromBarycenters, vcgSearchKDtree `to allow reusing KD-Trees
 * added `vcgSubdivide` to refine an existing mesh by subidviding faces
 * added `vcgMetro` to compare differences between two meshes using different types of subsampling (thanks to F. Girinion)
 * added `vcgArea` to calculate the surface area of a mesh
 * added option `keep` to `vcgIsolated` and allowed options diameter/facenum to be used with `split=T`
 * updated vcglib to revision 5735
 * added `Rvcg::IOMesh::mesh3d2Rvcg<T>`, allowing easier conversion from mesh3d to vcglib meshtypes
 * added `checkFaceOrientation` to check whether a the outer layer of a surface mesh points outward

#### bug fixes

 * `vcgClost`: in case distances are beyond threshold, distance values are to NaN and a warning is issued
 * refactored and simplified C++ code


