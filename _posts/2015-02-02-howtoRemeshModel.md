---
layout: post
tags: 
- R 
- statismo
- RvtkStatismo

date: 2015-02-02 13:50:00 +0200
title: Howto - remesh a statismo shape model with RvtkStatismo
---
<figure class="right">
    <img rel="zoom" src="/resources/images/decimod1.png" alt="origstate" width="300" >
 <figcaption>Mean shapes of models created from meshes only differing in mesh resolution.</figcaption>
</figure> 

To put some flesh onto my [earlier posts](/2015/01/30/remeshList/), I added an example shape model to RvtkStatismo's example data. And here is some working code to generate shape models with different mesh resolutions from an existing shape model. 
</br>Below, you find the code to 
 
 * restore shapes from a model
 * remesh/decimate the data based on the model mean
 * create new models from these data
 * match the original model onto instances from the new models (and vice versa) to check that they have similar shape variability
 
### Decimate a model

```r
require(RvtkStatismo);require(mesheR)
mod <- statismoLoadModel(system.file("extdata","mandibles.h5",package="RvtkStatismo"))
shapes <- restoreSamples(mod)

## now append the model's mean at the beginning of the list and
## decimate the list based on that mean
## afterwards remove the mean shape
shapesQD <- decimateList(append(list(DrawMean(mod)),shapes),percent = 0.4)[-1]

## create new models
decimMod <- statismoBuildModel(shapesQD)

## now we generate a random sample from the reduced model and fit the original model
## to see that  the sample is well is within the range of the old model
sampleShape <- DrawSample(decimMod)
Bayes <- createBayes(mod,sdmax = rep(5,100),align = F)
match <- gaussMatch(Bayes,sampleShape,iterations = 5,visualize = T,angtol = pi/2)

```
####Matching the original model onto a random instance from the decimated one
<center>
<video width="420" height="315" controls> <source src="/resources/videos/decimod.webm" frameborder="0" allowfullscreen> </video>
</center>


### Remesh a model (assuming we have already loaded the model from above and restored the shapes)

```r
## now append the model's mean at the beginning of the list and
## remesh the list based on that mean
## afterwards remove the mean shape
shapesRemesh <- remeshList(append(list(DrawMean(mod)),shapes),voxelSize = 1)[-1]

## create new models
remeshMod <- statismoBuildModel(shapesRemesh)

## now we generate a random sample from the original model and fit the remeshed model
## to see that the sample is well within the range of the new model
sampleShapeOrig <- DrawSample(mod)
BayesRemesh <- createBayes(remeshMod,sdmax = rep(5,100),align = F)
matchRe <- gaussMatch(BayesRemesh,sampleShapeOrig,iterations = 5,visualize = T,angtol = pi/2)


```

####Matching the remeshed model onto a random instance from the original one
<center>
<video width="420" height="315" controls> <source src="/resources/videos/remesh.webm" frameborder="0" allowfullscreen> </video>
</center>
