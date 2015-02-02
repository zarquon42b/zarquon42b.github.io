---
layout: post
tags: 
- R 
- mesheR

date: 2015-01-30 13:40:00 +0200
title: Remesh or decimate a set of registered meshes, while preserving correspondences

---
This morning, I implemented two simple routines in my R-package [mesheR](https://github.com/zarquon42b/mesheR), that allow to remesh or decimate a set of registered meshes (i.e. with all vertices in pseudo-homologous positions). The procedure is quite simple: select a reference from the sample and apply the decimation/remeshing. Then get the barycentric coordinates of the new vertex positions on the original mesh. These in turn can then be used to extract the corresponding vertex positions of the mesh on all the sample - as the mesh structure is identical throughout the sample.

####NOTE: The meshes do not have to be prealigned.

###Example

<figure>
    <img rel="zoom" src="/resources/images/meshlist1.png" alt="origstate" width="400" >
  <figcaption><b>Fig. 1:</b> A set of registered meshes (62623 faces).</figcaption>
</figure> 
**Fig. 1** shows a sample of mandibles (registered using ```gaussMatch``` with a GP-model created with [RvtkStatismo](https://github.com/zarquon42b/RvtkStatismo)). But maybe for some registration tasks I want to create a statistical model with only 10% the amount of faces (let's set it rather low to see the effect better). Assume we have saved the meshes in a list in ```R``` called ```matchlist```. Now we simply decimate the sample by calling ```decimateList(matchlist,percent=0.1)``` (you can also use all parameters from the workhorse function [vcgQEdecim](https://github.com/zarquon42b/Rvcg/blob/master/R/vcgQEdecim.r). </br>

And here we go: **Fig. 2** shows the same surfaces but with less vertices and faces.

<figure>
    <img rel="zoom" src="/resources/images/meshlistDec.png" alt="origstate" width="400" >
  <figcaption><b>Fig. 2:</b> The same mandibles now reduced to 6262 faces.</figcaption>
</figure> 

Now we could for example create a coarser statistical model from those.You can also do a complete remeshing using the function ```remeshList``` wrapping the remeshing function [vcgUniformRemesh](https://github.com/zarquon42b/Rvcg/blob/master/R/vcgUniformRemesh.r).