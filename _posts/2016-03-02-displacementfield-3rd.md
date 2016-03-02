---
layout: post
tags: 
- R 
- RvtkStatismo
- Statismo
- mesheR

date: 2016-03-02 16:15:00 +0200
title: Update&#58; Displacement fields the 3rd
---

To make the plotting of displacement fields more comprehensive, I deprecated ```plotDisplacementField```  in favor of a ```plot```-method for objects of class ```DisplacementField```, returning (and optionally plotting) an object of the (newly introduced) class ```DisplacementPlot```, that in turn has its own  ```plot```-method.

For better visualization, and as [rgl](https://cran.r-project.org/package=rgl) has no rendering options for arrows, I decided to render the starting positions as points, leading to lollipop graphs (<a href="#Fig1">Fig. 1</a> shows the resulting plot, using the [example from yesterday](../../01/displacementfieldsupdate/)). The code for the plot below is simply:

```r
plot(dispfield)
wire3d(dummytrans)
```






<a id="Fig1"></a>
<figure class="center">
    <img rel="zoom" src="/resources/images/tweak_disp_plot.png" alt="example 1" height="350" >    
    <figcaption>Fig. 1: Pimped displacement field rendering - with reference mesh added as wireframe</figcaption>

</figure> 

And finally, there is a new complementing function ```invertDisplacementField``` to invert an existing displacement field.
