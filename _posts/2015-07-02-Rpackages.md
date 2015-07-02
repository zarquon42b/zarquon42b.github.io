---
layout: post
tags: 
- R 
- Rvcg
- Morpho
- RvtkStatismo

date: 2015-07-02 15:45:00 +0200
title: New CRAN-Releases of Morpho and Rvcg
---

Within the last weeks, I finally managed to update my official R-packages Morpho and Rvcg on CRAN.

##The changes are: 
###Changes in Morpho version 2.3.0 (2015-06-18)

####New features

* added function ```line2plane``` to calculate intersection of a line and a plane
* added option ```pcAlign``` in function mirror to improve alignment to original object
* added option ```pcAlign``` in ```relWarps``` and ```procSym``` to allow alignment to first specimen rather than PC-axes.
* Gregory Jefferis added unit testing setup infrastructure
* added new functions ```getPLSfromScores```, ```getPLSscores```, ```predictPLSfromScores```,``` predictPLSfromData``` and ```plsCoVar``` for prediction and handling results from 2-Block PLS regression.
* made ```relaxLM``` an S3 function and added methods for ```mesh3d``` to relax two meshes with corresponding vertices. Added ```use.lm``` to specify subset of coordinates for alignment if ```bending=FALSE```
* new option '```as.factor```' in ```name2factor```
* deprecated ```warp.mesh``` (use ```tps3d``` now for meshes and matrices)
* ```meshDist``` now allows custom colorramps
* added option ```wireframe``` in ```deformGrid2d```
* added support for registered meshes in ```computeTransform```
* added selection of transform type in ```icpmat```
* added option ```use.lm``` to ```slider3d``` to specify subset for alignment if ```bending=FALSE```
* added ```getMeaningfulPCs``` to determine meaningful Principal Components (see my post [here](/2015/04/15/meaningPCs/))
* made optimization in ```pcAlign``` and ```mirror``` run in parallel (not supported on Windows OS).

####bugfixes and minor changes

* fixed normal handling in``` mergeMeshes```
* fixed coefficient scaling in ```RegScore```
* added update of normals in ```meshDist```
* removed unnecessary function ```meanMat``` and replaced it with generic ```colMeans```
* fixed calculation of loadings in ```pls2B```
* set ```lambda``` (regularization) in all tps related functions to 1e-8 to avoid gross distortions in some cases
* fixed typo in ```pcAlign``` leading to misbehavior if iterations < 1



###Changes in Rvcg version 0.12.2 (2015-06-28)
####new features
 * updated vcglib source code to Revision: 5521
 * added option ```as.int``` to ```vcgIsosurface```
 * added option ```iterate``` in ```vcgClean```
 
####bug fixes
 * removed wrong error call in ```vcgKDtree```
 * silenced all output in ```vcgQEdecim``` if ```silent=TRUE```
