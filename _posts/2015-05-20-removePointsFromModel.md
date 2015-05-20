---
layout: post
tags: 
- R 
- statismo
- RvtkStatismo

date: 2015-05-20 13:50:00 +0200
title: Remove points from statismo shape model
---

I added a new function, called ```removePointsFromModel``` to my RvtkStatismo package to selectively remove coordinates from a statismo shape model. 

Here is the example from the documentation:


```r
require(RvtkStatismo)
require(Rvcg)
require(rgl)
data(humface)
hummodel <- statismoModelFromRepresenter(humface,kernel=list(c(50,50)))
hummodel0 <- removePointsFromModel(hummodel,1:1000)
shade3d(DrawSample(hummodel0),col=3)
```

The last command renders a random sample from the new model (Fig. 1) that now has some holes in it.

<figure class="center">
    <img rel="zoom" src="/resources/images/removePointsSample.png" alt="origstate" width="450" >
 <figcaption>Fig. 1: Random sample from the new model , missing the first 1000 vertices</figcaption>
</figure> 