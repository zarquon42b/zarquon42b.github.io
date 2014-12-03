---
layout: post
tags: 
- R 
- RvtkStatismo 
- statismo

date: 2014-11-19 10:59:00 +0200
title: RvtkStatismo, mesheR&#58; Create an endocast using a GP model of a sphere
---

Here is an example, how to regularize a sphere's deformation to create a nice endocast.

Given a skull and a sphere (in my case 10242 vertices and 20480 faces) placed inside the cranial vault, the commands are:

First we do a coarse matching:


```r
##create a deformation model of a sphere
mod <- statismoModelFromRepresenter(sphere2,kernel = list(c(100,70),c(50,50),c(20,5)),ncomp = 100,isoScale = 0.3)
affine <- similarity <- list(iterations=10,rhotol=pi/2)

Bayes <- createBayes(mod,sdmax = rep(5,100),wt=5,shrinkfun = function(x,i){ x <- x*0.9^i},align = F)

test <- gaussMatch(Bayes,skull,toldist = 200,visualize = T,oneway = T,angtol=pi/2,AmbergK=10,AmbergLambda = seq(from=0.4,to=1.2,length.out = 170),iterations = 170,sigma = 90,smooth=1,smoothtype = "HC",nh=100) 

```
<center>
<video width="420" height="315" controls> <source src="/resources/videos/endo.webm" frameborder="0" allowfullscreen> </video>
</center>

</br>
For the fine matching, we remesh the result ( I used the remeshing VCG filter in meshlab and saved it as *testVCG.ply*) to create a relatively uniform version of the fitted endocast.


```r
secrun <- vcgImport("./testVCG.ply")

#create a new model based on the fine endocast
mod2 <- statismoModelFromRepresenter(secrun,kernel = list(c(50,10),c(20,5)),ncomp = 100)

Bayes2 <- createBayes(mod2,sdmax = rep(5,100),wt=2,shrinkfun = function(x,i){ x <- x*0.9^i},align = F)
test2 <- gaussMatch(Bayes2,skull,toldist = 200,visualize = T,oneway = T,angtol=pi/2,AmbergK=10,AmbergLambda = seq(from=0.4,to=1.2,length.out = 20),iterations = 20,sigma = 20,nh=100)
```

And here is the distance map to the inner vault (the error occurs only where there are wholes and cuts in the skull)

<figure>
    <img rel="zoom" src="/resources/images/endodist.png" alt="endodist" width="400">
  <figcaption><b>Fig.1:</b> Distance between fitted endocast and cranial vault</figcaption>
</figure>

