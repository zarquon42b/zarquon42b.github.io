---
layout: post
tags: 
- R 
- Morpho

date: 2016-03-14 10:25:00 +0200
title: Morpho&#58; Slide surface semi-landmarks without the actual surfaces
---

In Biology and Physical Anthropology, sliding semi-landmarks are widely used to estimate the surface shape of a biological structure. The "sliding" part means that (mathematical) homology between specimens is enforced by allowing the coordinates to slide along the surfaces in order to minimize some metric (bending energy, Procrustes distance). As the surface is usually curved, it has to be approximated locally, to allow formulating the minimization as a linear problem. This is done by calulating the tangent plane at each semi-landmark - usually by the plane orthogonal of the surface's normal at that point. After each iteration, the slided coordinates are reprojected back onto the surface representation (usually a triangular mesh).
Based on a user request, I added a procedure to allow sliding without having the actual surface available. The main issue, hereby is to determine the tangent plane. To accomplish this, the normal at each coordinate is computed based on the positions of the 10 nearest neighbours (using ```Rvcg::vcgUpdateNormals```). Based on these normals the tangent planse are calculated as orthogonal complements (```Morpho::tangentPlane```).

**CAVEATS:**

* This works only for single layers of semi-landmarks and not for shapes representing thin two-sided structures (unless the coordinate density is high)
* Due to unavailable surfaces onto which the slided coordinates could be projected, the slided positions may be off the original surface
* To reproduce this, install Morpho from source ```devtools::install_github("zarquon42b/Morpho")```

## Example 1 

Estimate the normals from the pointcloud and visualize the resulting tangent planes (<a href="#Fig1">Figure 1</a>).

```r
require(Morpho);require(Rvcg)
data(nose)
normalcloud <- vcgUpdateNormals(shortnose.lm)

## visualize normals
require(rgl)
spheres3d(shortnose.lm,col="red",radius=0.2)
plotNormals(normalcloud,lwd=2,long=2)

# visualize tangent planes

## estimate plane vectors from normals
planes <- apply(normalcloud$normals,2,function(x) x <- tangentPlane(x[1:3]))

## small helperfunction to create a mesh with 2 triangles forming a square representing the tangent plane
tan2mesh <- function(x,y,pt) {
    vb <- matrix(1,4,4)
    vb[1:3,1] <- pt[1:3]
    vb[1:3,2] <- pt[1:3]+x
    vb[1:3,3] <- pt[1:3]+y
    vb[1:3,4] <- vb[1:3,3]+x
    cent <- (vb[,4]-vb[,1])/2
    vb <- vb-cent
    it <- matrix(c(1,4,3,1,2,4),3,2)
    out <- list(vb=vb,it=it)
    class(out) <- "mesh3d"
    return(out)
}
## create all the little meshes and concatenate them
planemeshes <- mergeMeshes(lapply(1:nrow(shortnose.lm), function(x) x <- tan2mesh(planes[[x]]$y,planes[[x]]$z,normalcloud$vb[,x])))
## render 
shade3d(planemeshes)
```

<a id="Fig1"></a>
<figure class="center">
    <img rel="zoom" src="/resources/images/nose_planes.png" alt="example 1" height="500" >    
    <figcaption>Fig. 1: Normals and tangents estimated from point cloud.</figcaption>

</figure> 



## Example 2

We use the example data included in Morpho and compare the results with and without surfaces. We can see that the result is very close to the one including surfaces (<a href="#Fig2">Figure 2</a>) - only the lonely coordinates around the nostrils that are allowed to slide differ as the reprojection onto the surface is missing.

```r
require(Morpho)
data(nose)
## create mesh for longnose
longnose.mesh <- tps3d(shortnose.mesh,shortnose.lm,longnose.lm,threads=1)
meshlist <- list(shortnose.mesh,longnose.mesh)
data <- bindArr(shortnose.lm, longnose.lm, along=3)
dimnames(data)[[3]] <- c("shortnose", "longnose")

## define curves and surface landmarks
fix <- c(1:5,20:21)
outline1 <- c(304:323)
outline2 <- c(604:623)
outlines <- 611:623
outlines <- list(outline1,outline2)
surp <- c(1:623)[-c(fix,outline1,outline2)]
slideWithCurves <- slider3d(data, SMvector=fix, deselect=TRUE, surp=surp, meshlist=meshlist,iterations=3,outlines=outlines)

## An example with sliding without meshes by estimating the surface from the
## semi-landmarks

slideWithCurvesNoMeshes <- slider3d(data, SMvector=fix, deselect=TRUE, surp=surp,iterations=3,outlines=outlines)

## compare it to the data with surfaces for the 1st specimen
deformGrid3d(slideWithCurves$dataslide[,,1],slideWithCurvesNoMeshes$dataslide[,,1],ngrid = 0)
```

<a id="Fig2"></a>
<figure class="center">
    <img rel="zoom" src="/resources/images/slide_compare_nose.png" alt="example 1" height="500" >    
    <figcaption>Fig. 2: Differences between sliding with actual and with approximated surface. Red: slided along surface. Green: slided along approximated surface.</figcaption>

</figure> 
