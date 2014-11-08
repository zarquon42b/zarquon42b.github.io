---
layout: post
tags: 
- R 
- Morpho 

date: 2014-11-07 10:05:00 +0200
title: Morpho&#58; Added sliding to minimize Procrustes distance and some thoughts
---

Responding to a user request, I implemented sliding of semi-landmarks in order to minimize Procrustes distance to the reference (as opposed to the already implemented bending energy criterion).
So, I implemented it and tested a bit and found out that it may lead to odd distortions if one is dealing with large shape differences and/or surfaces including concave parts such as crevasses.

Here are the tests (you will need to install "fastslide" branch from [GitHub](https://github.com/zarquon42b/Morpho/tree/fastslide)):
<figure>
   <img rel="zoom" src="/resources/images/orig.png" alt="bending" width="250" >
  <figcaption"><b>Fig. 1: </b>Red: semi-landmarks displaying a nose. Black: semi-landmarks displaying a grotesquely long nose.</figcaption>
</figure> 


```r
require(Morpho)
require(Rvcg)
data(nose)
semi <- vcgSample(shortnose.mesh,SampleNum = 1000,type="km")## subsample 1000 semi-landmarks on a surface
semilong <- tps3d(semi,shortnose.lm,longnose1)## deform it to be a long nose
## calculate original Procrustes distance between shapes
rotOrig <- rotonto(semi,semilong)#
angle.calc(rotOrig$X,rotOrig$Y)
#[1] 0.2663075

##first do relaxation minimizing bending energy:
relaxBending <- relaxLM(semi,semilong, mesh=shortnose.mesh, iterations=3,SMvector=1:nrow(semi), deselect=F,surp=1:nrow(semi),bending=T)
deformGrid3d(semi, relaxBending,col2=5)##smoothly deformed (see Fig 2.)
rotB <- rotonto(relaxBending,semilong)##align relaxed and reference
angle.calc(rotB$X,rotB$Y)
#[1] 0.251212

relaxProcD <- relaxLM(semi,semilong, mesh=shortnose.mesh, iterations=3,SMvector=1:nrow(semi), deselect=F,surp=1:nrow(semi),bending=F)
deformGrid3d(semi, relaxProcD,col2=4)##awkwardly deformed (see Fig 3.)
rotProcD <- rotonto(relaxProcD,semilong)
angle.calc(rotProcD$X,rotProcD$Y)
#[1] 0.227266

```
<table>
    <tr>
        <td>
            <figure>
                 <img rel="zoom" src="/resources/images/bending.png" alt="bending" height="200" >
                <figcaption><b>Fig. 2: </b>Cyan: relaxed using bending energy, Red: original.</figcaption>
            </figure>
        </td>
    
        <td>
            <figure >
                 <img rel="zoom" src="/resources/images/ProcD.png" alt="bending" height="200" >
                <figcaption"><b>Fig. 3:</b> Blue: relaxed using Procrustes distance, Red: original.</figcaption>
            </figure> 
       </td>
    </tr>
</table>   
 


##Conclusion
While Procrustes distance is smaller with this method, the shape is undergoing great distortions, because the deformation is not necessarily smooth. So, as far as I am concerned, I would stick with the bending energy criterion, when applying the sliding method.
