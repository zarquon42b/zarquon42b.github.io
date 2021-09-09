---
layout: post
tags: 
- R 
- Morpho
- Rvcg

date: 2021-09-09 08:25:00 +0200
title: New Versions of Morpho and Rvcg on CRAN
---

Hi everyone, after quite some while without official updates, I am happy to anounce new versions of [Morpho](https://cran.r-project.org/package=Morpho) and [Rvcg](https://cran.r-project.org/package=Rvcg) to CRAN that now have been built for all platforms. 


Here is the complete list of changes in the latest Morpho (2.9) and Rvcg (0.20.2) releases


## Morpho 0.28

### New features and bug fixes


* `deformGrid2d`: added option `lty`
* `read.slicerjson`: add option to specify na values.
* `rotonto`: return correctly dimensioned matrices in NA cases.
* NEW: `getPointAlongOutline` and `resampleCurve`
* `meshDist`: added option titleplot for customizing heatmap axis.
* `procSym`: Add numbering to PC-Variance table.
* `groupPCA`: remove misleading combinedVar table from output
* `mirror`: added option to mirror on plane, using it as a wrapper for mirror2plane.
* fixed arguments in deprecated function `showPC`
* deprecated: `showPC`
* `getSides`: set default values for `pcAlign` and `icpiter`
* NEW: `getSides` to find bilateral landmarks.
* NEW: `updateIndices`: update a vector of indices after removel of some of the indexed items
* NEW: `restoreFromPCA`: retrieve data back from a pca space.
* `slider3d`: new option `smoothnormals` to obtain tangent plains from smoothed normals
* `read.slicer.json`: added option `lps2ras` to automatically convert lps 2 ras space on import
* `read.fcsv`: add option `lps2ras` to allow an automatic conversion to RAS space if coordinates are recorded in LPS (as of Slicer > 4.11).


## Rvcg 0.20.2

### New features and bug fixes


* NEW: `vcgIsotropicRemeshing`: remesh to obtain uniform edge lengths
* NEW: `vcgGeodist` `vcgGeodistPath`: get geodesic paths on meshes
* NEW: `vcgVertxNeighbours`: find neighbourhood of vertices
* NEW: `vcgFaceNormals`: compute per face normals of a mesh
