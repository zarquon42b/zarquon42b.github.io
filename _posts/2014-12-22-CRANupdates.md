---
layout: post
tags: 
- R 

date: 2014-12-22 13:40:00 +0200
title: Updates&#58; Rvcg 0.10.1 and Morpho 2.2 on CRAN

---
New versions of my R-packages [Rvcg 0.10.1](http://cran.r-project.org/web/packages/Rvcg/) and [Morpho 2.2](http://cran.r-project.org/web/packages/Morpho/) are now available on [CRAN](http://cran.r-project.org/).

###Changes in Morpho since 2.0.3:

####New features

 * ```slider3d```, ```relaxLM and ```procSym``` now allow minimizing Procrustes distance
 * added orientation check in ```pcAlign``` to avoid reflections
 * massive speed improvements in sliding semi-landmarks routines
 * added options missing/missingList in ```relaxLM``` and ```slider3d``` to allow using semi-landmarks in "thin-air"
 * added helper function ```createMissingList```
 * added function ```points2plane``` for projecting a point/pointcloud onto a plane.
 * ```pcAlign``` with argument ```y``` missing now centers a shape and aligns it by its principal axes.
 * added option ```pcAlign``` in ```procSym``` and ```ProcGPA``` to enable/disable alignment of sample by principal axes
 * added new function mirror to mirror a landmark configuration or a mesh and registering onto the original one.
 * added new functions ```retroDeform3d``` and ```retroDeformMesh``` for removing affine deformation from a 3D-meshes and pointclouds
 * ```deformGrid3d``` now also accepts meshes
 * added function ```classify``` for ```CVA``` and ```groupPCA``` for creating classification tables
 * added new functions ```getTrafo4x4```, ```getTrafoRotaxis, ```computeTransform``` and ```applyTransform```, for computing and applying affine transformations.
 * new function ```pcAlign``` to align meshes and pointclouds by their principal axes
 * added function ```meshPlaneIntersect``` to find intersection points between a mesh and a plane
 * added function ```getFaces``` to get indices of faces that contain specified vertices

####bugfixes and minor changes

 * fixed issue with argument sep in ```typprobClass```
 * added option size in ```deformGrid3d```
 * fixed argument ```tol``` in ```ray2mesh```
 * fixed ```rhotol``` in ```placePatch``` if ```inflate=NULL```
 * fixed NA in colors from meshDist
 * fixed ```rmVertex``` in case no faces remain
 * changed ```relaxLM``` to accept 2D configs
 * replaced workhorse function in ```projRead``` by the faster ```vcgClostKD```
 * made ```plotNormals``` to work with homogenous and non-homogeneous coordinates
 * fixed issue in output of ```CVAdists``` (wrong attribution of p-value tables)
 * renamed ```conv2backf``` to ```invertFaces```
 * renamed ```crossp``` to ```crossProduct```
 * renamed ```tanplan``` to ```tangentPlane```
 * reorient faces if reflections are involved in ```applyTransform```
 * made ```read.lmdta``` more versatile
 * fixed an issue with argument "size" in ```deformGrid3d```
 * set default method to "vcg" in ```meshDist```


 

###Changes in Rvcg since 0.9: 
 
 * pulled new upstream code
 * patched some memory leaks in upstream code
 * added option silent for ```vcgImport, vcgIsolated, vcgQEdecim``` and ```vcgUpdateNormals```
 * added improved exception handling to avoid R session crashes caused by wrong input types.
 * added support for reading face and vertex quality from ply files in ```vcgImport```
 * added option split in ```vcgIsolated``` to split a mesh by connected components and return them as a list
 * ```vcgClean``` now allows to fix uncoherently oriented faces
 * added option tol to specify a search radius in ```vcgClost```
 * added example and docu to ```vcgUniformRemesh```
 * new function ```vcgUniformRemesh``` to remesh based on a voxelized space faces for the closest one with a correct normal orientation.
 * added option ```weightnorm``` in  ```vcgClostKD``` to enable/disable calculation of a weighted normal at the closest point
 * fixes and optimizations in Rkdtree.cpp
 * added option angdev in ```vcgClost/Rkdtree``` to find the closest point with an appropriate normal, if none is found, distance is set to 1e5
 * added method Laplacian (surface preserving) in ```vcgSmooth```
 * added ```vcgStlWrite``` to export mesh3d objects to STL format.
 * added option threshold in ```vcgIsosurface```
 * ```vcgIsosurface``` no longer binarizes the array values
 * fixed texture import in ```vcgImport```
 * fixed missing <#include time.h> in upstream code preventing windows build
  
Happy Holidays and a Happy New Year