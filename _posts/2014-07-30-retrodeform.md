---
layout: post
tag: R rdf
date: 2014-07-30 12:59:00 +0200
title: Retrodeformation of a surface mesh based on bilateral landmarks (videos inside)
---

Forget what I said about Pandora's Box some weeks ago, that was complete nonsense, implementing stuff is still as hard as ever. I spent the last week implementing a symmetrizing algorithm that tries to reverse bending and local stretching caused for example by taphonomic processes. Unfortunately, the paper [[1]](#1) was quite obscure and I had to do a significant amount of literature research. But finally it worked out. Watch the visualizations of the deformation processes: 



<video width="420" height="315" controls> <source src="/resources/videos/frontview.webm" frameborder="0" allowfullscreen> </video>

<video width="420" height="315" controls> <source src="/resources/videos/bottomview.webm" frameborder="0" allowfullscreen> </video>

<video width="420" height="315" controls> <source src="/resources/videos/topview.webm" frameborder="0" allowfullscreen> </video>



**References**

<a id="1">[1]</a> Ghosh, D.; Amenta, N. & Kazhdan, M. Closed-form Blending of Local Symmetries. Computer Graphics Forum, Wiley-Blackwell, 2010, 29, 1681-1688
