---
layout: post
tags: 
- R 
- RvtkStatismo 
- statismo

date: 2014-10-27 16:59:00 +0200
title: RvtkStatismo&#58; Add isotropic scaling when creating a Gaussian Process model
---

I wondered whether it might be useful to add isotropic scaling to when building a Gaussian Process model from a reference. Because in samples with a fair amount of isotropic variation, the additional information might be worth accounting for. 
In ```RvtkStatismo```'s functions ```statismoModelFromRepresenter``` and ```statismoGPmodel```, I added the option isoScale to specify the range of the isotropic scale (e.g. ```isoScale=0.05``` will result in a scale factor of &#177;15% of the original size within the range of 3 standard deviations). 

Here is an example (once again using Marcel's example femurs) - you will, of course need to install latest master branch of RvtkStatismo:

  

```r
require(RvtkStatismo)

###get the data
download.file(url="https://github.com/marcelluethi/statismo-shaperegistration/raw/master/data/VSD001_femur.vtk","./VSD001_femur.vtk",method = "w")
download.file(url="https://github.com/marcelluethi/statismo-shaperegistration/raw/master/data/VSD002_femur.vtk","./VSD002_femur.vtk",method = "w")
download.file(url="https://github.com/marcelluethi/statismo-shaperegistration/raw/master/data/VSD001-lm.csv","./VSD001-lm.csv",method = "w")
download.file(url="https://github.com/marcelluethi/statismo-shaperegistration/raw/master/data/VSD002-lm.csv","./VSD002-lm.csv",method = "w")

### read the data
ref <- read.vtk("VSD001_femur.vtk")
tar <- read.vtk("VSD002_femur.vtk")
ref.lm <- as.matrix(read.csv("VSD001-lm.csv",row.names=1))
tar.lm <- as.matrix(read.csv("VSD002-lm.csv",row.names=1))

### create models
mymod <- statismoModelFromRepresenter(ref,kernel=list(c(50,50)),ncomp = 100)#default Gaussian Process model
mymodScale <- statismoModelFromRepresenter(ref,kernel=list(c(50,50)),isoScale=0.05,ncomp = 100)#add isotropic scaling with 3 sd being +- 15%

## calculate constrained models based on target landmarks
cmod <- statismoConstrainModel(mymod,tar.lm,ref.lm,2)
cmodS <- statismoConstrainModel(mymodScale,tar.lm,ref.lm,2)
```

###Here are the results (*green*=reference/constrained model mean):
<figure>
  <img src="/resources/images/origstate.png" alt="origstate" width="400" >
  <figcaption>Fig. 1: Original state with landmarks.</figcaption>
</figure> 
<figure>
  <img src="/resources/images/constNoScale.png" alt="The Pulpit Rock" width="400">
  <figcaption>Fig. 2: The constrained GP model without scaling.</figcaption>
</figure> 

<figure>
  <img src="/resources/images/constScale.png" alt="The Pulpit Rock" width="400">
  <figcaption>Fig.3: The constrained GP model supplemented with isotropic scaling.</figcaption>
</figure>






