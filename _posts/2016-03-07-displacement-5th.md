---
layout: post
tags: 
- R 
- RvtkStatismo
- Statismo
- mesheR

date: 2016-03-07 14:15:00 +0200
title: More interpolations, fast subsampling and tweaking
---

## General stuff
As can be seen in my last four posts, I started playing with displacement fields and interpolation. While the smoothers used so far provided fast and reasonable approximations, I wondered whether this could be improved/complemented by additional methods and starting digging into splines again. The nice thing about learning and the subsequent code revision is that you pick up quite some bug fixes and speed improvements along the way. For example: I realized that there was substantial tweaking potential in my Thin-Plate Spline function ```tps3d``` in *[Morpho](https://github.com/zarquon42b/Morpho)*, which now is much faster: Using 6000 control points, the deformation of a mesh with ~120000 vertices takes 16secs on my workstation (instead of ~90 secs before). 

## Fast K-means clustering for 2D and 3D data
My idea was to subsample the displacement fields and calculate a TPS interpolation based on this subsampled data. Here, the next obstacle appeared: I could not find a fast way of getting nicely distributed sub-samples in R. R's built in K-means clustering is too slow for large point clouds and large \\(k\\). So using the ```vcgKDtree``` function from *[Rvcg](https://github.com/zarquon42b/Morpho)*, I managed to implement a fast and parallel (thanks to OpenMP) K-means clustering algorithm that not only returns the K-means centers, but those points from the displacement field closest to these centers. Thus, the displacement field (or any point set) can be subsampled fast and leading to reasonable results (<a href="#Fig1">Figure 1</a> and <a href="#Fig2">Figure 2</a> show 1000 points sampled from a mesh).

```r
require(Rvcg);require(Morpho)
data(humface)
clust <- fastKmeans(humface,k=1000,iter.max=100)
## plot the cluster centers
wire3d(humface)
spheres3d(clust$centers)
## now look at the vertices closest to the centers
spheres3d(vert2points(humface)[clust$selected,],col=2)
			 
```

<a id="Fig1"></a>
<figure class="left">
    <img rel="zoom" src="/resources/images/fastkmeans_center.png" alt="example 1" height="200" >    
    <figcaption>Fig. 1: Points sampled on the surface. Black spheres: Cluster centers</figcaption>

</figure> 

<a id="Fig2"></a>
<figure class="float">
    <img rel="zoom" src="/resources/images/fastkmeans_closest.png" alt="example 1" height="200" >    
    <figcaption>Fig. 2: Points sampled on the surface. Red spheres: Vertices closest to each center</figcaption>

</figure> 

## Synthesis

To throw all together, we can now do a fast subsampling of the displacement filed and compute a smooth TPS deformation (or smooth an existing one. In the next example, we will reuse the example from [before](../../01/displacementfieldsupdate/), to interpolate a low resolution field. This time the resulting deformation leads instantaneously to a smooth surface (<a href="#Fig3">Figure 3</a>). And additionally, we interpolate the highres field now to a cubic grid and add it to the plot (<a href="#Fig4">Figure 4</a>).

```r

highresdisp <- interpolateDisplacementField(dispfield,highres,type="TPS",subsample=4000)
highres_deformed <- applyDisplacementField(highresdisp,highres)
shade3d(highres_deformed,col="white")

## create a nice deformation grid
require(sp)
grid <- spsample(SpatialPoints(vert2points(highres)),100000,type="regular")
grid <- grid@coords
gridfield <- interpolateDisplacementField(highresdisp,grid,type = "TPS",subsample=4000)
```



<a id="Fig3"></a>
<figure class="left">
    <img rel="zoom" src="/resources/images/tps_deform.png" alt="example 1" height="250" >    
    <figcaption>Fig. 3: Displacement field transform based on TPS-interpolaton.</figcaption>
</figure> 

<a id="Fig4"></a>
<figure class="float">
    <img rel="zoom" src="/resources/images/tps_deform_grid.png" alt="example 1" height="250" >    
    <figcaption>Fig. 4: Colorful displacement grid.</figcaption>

</figure> 
