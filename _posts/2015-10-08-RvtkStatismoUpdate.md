---
layout: post
tags: 
- R 
- RvtkStatismo


date: 2015-10-08 15:45:00 +0200
title: RvtkStatismo&#58; Updates
---

Newly motivated by the nice [SHAPE symposium](http://www.shapesymposium.org/) in Delemont, I started showing some love to RvtkStatismo: ```statismoConstrainModel``` now accepts per coordinate noise values (only spherical at the moment). Additionally, there is a new function called ```vtkTriangulate``` that creates an isosurface (as ```mesh3d```)from a (binary) image file and ```vtkMeshWrite``` can optionally write ASCII vtk files. All this is accompanied by some bugfixes I found along the way.

Here are the effects of per-landmark noise and global noise values:


###Constrain a model

```r
require(RvtkStatismo)
require(Rvcg)
require(mesheR)
require(rgl)
data(humface)
# Create a model
hummodel <- statismoModelFromRepresenter(humface,kernel=list(c(80,50),c(20,40)))
noise <- (0:6)*10 #create an increasing amount of noise
GPmodConst <- statismoConstrainModel(hummodel,humface.lm,humface.lm,ptValueNoise = noise)
##now look at the sampled landmark variability (extracted from sampled surfaces via mesheR::transferPoints)
for(i in 1:10) {
    tmpsamp <- DrawSample(GPmodConst)
    spheres3d(transferPoints(humface.lm,humface,tmpsamp),col=2,radius=2)
    }
    
```

In <a href="#Fig1"> Figure 1 and Figure 2</a> we can see how the variability of sampled surfaces (shown only at the landmark location is directly affected by the choice we make at each landmark (especially at the right eye were noise is set to zero).

<a id="Fig1"></a>

<figure class="left">
    <img rel="zoom" src="/resources/images/samplefront.png" alt="frontalview" height="300" >
    

</figure> 
<figure >
<img rel="zoom" src="/resources/images/samplelat.png" alt="lateralview" height="300" >  
</figure>   
 <figcaption>Fig. 1: noise specific variability of landmarks in posterior model</figcaption>

</br>