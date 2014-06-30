---
layout: post
tag: RvtkStatismo R S4
date: 2014-06-30 17:40:00 +0200
title: RvtkStatismo - (almost) all members of statismo::StatisticalModel implemented
---

Yay - despite the arrival of a new intern, colloquium and another meeting, I managed to finish the implementation of member functions of statismo::StatisticalModel (only ```EvaluateSampleAtPoint()``` is missing). The (still very basic) documentation for these is to be found on [page 13](/resources/RvtkStatismo.pdf#page.13) of the [updated manual](/resources/RvtkStatismo.pdf). In some cases the arguments had to be adapted to be sensible within R, but basically this is pretty much the same as from C++. Only the ```GetDomain()``` function was split into ```GetDomainPoints()``` (output is a k x 3 matrix) and ```GetDomainSize()```. I will try to implement the constrained model building within the next week before the next big chunk of work is rolling my way. If there is anybody out there reading this: **PLEASE TEST** and report back.

TODO: 

* write a more specific documentation in R.
* test how easily the wrappers of RvtkStatismo can be used when writing a new package based on statismo and simply linking to this package. 
* If this works, this also needs to be properly documented and maybe a function ```RvtkStatismo.package.skeleton``` might prove useful - that is if anybody else uses this package.