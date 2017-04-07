---
layout: post
tags: 
- R 
- Morpho
- Rvcg

date: 2017-04-06 10:25:00 +0200
title: Morpho and Rvcg&#58; New versions on CRAN
---

Both my official R-packages have seen a new release and are now available on CRAN. Here is a list of new features and bug fixes:

## Rvcg

### New features

 * updated vcglib to version 1.0.1
 * added `meshInfo`, `nfaces` and `nverts` to obtain mesh information
 * `vcgStlWrite` and `vcgPlyWrite`: avoid doubled file extension if filename already contains extension
 * NEW: `vcgObjWrite`, `vcgOffWrite` and `vcgWrlWrite`, allowing export of meshes into OBJ, OFF and WRL format
 * `vcgImport`: now supports OFF file format

## Morpho

### New features

 * added `align2procSym` to align new data to existing Procrustes aligned data.
 * `CVA`: added option to specify prior probs
 * `fixLMtps`, `proc.weight`: allow custom weight functions
 * `slider2d`: public version of formerly private Semislide function
 * `procSym`: added`weights` and `centerweights` to control Procrustes registration
 * `predictRelWarps`: added prediction of uniform scores
 * `predictRelWarps`: added support for `alpha=0`
 * `icpmat`: added options for `weights` and `centerweight`
 * `deformGrid3d`: allows to export resulting 3D object as mesh
 * `cSize` now also operates on mesh vertices

### Bugfixes and minor changes

 * `computeTransform`: decreased singularity tolerance for type="tps"
 * `tps2d`: added as alias of `tps3d` to avoid user confusion
 * `equidistantCurve`: some minor improvements and fix for 2D case
 * `CreateL`: fixed return of Lsubk3 if dim=2
 * `read.mpp`:  more generic
 * `applyTransform`: more efficient normal handling for affine transform
 * `write.*` functions: only append file suffix if missing in the filename
