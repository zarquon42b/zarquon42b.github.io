---
layout: post
tags: 
- vtk 
- RvtkStatismo
date: 2014-07-16 10:09:00 +0200
title: VTK - Opening Pandora's Box
---

Up until recently, implementing new algorithms meant mainly: reading papers, trying to figure out how to implement it and finally code profiling. This was really time consuming, but at least at some point in time I knew exactly how and why everything was working. As I now have an interface between R and VTK this seems be somewhat changing. An example: our PhD student asked me if it was possible to convert a 3D-mesh into a 3D-image. After some googeling and realizing that VTK supports such a thing, this was a complete no-brainer to implement. In a matter of minutes, the code was hacked together and the function ```vtkMesh2Image``` was added to ```RvtkStatismo```. Now I don't know whether to cheer or to frown: On one hand I can now implement a lot of stuff I always wanted to do but on the other hand I do not know anymore what exactly is going on under the hood...

But I tend to be cheering because it is like getting a large box of LEGO (even LEGO Technic) for free.
