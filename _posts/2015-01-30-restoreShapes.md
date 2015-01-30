---
layout: post
tags: 
- R 
- statismo
- RvtkStatismo

date: 2015-01-30 13:50:00 +0200
title: RvtkStatismo - Restore shapes from a model (with stored PC-scores)
---
As a follow up of my [earlier post](/2015/01/30/remeshList/), one might want to change an existing shape model's general mesh resolution. If the PC-scores are stored (and the model is not reduced in variance), it is fairly easy to obtain the orginal shapes.

Assume you have stored a statismo shape model (using a mesh representer) in the local file *mymod.h5*, to restore the shapes, the commands in **R** are simply:

```r
require(RvtkStatismo)
mymod <- statismoLoadModel("mymod.h5")

## or (in case you do not have one and want to test the code,
## use the example from the RvtkStatismo help to create 
## a model from some landmarks:

require(Morpho)
data(boneData)
align <- rigidAlign(boneLM)$rotated
mymod <- statismoBuildModel(align,representer=align[,,1],scale=FALSE)
##now restore shapes
rest <- restoreSamples(mymod)
```

Now we could remesh this sample and create a new statismo model. </br>
Have a nice weekend!