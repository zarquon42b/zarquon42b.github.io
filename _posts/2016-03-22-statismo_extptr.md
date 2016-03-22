---
layout: post
tags: 
- R 
- Morpho
- statismo
- RvtkStatismo
date: 2016-03-22 15:25:00 +0200
title: RvtkStatismo&#58; Store your models as external pointers
---

In [RvtkStatismo](https://github.com/zarquon42b/RvtkStatismo), statistical shape models are stored as objects of class `pPCA` and in each call of the underlying [statismo](https://github.com/statismo/statismo) functions are converted to `StatisticalModel<vtkPolyData>` and back, which duplicates memory and reduces speed (not very much, but still ...). 
As I got comfortable with Rcpp's external pointers (see my [recent post](../../09/Rvcg-XPTr/)), I decided to dump ```boost::shared_ptr``` in favor of `Rcpp::XPtr` with the additional benefit that the pointer can now be directly exposed to R. Pointers to shape models are stored in the newly introduced class `pPCA_pointer` and methods are added to access and process these objects. For the user it does not make any differences whether dealing with `pPCA` or `pPCA_pointer`, except that the pointers can't be saved in the R work-space (however, using `statismoSaveModel` is more efficient anyway). The functions `statismoBuildModel`, `statismoLoadModel`, `statismoConstrainModel` and `statismoBuildConditionalModel`, now have the additional option `pointer` and return, if `pointer=TRUE`, an object of class `pPCA_pointer`.

In order to install and test the new features you need to: 

1. The development branch of statismo (ubuntu 14.04 users can install it from my [ppa](https://launchpad.net/~zarquon42/+archive/ubuntu/statismo-develop):
   
	   sudo apt-add-repository ppa:zarquon42/statismo-develop	   
	   sudo apt-get update   
	   sudo apt-get install statismo


2. the development branch of RvtkStatismo
   In R issue:

	   devtools::install_github("zarquon42b/Rvtkstatismo",ref="develop")
	

