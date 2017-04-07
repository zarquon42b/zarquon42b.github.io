---
layout: post
tags: 
- R 
- Morpho
- Rvcg

date: 2017-04-7 09:25:00 +0200
title: Psychedelic skulls from an SSM
---

A lot of people think statistics is utterly boring. However, you can also do a lot of fun stuff with it. While I was working on creating a statistical shape model of the human skull, I felt somewhat creative and generated a [movie](#movie) of warping skulls with a shifting heatmap coloration based on random samples and a gaussian smoother. Here is the code (we assume, there is already an existing SSM called *"skullmod"*):

### Sample from the model

```r
require(RvtkStatismo)
skullmod <- statismoLoadModel("skullmod")
## sample 20 instances from the model
mysample <- lapply(1:20,function(x) DrawSample(skullmod))
```

### Create a coloring function

The function below samples points from the the surfaces and then creates a weighted distance for each vertex.

```r
## the weighting function
gaussWeight <- function(r,sigma) {
    sigma <- 2*sigma^2
    return(exp(-r^2/ sigma))
}

## the function that colorizes the meshes with heatmap based
## on the weighted distances to the sampled surface points
mycolorfun <- function(x,random=100) {
    samplenum <- sample(random,size = 1)
    mymeansamp <- vcgSample(x,SampleNum = samplenum)
    inds <- vcgKDtree(mymeansamp,x,k=nrow(mymeansamp))
    test <- gaussWeight(inds$distance,8)
    testsum <- rowSums(test)
    mD <- meshDist(x,distvec = testsum,plot = FALSE)
    return(mD$colMesh)
}

```

### Use the function to colorize our sampled model instances and interpolate between those to create an image series

```r
mysampleCol <- lapply(mysample,mycolorfun)
## we append the first instance at the end to create a loopable image series
mysampleColRLoop <- append(mysampleCol,mysampleCol[1])
require(mesheR)
warpmovieMulti(mysampleColLoop,n=15,folder = "colmovie",movie="skulls")

```

### And here is the movie:
<a id="movie"></a>
<center>
<video width="420" height="315" controls> <source src="/resources/videos/colorSkull.webm" frameborder="0" allowfullscreen> </video>
</center>
