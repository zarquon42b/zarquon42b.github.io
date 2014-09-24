---
layout: post
tags: 
- RvtkStatismo 
- R 
- S4
date: 2014-07-01 15:05:00 +0200
title: RvtkStatismo - update and some fixes
---

This morning I realised that I had introduced some issues with S4 classes: As R accepts the S3 class ```mesh3d``` as list, an object of class ```pPCA``` passes class-validation in R but NOT in Rcpp (on the C++ level). The ladder threw an exception when trying to import a model with a polygon mesh as representer. Thus, I had to add a virtual class called ```representer``` that now is a superclass of list and mesh3d. Now only the implementation of meshinfo seems to be missing (both in the wrapper and the S4 class specification), but it should not be a big problem to do that.

###Documentation
I spent quite some time in making documentation more comprehensive (see [updated manual](/resources/RvtkStatismo.pdf)).

