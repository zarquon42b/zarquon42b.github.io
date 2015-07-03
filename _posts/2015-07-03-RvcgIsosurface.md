---
layout: post
tags: 
- R 
- Rvcg


date: 2015-07-03 12:45:00 +0200
title: Rvcg&#58; Create an Isosurface from a 3D Image using vcgIsosurface
---

While ```vcgIsosurface``` is available for some time now in Rvcg, I tweaked it to allow for specifying not only origin and spacing, but now also for defining an IJK to RAS transform and the direction matrix of the original image. The resulting surface is then congruent with the original image, when viewed in Slicer4.

Here are two examples (one for ANTsR and one for SimpleITK) how to create an isosurface from a segmentation (the result combined with the image can be seen in [Figure 1](#Fig1).)


###ANTsR
```r
require(ANTsR)
require(Rvcg)
###load image
myimage2 <- antsImageRead("myimageThresh.nii.gz")

### Get Array
antsArr <- ANTsR::as.array(myimage2)

### Generate surface
surfAnts <- vcgIsosurface(antsArr,threshold = 255,spacing = antsGetSpacing(myimage2),origin = antsGetOrigin(myimage2),direction=antsGetDirection(myimage2),as.int=TRUE)

### decimate it
surfAnts <- vcgQEdecim(surfAnts,edgeLength = 1)

### smooth it
surfAnts <- vcgSmooth(surfAnts)

### save it to disk 

vcgPlyWrite(surfAnts)

```

###SimpleITK
The example for SimpleITK is pretty much the same, the main differences is that we have to transform the direction vector into matrix ourselves:

```r
require(SimpleITK)
require(Rvcg)
###load image
myimage <- ReadImage("myimageThresh.nii.gz")

### Get Array
sitkArr <- SimpleITK::as.array(myimage)

### Generate surface
surfSitk <- vcgIsosurface(sitkArr,threshold = 255,spacing = myimage$GetSpacing(),origin = myimage$GetOrigin(),direction=matrix(myimage$GetDirection(),3,3),as.int=TRUE)

### decimate it (my take some time)
surfSitk <- vcgQEdecim(surfSitk,edgeLength = 1)

### smooth it
surfSitk <- vcgSmooth(surfSitk)

### save it to disk 

vcgPlyWrite(surfSitk)

```



<a id="Fig1"></a>
<figure class="center">
    <img rel="zoom" src="/resources/images/slicer.png" alt="slicer" width="450" >
 <figcaption>Fig. 1: Surface representation and original (unsegmented) image in Slicer.</figcaption>
</figure> 
</br>