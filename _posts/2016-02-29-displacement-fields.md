---
layout: post
tags: 
- R 
- RvtkStatismo
- Statismo
- mesheR

date: 2016-02-29 14:45:00 +0200
title: Displacement fields in mesheR
---

Inspired by the awesome Shape Modelling [MOOC](https://www.futurelearn.com/courses/statistical-shape-modelling/), organized by the University of Basel, I decided to add interpolation of displacement fields in mesheR as well. For smoothing, I decided for a Gaussian smoother based on the displacement vectors of the k-closest domain points (a lot of useful stuff was already there from ```gaussMatch```)

The functions added are:

* ```createDisplacementField``` -- creates a discrete displacement field
* ```interpolateDisplacementField``` -- interpolate discrete displacement field at any point(s)
* ```applyDisplacementField``` -- apply (and optionally interpolate) a deformation defined by a displacement field to coordinates/mesh
* ```plotDisplacementField``` -- visualize a displacement field

Here is some code to play with. Happy 29th February.


## Example 1

We are going create a displacement field from a GP-model instance and its mean and apply it to a second random instance.


```r
require(Rvcg);require(mesheR);require(rgl)
require(RvtkStatismo)
data(humface)

## create a GP model of a human face

mymod <- statismoModelFromRepresenter(humface,kernel=list(c(50,30)))

## sample two instances from the model

sample1 <- DrawSample(mymod)
sample2 <- DrawSample(mymod)
dispfield <- createDisplacementField(DrawMean(mymod),sample1)
dispfieldNew <- interpolateDisplacementField(dispfield,sample2)
sample2displaced <- applyDisplacementField(dispfieldNew,sample2)

##visualize the displacement field

plotDisplacementField(dispfieldNew,lwd=2)
wire3d(sample2)

```

<a id="Fig1"></a>
<figure class="center">
    <img rel="zoom" src="/resources/images/dispfield0.png" alt="example 1" height="300" >    
    <figcaption>Fig. 1: Displacement field in example 1</figcaption>

</figure> 


## Example 2

Here we use a discrete displacement field generated from a coarse mesh (*Example 1*) and apply the resulting deformation to a high resolution version of the reference mesh (you will need the latest master snapshot of Rvcg to create a high resolution mesh). The result and the differences to the target mesh that was used to calculate the discrete displacment field can be seen in <a href="#Fig2">Figure 2</a>. 

```r

## create a finer mesh of the mean using subdivison algorithm

highres <- vcgSubdivide(DrawMean(mymod),type="loop",threshold=1.5)
dispfieldHighres <- interpolateDisplacementField(dispfield,highres)
highresDisplaced <- applyDisplacementField(dispfieldHighres,highres)

## visualize the result, also displaying the errors between the
## deformed highres mean and the target surface

Morpho::meshDist(highresDisplaced,sample1,tol=0.1)
```
<a id="Fig2"></a>
<figure class="center">
    <img rel="zoom" src="/resources/images/dispfield_fine.png" alt="initial state" height="300" > 
    <figcaption>Fig 2: Interpolated displacement field to deform a high-resolution mesh</figcaption>
</figure> 

