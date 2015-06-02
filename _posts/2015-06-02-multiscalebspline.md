---
layout: post
tags: 
- R 
- statismo
- RvtkStatismo

date: 2015-06-02 09:45:00 +0200
title: RvtkStatismo&#58; Multiscale B-Spline kernel
---

The upcoming release of [statismo](https://github.com/statismo/statismo) (0.11) is sporting some fancy new command-line tools for model generation and fitting, including the option to use a multiscale B-spline kernel for creating/improving a Gaussian Process model. I now implemented this in [RvtkStatismo](https://github.com/zarquon42b/RvtkStatismo) for generating/extending shape models, using an adapted version of the command-line tool's code.

```statismoModelFromRepresenter``` and ```statismoGPmodel``` now allow the combination of multiscale B-Spline and Gaussian kernels. At the moment the interface is as follows: 

We call ```statismoModelFromRepresenter(mymesh,kernels=list(...))```: if the first entry in kernels is a vector of length three, it will be interpreted as requesting a Multiscale B-Spline kernel with the vector's first entry being the baselevel the second the scale and the third entry the number of levels to be generated. The interface for Gaussian kernels is the same as before.

Here the example:
First get RvtkStatismo from the specific branch

```r
require(devtools)
install_github("zarquon42b/RvtkStatismo",ref="multiscale-bspline")
```


```r
require(RvtkStatismo)
require(rgl)

ref <- read.vtk("VSD001_femur.vtk")
## we create a model using a a base-level of 150, as scale of 150 and 10 levels
mymod <- statismoModelFromRepresenter(ref,kernel=list(c(150,150,10)),ncomp = 100)

##generate and render some random samples (Fig. 1)
for(i in 1:10) wire3d(DrawSample(mymod),col=i)

```


<a id="Fig1"></a>
<figure class="center">
    <img rel="zoom" src="/resources/images/multiscaleFemur.png" alt="figure1" width="450" >
 <figcaption>Fig. 1: Random instances sampled from a model based on a multiscale B-Spline kernel</figcaption>
</figure> 