---
layout: post
tags: 
- R 
- Morpho


date: 2015-04-05 13:50:00 +0200
title: Create a nicely colored easter egg with Morpho
---
    
On Friday, I added the option ```rampcolors``` to the function ```meshDist``` in [Morpho](https://github.com/zarquon42b/Morpho) to allow defining custom colorramps and adapted the function ```render``` to conveniently adapt the ramps, without recomputing distances.

Now we use this to create a nice easteregg:

```r
##    first we install the latest snapshot of Morpho
require(devtools)
install_github("zarquon42b/Morpho")
require(rgl);require(Morpho)
##create an ellipsoid
egg <- quad2trimesh(ellipse3d(diag(c(1.5,1,1)),subdivide = 5))
## get minimal point on x-axis
maxind <- which(vert2points(egg)[,1]== max(vert2points(egg)[,1]))
zero <- quad2trimesh(ellipse3d(diag(rep(1e-5,3)),centre = vert2points(egg)[maxind,])) 
mD <- meshDist(egg,zero,sign=F,steps=50,rampcolors = rainbow(6))

###here is a striped version

render(mD,steps=60,rampcolors = rep(c("red","orange","green"),4))

```
<figure class="center">
 <img rel="zoom" src="/resources/images/easteregg.png" alt="origstate" width="300" >
 <figcaption>Easter egg colored with function meshDist.</figcaption>
     </figure>
    
    
    <figure class="center">
 <img rel="zoom" src="/resources/images/easterstriped.png" alt="origstate" width="300" >
 <figcaption>Striped version.</figcaption>
</figure>
    
Happy easter holidays!










