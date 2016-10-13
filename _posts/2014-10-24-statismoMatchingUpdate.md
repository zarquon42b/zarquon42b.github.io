---
layout: post
tags: 
- R 
- RvtkStatismo 
- registration
- mesheR

date: 2014-10-24 13:59:00 +0200
title: UPDATE&#58; statismo models for elastic mesh registration in R
---

## UPDATE: 10/2016
*As the kernel interface has changed in July 2016 (read more [here](/2016/03/17/RvtkStatismo_new_kernels/)), I added the updated commands in the code section.*


I changed/fixed some stuff in the interaction between RvtkStatismo and my matching routines (```gaussMatch``` and ```AmbergRegister```) which are:

* class ```BayesDeform``` now has the additional parameter ```wt``` that allows to control the weight of the model's proposition against the weight by the (regularized) closest points/displacement field
* this object is now replacing the reference mesh instead of being an additional argument in the registration functions
* ```createBayes``` has an additional argument ```shrinkfun``` that allows to specify a function controlling the model's weight for the i-th iteration (see below for details)

These improvements allow for a controlled decrease in the model's influence on the deformation the closer we get to the target shape.

In case someone wants to rerun the examples from my [earlier post](http://zarquon42b.github.io/2014/08/14/statismoMatching/), here are the updated parameters/commands:



### CAVEAT:
<font color="#FF0000"><b>You need to install latest version from master branch of mesheR, RvtkStatismo and Morpho !!</b>
</font>

```r
require(RvtkStatismo)
require(Rvcg)
require(Morpho)
require(mesheR)
require(rgl)
data(humface)
data(dummyhead)


### first create a model based on the reference


## mymod <- statismoModelFromRepresenter(dummyhead.mesh,kernel = list(c(50,50)),ncomp = 100) ## Old Interface
## new kernel interface as of 07/2016
GK <- GaussianKernel(50,50)
mymod <- statismoModelFromRepresenter(dummyhead.mesh,kernel=GK,ncomp = 100)

##now create an object of class BayesDeform

Bayes <- createBayes(mymod,sdmax=rep(4,30),ptValueNoise = 2,wt=1.5,shrinkfun = function(x,i){ x <- x*0.9^i})# we start off with a rather strong weight for the model with each iteration it will be 90% of the previous weight
## setup parameters for AmbergRegister
params <- list(iterations=30)
params <- append(params, list(
        # then let it increase from 0.2 to 0.6
        lambda=seq(from = 0.2,to=0.6,length.out = params$iterations),
        # treat \code{k} similar as \code{lambda}
        k=seq(from = 1,to=params$iterations,by=1),
        useiter=FALSE # iteratively deform dummyhead onto humface
        ))

## setup parameters for some additional rigid wiggling (ICP)

rigid <- list(iterations=60,subsample=200,rhotol=pi/2,uprange=0.3)#here we specify an overlap between reference and target of 30% 

## run the matching
map <- AmbergRegister(Bayes, humface, lm1=dummyhead.lm, lm2=humface.lm, iterations=params$iterations,k=params$k, lambda=params$lambda, useiter=params$useiter,rigid=rigid,visualize = T)

```
Here is the output as movie:
<center>
<video width="420" height="315" controls> <source src="/resources/videos/face1.webm" frameborder="0" allowfullscreen> </video>
</center>

And here is the updated example matching Marcel's Femur surfaces:

```r

require(RvtkStatismo)
require(Rvcg)
require(Morpho)
require(mesheR)
require(rgl)

download.file(url="https://github.com/marcelluethi/statismo-shaperegistration/raw/master/data/VSD001_femur.vtk","./VSD001_femur.vtk",method = "w")
download.file(url="https://github.com/marcelluethi/statismo-shaperegistration/raw/master/data/VSD002_femur.vtk","./VSD002_femur.vtk",method = "w")
download.file(url="https://github.com/marcelluethi/statismo-shaperegistration/raw/master/data/VSD001-lm.csv","./VSD001-lm.csv",method = "w")
download.file(url="https://github.com/marcelluethi/statismo-shaperegistration/raw/master/data/VSD002-lm.csv","./VSD002-lm.csv",method = "w")

ref <- read.vtk("VSD001_femur.vtk")
tar <- read.vtk("VSD002_femur.vtk")

ref.lm <- as.matrix(read.csv("VSD001-lm.csv",row.names=1))
tar.lm <- as.matrix(read.csv("VSD002-lm.csv",row.names=1))
## mymod <- statismoModelFromRepresenter(ref,kernel=list(c(50,50)),ncomp = 100) ## Old Interface
## new kernel interface as of 07/2016
GK <- GaussianKernel(50,50)
mymod <- statismoModelFromRepresenter(ref,kernel=GK,ncomp = 100) 

Bayes <- createBayes(mymod,sdmax = rep(4,50),wt=1.5,shrinkfun = function(x,i){ x <- x*0.93^i})

## setup similarity and affine icps
similarity = list(iterations=10,rhotol=pi/2)
affine = list(iterations=10,rhotol=pi/2)

### run the matching
matchGP <- gaussMatch(Bayes,tar,lm1 = ref.lm,lm2=tar.lm,iterations = 50,sigma = 30,gamma=2,toldist = 30,angtol = pi/2,nh=100,visualize = T,similarity = similarity,affine = affine)


```

Here is the output as movie:

<center>
<video width="420" height="315" controls> <source src="/resources/videos/femur.webm" frameborder="0" allowfullscreen> </video>
</center>




