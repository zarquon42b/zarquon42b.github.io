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

