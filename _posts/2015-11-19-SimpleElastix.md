---
layout: post
tags: 
- R 
- RANTs
- Statismo


date: 2015-11-19 15:45:00 +0200
title: SimpleElastix&#58; Wrapping elastix in R and using a statismo deformation model
---

Googleing for "stochastic gradient descent", I stumbled upon SimpleElastix, a SimpleITK implementation of the registration tool [elastix](http://elastix.isi.uu.nl/) that wraps the code for R, Python, etc.. This got me really excited, because I was already playing with statismo-elastix.


Here is how to get things up and running in R:

1. Get SimpleElastix as described here: [http://simpleelastix.readthedocs.org/GettingStarted.html](http://simpleelastix.readthedocs.org/GettingStarted.html)
2. Do the Superbuild
3. Get statismo-elastix (fixed for statismo 0.11 from [my fork](https://github.com/zarquon42b/statismo-elastix) and rebuild the elastix component pointing to the statismo-elastix component directory.
4. rebuild SimpleElastix (as we updated elastix)
5. Go to SimpleElastix-build/Wrapping/Rpackaging and run ```R CMD INSTALL SimpleITK```


And here is an example, assuming you have a deformation model called *defmod.h5* (created with statismo-build-deformation-model), a fixed model in the domain of the deformation model called *template.nii.gz* and a moving image (already aligned to the model) called moving.nii.gz and finally an elastix parameter file called [*Parameters_statismo.txt*](/resources/Parameters_statismo.txt).

We then run statismo-elastix from R:

```r
require(SimpleITK)
movingimage <- ReadImage("moving.nii.gz")
fixedimage <- ReadImage("template.nii.gz")

##cast to float to avoid errors due to unimplemented types
ci <- CastImageFilter()
ci$SetOutputPixelType("sitkFloat32")
image1 <- ci$Execute(movingimage)
image2 <- ci$Execute(fixedimage)

##set up elastix
elastix <- SimpleElastix()
elastix <- elastix$SetFixedImage(image2)
elastix <- elastix$SetMovingImage(image1)
#parameterMap <- GetDefaultParameterMap("affine")
pm <- elastix$ReadParameterFile("./Parameters_statismo.txt")
#parameterMap("Registration")= ["MultiResolutionRegistration"]
elastix <- elastix$SetParameterMap(pm)
elastix <- elastix$LogToConsoleOn() ## write stdout to console
##create output dir
dir.create("statismo-test")
elastix <- elastix$LogToFolder("statismo-test")

##run elastix
elastix <- elastix$Execute()

```
NOTE: At the moment, the Python wrappers, however, seem to offer the smoothest integration. So here is a little [python script](/resources/statismoElastix.py) and a [wrapper function](/resources/statismoElastix.r) to call it from R and pass the arguments.

### Python script:

```python
import sys
import os as os
import SimpleITK as sitk
from subprocess import call

def statismoElastix(fixedimage, movingimage,  model, meshname,outdir="",para_file=""):
    # convert to strings
    outdir = str(outdir)
    movingimage = str(movingimage)
    fixedimage = str(fixedimage)
    model = str(model)
    meshname = str(meshname)
    para_file = str(para_file)
    # create output directory
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    # load images
    image1= sitk.ReadImage(fixedimage)
    image2 = sitk.ReadImage(movingimage)
    # convert images to float
    ic = sitk.CastImageFilter()
    ic.SetOutputPixelType(sitk.sitkFloat32)
    image1a = ic.Execute(image1)
    image2a = ic.Execute(image2)
    ## set up elastix
    elastix = sitk.SimpleElastix()
    elastix.SetFixedImage(image1a)
    elastix.SetMovingImage(image2a)
    if len(para_file) == 0: 
        pm = sitk.GetDefaultParameterMap("nonrigid")
        pm["Transform"] = ["SimpleStatisticalDeformationModelTransform"]
        pm["StatisticalModelName"] = [model]
        pm["Interpolator"] = ["BSplineInterpolator"]
        pm["ImageSampler"] = ["Random"]
        pm["Metric"] = ["AdvancedMattesMutualInformation"]
        pm["Registration"] = ["MultiResolutionRegistration"]
    else:
        pm = elastix.ReadParameterFile(para_file)

    elastix.SetParameterMap(pm)
    elastix.LogToFolder(outdir)
    elastix.LogToConsoleOn()
    elastix.Execute()
    trafopara = outdir + "/TransformParameters.0.txt"
    
    # call transformix
    # sitk.WriteImage(elastix.GetResultImage(),"test.nii.gz")
    call(["transformix","-tp", trafopara,"-out", outdir,"-def", meshname])
    #print outdir
    trafomesh = outdir + "/outputpoints.vtk"
    return trafomesh

```

### R Wrapper:

```r
require(Morpho);require(RvtkStatismo);require(rPython)
#' run elastix with statismo-elastix plugin
#'
#' run elastix with statismo-elastix plugin and deform a mesh based on the transform
#' @param fixedimage fix image (in the domain of the deformation model) path
#' @param movingimage moving image path
#' @param model statismo deformation model path
#' @param mesh mesh3d
#' @param outdir where to write elastix output data
#' @param parafile character: optional read parameter file
#' @param IJK2RAS 4x4 transform to project mesh into image space
#' 
statismoElastix <- function(fixedimage, movingimage, model, mesh, outdir="./", parafile=NULL, IJK2RAS = diag(c(-1,-1,1,1))) {
    rPython::python.load("statismoElastix.py")
    mesh2ras <- Morpho::applyTransform(mesh,IJK2RAS)
    outmesh <- paste0(tempdir(),"mesh2ras")
    if (is.null(parafile))
        parafile <- ""
    RvtkStatismo::vtkMeshWrite(mesh2ras,outmesh)
    outmeshname <- paste0(outmesh,".vtk")
    callit <- rPython::python.call("statismoElastix",fixedimage, movingimage, model,  outmeshname, outdir,parafile)
    out <- RvtkStatismo::read.vtk(callit)
    out <- Morpho::applyTransform(out,IJK2RAS)
    return(out)
}


```

