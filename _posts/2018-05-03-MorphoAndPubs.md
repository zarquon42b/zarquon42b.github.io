---
layout: post
tags: 
- R 
- Morpho
- Rvcg

date: 2018-05-08 08:25:00 +0200
title: Update of Morpho and related publications
---

It has been some time since my last post, so here a quick update. Last month, I have issued a new release of Morpho (2.6) on CRAN that contains a lot of new features. As it happens, we managed to get two new papers published that directly relate to some ofthose new features. 

The first paper ist on extracting parts of a triangular mesh based on its visibility from a set of view points.

The second paper deals with retrodeforming fossil specimens with an emphasis on symmetrically placed semi-landmarks.


1. <a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/ajpa.23493"><i>Profico A, Schlager S, Valoriani V, Buzi C, Melchionna M, Veneziano A, Raia P,
Moggi-Cecchi J, Manzi G. 2018. Reproducing the internal and external anatomy of fossil
bones: Two new automatic digital tools. American Journal of Physical Anthropology.</i></a>

2. <a href="http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0194073"><i>Schlager S, Profico A, Di Vincenzo F, Manzi G. 2018. Retrodeformation of fossil specimens
based on 3D bilateral semi-landmarks: Implementation in the R package "Morpho". PLOS
ONE 13(3):1–19.</i></a>



Here is the complete list of changes in the latest Morpho (2.6) release


## Morpho

### New features
 
 * `virtualMeshScan`, `getOuterViewpoints`: perform a virtual rescan of a mesh using defined POVs.
 *  `deformGrid3d`: fixed indices starting with 0 for slices, add `gridcol` and `gridwidth` and added options to select subsets of slices.
 *  `deformGrid2d`: added options `cex1`,`cex2`,`gridcol` 
 *  `fixLMmirror`: now allowing heavy abuse with loads of missing data and improved error handling
 *  `plotNormals`: allow for per vertex lenght vector and changed long=>length and deprecated old option
 *  `checkLM`: added possibility to view backwards
 *  `slider3d`: made function work in parallel on all OS
 *  `pls2B`: added CV (+ options)
 *  added `plsCoVarCommonShape`: Compute the shape changes along the common axis of deformations
 *  added `getPLSCommonShape`: Obtain linear combinations associated with the common shape change in
each latent dimension of a `pls2B`

### Bugfixes and minor changes
 
 *  `line2plane`: fixed deprectated array multiplication warning
 *  changed `Matrix::cBind` to `base::cbind`
 *  Depend: > R 3.2.0
 *  `GetPhi` (privat function in retrodeform3d): set h to average between landmark distance (not the squared distance)
 *  `CVA`: add rownames and colnames to scores and CVs
 
