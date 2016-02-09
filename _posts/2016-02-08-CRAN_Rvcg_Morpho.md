---
layout: post
tags: 
- R 
- RvtkStatismo
- Statismo


date: 2016-02-08 11:45:00 +0200
title: New Releases of Rvcg and Morpho&#58; performance improvements and bugfixes
---

Somewhat delayed here the announcement of new CRAN releases of **[Rvcg](https://cran.r-project.org/package=Rvcg)** and **[Morpho](https://cran.r-project.org/package=Morpho)**: 
The most significant changes are the optional usage of OpenMP for closest point search/KD-tree search in Rvcg (functions ```vcgClostKD``` and ```vcgKDtree``` now have an option ```threads``` to specify number of threads to use). This is significantly boosting the registration functions ```gaussMatch```,```modelFitting``` and  ```AmbergRegister``` from **[mesheR](https://github.com/zarquon42b/mesheR)** where this function is called several times in each iteration.

### Here are all changes in Rvcg:

 * updated vcglib source code to Revision: 5542
 * added functions to create basic meshes (spheres, polyhedrons)
 * enabled OpenMP support to run closest point search in parallel (vcgKDtree and vcgClostKD)
 * added options IJK2RAS and direction in vcgIsosurface
 * added new option writeNormals in vcgPlyWrite
 * added option facenormals in vcgClost* functions
 * added functions to check if the normals of a mesh are oriented outward
 * added additional low-level options in vcgKDtree

### And here the changes in Morpho:

 * meshPlaneIntersect now also supports normals (as cutSpace)
 * added default method for applyTransform for 2D and 3D vectors
 * removed bePCs with zero variance from output in relWarps
 * improved error handling in placePatch
 * set square=FALSE in qqmat
 * added message if CSinit = F and orp = T, that orp is disabled
 * fixed applyTransform for type="tps" and inverse = TRUE
 * added testthat test for relWarps
 * tweaked relWarps to work with large amounts of coordinates
 * fixed wrong bracket position in ProcGPA leading to only a single iteration
 * CVA: fixed calculation of posterior probs if cv=F
 * fixed linewidth in CVA example to stop check complaints
 * set p.adjust.method="none"
 * only return significant scores in relWarps
 * named output of plsCoVar
