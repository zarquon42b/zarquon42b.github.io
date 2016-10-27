---
layout: post
tags: 
- R 
- RvtkStatismo
- Statismo


date: 2016-10-27 10:45:00 +0200
title: Compute Geodesic Path and Distance in RvtkStatismo
---

The development branch of RvtkStatismo now contains an implementation of `vtkDijkstraGraphGeodesicPath`. The R-functions `vtkGeodesicPath` and `vtkGeodesicPathForPointPair` allow to compute the (pseudo-) geodesic path by tracking the shortest route along connected vertices - this means the higher the mesh resolution, the smoother the resulting path will be. `vtkGeodesicPath` needs a mesh and two vertex indices (defining start and end positions of the path) as input. `vtkGeodesicPathForPointPair` requires a mesh and two vectors containing points on the surface. For the latter the search will start and and at the vertices closest to those coordinates. 


### Example 1: `vtkGeodesicPath` (<a href="#Fig1">Figure 1</a>)


```r
 require(Rvcg)
 data(humface)
 gp <- vtkGeodesicPath(humface,1,1000)
 gp$distance
 ## The distance is 98.36738 mm
 
 ## render it
 require(rgl);require(Morpho)
 points3d(vert2points(humface)[gp$index,])
 lines3d(vert2points(humface)[gp$index,],col="blue",lwd=4)
 spheres3d(vert2points(humface)[c(1,1000),],col=2)
 shade3d(humface,col="white")
```

### Example 2: `vtkGeodesicPathForPointPair` (<a href="#Fig2">Figure 2</a>)


```r
 require(Rvcg)
 data(humface)
 gp <- vtkGeodesicPathForPointPair(humface,humface.lm[1,],humface.lm[2,])
 gp$distance
 ## The distance is 30.98827 mm
 
 ## render it
 require(rgl);require(Morpho)
 points3d(vert2points(humface)[gp$index,])
 lines3d(vert2points(humface)[gp$index,],col="blue",lwd=4)
 spheres3d(humface.lm[1:2,],col=2)
 shade3d(humface,col="white")
```

The paths are quite crooked because of the mesh's low resolution. To obtain a smoother path, we can e.g. apply a triangle subdivision first  (<a href="#Fig3">Figure 3</a>):


### Example 3: `vtkGeodesicPathForPointPair` on a high resolution mesh (<a href="#Fig2">Figure 3</a>)


```r
 humface <- vcgSubdivide(humface,threshold = 0.5,looptype = "cont",iterations=5)
 gp <- vtkGeodesicPathForPointPair(humface,humface.lm[1,],humface.lm[2,])
  
 ## render it
 require(rgl);require(Morpho)
 points3d(vert2points(humface)[gp$index,])
 lines3d(vert2points(humface)[gp$index,],col="blue",lwd=4)
 spheres3d(humface.lm[1:2,],col=2)
 shade3d(humface,col="white")
```

<a id="Fig1"></a>
<figure class="left">
    <img rel="zoom" src="/resources/images/vtkgeopath.png" alt="initial state" height="300" > 
    <figcaption>Fig 1: Geodesic Path between first and 1000th vertex</figcaption>
</figure> 
<a id="Fig2"></a>
<figure class="float">
    <img rel="zoom" src="/resources/images/vtkgeopathpair.png" alt="initial state" height="300" > 
    <figcaption>Fig 2: Geodesic Path between landmarks (endo- and ectocanthion)</figcaption>
</figure> 
<a id="Fig3"></a>
<figure class="float">
    <img rel="zoom" src="/resources/images/vtkgeopathsmooth.png" alt="initial state" height="300" > 
    <figcaption>Fig 3: Geodesic Path between landmarks (endo- and ectocanthion) on a refined surface</figcaption>
</figure>
