---
layout: post
tags: 
- R 
- RvtkStatismo
- Statismo


date: 2016-02-08 11:45:00 +0200
title: Perform boolean operations on meshes in RvtkStatismo
---

Due to the wrappers in RvtkStatismo for meshes from R to vtkPolyData, extending the functionality of this package is quite easy. Recently, I added the functionality to perform boolean operations on triangular meshes using the new function ```vtkBooleanOp```.
It creates Unions, Intersections and Differences from two triangular meshes stored in R as objects of class ```mesh3d```. 
For creating intersection planes based on an object's bounding box, the function ```BBoxSlices```was added to *[mesheR](https://github.com/zarquon42b/mesheR)*. 

As usual, here is some example code, ready to be run in an R:


### Example 1: create the union of two spheres (<a href="#Fig1">Figure 1</a>)

```r
require(Rvcg);require(Morpho);require(rgl)
require(RvtkStatismo)
## create two unit spheres
sphere1 <- vcgSphere()
sphere2 <- vcgSphere()
## translate sphere2 by half its radius
sphere2 <- translate3d(sphere2,0,0,0.5)
union <- vtkBooleanOp(sphere1,sphere2)

## create normals for smooth rendering
union <- vcgUpdateNormals(union)
shade3d(union,alpha=0.5,col=2)
wire3d(union)

```


<a id="Fig1"></a>
<figure class="center">
    <img rel="zoom" src="/resources/images/union.png" alt="initial state" height="300" >    
    <figcaption>Fig. 1: Union of two spheres</figcaption>

</figure> 

### Example 2: crop a mesh by a bounding box slice (<a href="#Fig2">Figure 2</a> and <a href="#Fig3">Figure 3</a>)


```r
require(Rvcg)
require(rgl)
require(mesheR)
sphere <- vcgSphere()
## get corners of the bounding box
bbox <- getMeshBox(sphere,pca=FALSE)
## get a triangular mesh consisting of 3 triangles cutting a slice from the y-z plane
slice <- BBoxSlices(bbox,axis = 1,percent = 0.7)
myplot <- plot3d(sphere,col="white")
shade3d(slice,col=2,alpha=0.5)

## now use the slice to get the difference 

cuthead <- vtkBooleanOp(sphere,slice,type=2)
## create normals for smooth rendering
cuthead <- vcgUpdateNormals(cuthead)
shade3d(cuthead,col="white")
```


<a id="Fig2"></a>
<figure class="left">
    <img rel="zoom" src="/resources/images/differencePlane.png" alt="initial state" height="300" > 
    <figcaption>Fig 2: The sphere and an intersection plane</figcaption>
</figure> 
<a id="Fig3"></a>
<figure class="float">
    <img rel="zoom" src="/resources/images/differenceSphere.png" alt="initial state" height="300" > 
    <figcaption>Fig 3: The sphere cut off by the intersection plane</figcaption>
</figure> 
