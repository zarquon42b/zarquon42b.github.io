---
layout: post
tags: 
- R 
- RvtkStatismo
- Statismo
- mesheR

date: 2016-03-04 14:15:00 +0200
title: Update Displacement fields the 4th&#58; B-splines 
---

As RvtkStatismo is already sporting a B-spline kernel for Gaussian-Process models (a modified version contained in the [statismo command line tools](https://github.com/statismo/statismo/blob/master/modules/ITK/cli/utils/statismo-build-gp-model-kernels.h)), I decided to adapt that code and make it available in mesheR to allow displacment field smoothing using a B-spline kernel. Below, we modify the example from the documentation of ```gaussMatch``` to use a B-spline interpolation to smooth the displacement field. The downside, however, is the much slower performance (depending on the selected support value). Additionally, the default is to decrease the *support* value with each iteration, allowing less and less "wobbling". For the i-th generation: \\( sigma = sigma*f^{-(i-1)}\\). Thus, the values for ```f```, and accordingly```iterations```, need to be selected in a sensible fashion.

## Example
 
Below we see an example using a B-spline kernel with a starting  value of ```sigma = 20``` and let it decrease uniformly with each iteration using the default settings. The result is a nice and smooth deformation of an (already affinely registered) normal nose to a harlekin nose (<a href="#Vid1">Video 1</a>).


```r
require(Morpho)
data(nose)##load data
##warp a mesh onto another landmark configuration:
 warpnose.long <- tps3d(shortnose.mesh,shortnose.lm,longnose.lm)
### result won't be too good as the surfaces do stronly differ.
## we start with an affine transformation initiated by landmarks
affine <- list(iterations=20,subsample=100,rhotol=pi/2,uprange=0.9)
	 
 matchBSpline <- gaussMatch(shortnose.mesh,warpnose.long,
	 lm1=shortnose.lm,
	 lm2=longnose.lm,gamma=2,iterations=20,nh=300,
	 angtol=pi/2,affine=affine,sigma=20,displacementsmooth="b")
			 
```
<a id="Vid1"></a>
<center>
<video width="420" height="315" controls> <source src="/resources/videos/bsplinenose.webm" frameborder="0" allowfullscreen> </video>
</center>





