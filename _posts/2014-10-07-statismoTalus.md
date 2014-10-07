---
layout: post
tags: 
- R 
- RvtkStatismo

date: 2014-10-07 13:40:00 +0200
title: Getting nice deformations with (Rvtk)Statismo

---

I got involved in a project that includes surface matching of talus bones (Hi Peter) and using (Rvtk)Statismo in the registration process definitely pays off. 
Using a model generated for the atlas allows for nice controlling the shape deformation involved - even with my elastic ICP procedures from [mesheR](https://github.com/zarquon42b/mesheR).

While the first couple of targets could be matched easily in the way of [my last post](http://zarquon42b.github.io/2014/08/14/statismoMatching/), there was one bugger, quite different from the rest with a very wide articulation area.

###Coarse registration
The approach hereby was to use a smoothed gaussian displacement field (function ```gaussMatch```)[[1]](#1) with the displacement restricted by a deform as specified by [[2]](#2). The resulting displacement is then regularized by the statismo model (simply by calculating a weighted average for each displacement - one from suggested by the ICP and one from its counterpart projected into model space). 
This gets us already pretty close to the target without messing up the internal mesh structure (which would be the case without regularization):

<center>
<video width="420" height="315" controls> <source src="/resources/videos/talusfit1.webm" frameborder="0" allowfullscreen> </video>
</center>


###Fine registration
In a final step we simply use the result from the procedure and the function ```AmbergRegister``` from [mesheR](https://github.com/zarquon42b/mesheR) to fit the estimate smoothly onto the target. This is done without a shape model.
<center>
<video width="420" height="315" controls> <source src="/resources/videos/talusfit2.webm" frameborder="0" allowfullscreen> </video>
</center>

###Results
And here are the heatmap and displacement field: 
<img src="/resources/images/heatmapTalus.png"  style="height: 300px; float: left">
<img src="/resources/images/displaceTalus.png"  style="height: 300px">

###Timing
The timing is about 7 minutes for both registration processes, but could be improved by using a decimated mesh for the first registration.

<a id="1">[1]</a> Moshfeghi M, Ranganath S, Nawyn K. 1994. Three-dimensional elastic matching of volumes. IEEE Transactions on Image Processing: A Publication of the IEEE Signal Processing Society 3(2):128-138.</br>

<a id="2">[2]</a> Amberg B 2011. Editing faces in videos, University of Basel. http://edoc.unibas.ch/1415/.
