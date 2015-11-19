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


