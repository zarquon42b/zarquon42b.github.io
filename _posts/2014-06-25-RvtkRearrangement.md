---
layout: post
tags: 
- RvtkStatismo 
- R
title: class pPCA and rearrangements in RvtkStatismo
---

I got rid of the ugly bastard class ```pPCAconstr```! Now there is only one shape model class that can be restricted by defining existing/missing coordinates and a given specific shape (function ```ComputeConstrainedModel()``` (I have not yet looked at the statismo methods to restrict a model, though).

###Header files
Header files now reside in inst/include, thus future packages may use the already implemented routines (e.g. conversion between statismo and pPCA) by adding 

* LinkingTo: RvtkStatismo in the package's DESCRIPTION file
* adding RvtkStatismo to **Import** section in DESCRIPTION
* adding ```importFrom RvtkStatismo statismoBuildModel``` (or any function from RvtkStatismo) to trigger loading RvtkStatismo's dynlib.

###File layout
I made the file naming in the R folder more comprehensive and split a couple of very long files.

###Misc
I added a converter between *vtkPolyData* and *vtkUnstructuredGrid* (courtesy of VTK examples in their Wiki), that might prove usefull when implementing more representers in the future.

