---
layout: post
tags: 
- statismo

date: 2022-04-06 11:25:00 +0200
title: Statismo packages now available for Ubuntu 22.04 LTS (Jammy Jellyfish)
---

Hi everyone,

with the advent of Ubuntu 22.04 (Jammy Jellyfish), I had to repackage the *statismo* C++ library, which I use to build the R-package [RvtkStatismo](https://github.com/zarquon42b/RvtkStatismo) that allows shape modelling in R. 

The software packages can be found in my [PPA](https://launchpad.net/%7Ezarquon42/+archive/ubuntu/statismo-develop). As ubuntu 22.04 ships with ITK5 and VTK9, I took the chance to update and adapt the *statismo* code. Again, I had to fight badly to get everything linked correctly against the HDF5 library (it turned out that the path was included in the ITK_LIBRARY variable when using the Ubuntu packages). As before, there is also the *statismo-tools* package that brings some nifty command line tools that allow for some basic shape modeling routines.

As I have already updated *RvtkStatismo* to the *develop* version of statismo I will only maintain and package that branch of *statismo* in the forseable future. This branch corresponds to the *RvtkStatismo* *develop* branch as well, so make sure to pick the correct one (see examples below)


## Install statismo
Install the latest release:


```r
sudo apt-add-repository ppa:zarquon42/statismo-develop
sudo apt update
sudo apt install statismo-dev
```

## Install RvtkStatismo

Almost there now: We need to install the `devtools`package and then install *RvtkStatismo* and for using it in registration tasks I recommend installing *mesheR* as well

```r
devtools::install_github("zarquon42b/RvtkStatismo",ref="develop")
devtools::install_github("zarquon42b/mesheR")

## we chose the develop branch matching the statismo version above
```
