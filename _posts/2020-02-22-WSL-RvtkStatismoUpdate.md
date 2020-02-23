---
layout: post
tags: 
- R 
- RvtkStatismo
- Linux
- Windows

date: 2020-02-22 08:25:00 +0200
title: UPDATE Howto&#58; Installing RvtkStatismo on Windows 10 using WSL
---

##  Update: 22.02.2020
* Added installation of precompiled R-packages from PPA 
* Removed the part on Windows 10 Creators Update

## Update: 1.10.2019
* Added rrutter3.5 repo
* Added notice about rstudio version


Until recently, there was no feasible way to install RvtkStatismo on Windows due the virtual impossibility of compiling VTK and R with the same toolchain. However, Murat Maga (thanks for the heads up) brought my attention to the relatively new  Windows Subsystem for Linux (WSL) that can be installed on the latest Windows 10 builds. So I tried to install RvtkStatismo plus the popular R IDE Rstudio to allow for statistical shape modelling in R. Surprisingly, it worked pretty well. Below you can find a walk-through for doing so on your Windows 10 PC.


## Install WSL
Got to Microsoft Store and install the App Ubuntu 18.04

<strike>I would definitely recommend to install the [Windows 10 Creators Update](https://support.microsoft.com/de-de/help/4028685/windows-get-the-windows-10-creators-update)

Then follow the steps outlined here: [https://msdn.microsoft.com/de-de/commandline/wsl/install_guide](https://msdn.microsoft.com/de-de/commandline/wsl/install_guide)</strike>


## Add the required repositories

To do so, run the "Bash on Ubuntu on Windows" App which will open a terminal window. Issue the following commands, adding a repo for the latest R-version, as well as my ppa with the prebuilt Statismo binaries (I will use the development version here):

```bash
sudo apt-add-repository ppa:marutter/rrutter3.5
sudo apt-add-repository ppa:marutter/c2d4u3.5
sudo apt-add-repository ppa:zarquon42/statismo-develop
sudo apt update
sudo apt install statismo-dev r-base-dev r-cran-morpho r-cran-devtools
```

## Optional: Install X-server and Rstudio

If you do not need an IDE, your are set now to install RvtkStatismo using the terminal (see below for the commands). If not, you need an X-server. The easiest way is to download and install [MobaXterm](https://mobaxterm.mobatek.net/download-home-edition.html). Then open it and select Session => Shell => Terminal Shell => Ubuntu Bash (WSL). Do this everytime you want to use the WSL.

<strike>Download [Rstudio version for ubuntu 16.04](https://www.rstudio.com/products/rstudio/download/)</strike>
Due to changes in rstudio, you will need a version <1.2.0, in my case [Rstudio 1.1.463](https://support.rstudio.com/hc/en-us/articles/206569407-Older-Versions-of-RStudio) worked fine. Download the *.deb* file. To install it, use the MobaXterm terminal to run

```
sudo dpkg -i path_to_rstudio_deb_file 
```

If you have downloaded it to your Download dir, this looks like this in my case:


```
sudo dpkg -i  /mnt/c/Users/schlager/Downloads/rstudio-xenial-1.0.153-amd64.deb
sudo apt install -f #to install missing dependencies

```

Now run Rstudio by issueing (surprise, surprise)

```
rstudio
```

## Install RvtkStatismo

Almost there now: We need to install the `devtools`package and then install *RvtkStatismo* and for using it in registration tasks I recommend installing *mesheR* as well

```r
devtools::install_github("zarquon42b/RvtkStatismo",ref="develop")
devtools::install_github("zarquon42b/mesheR")

## we chose the develop branch matching the statismo version above
```

## Proof

Here is the proof: I ran `example("statismoModelFromRepresenter",run.dontrun=TRUE)`: 
<a id="Fig1"></a>
<figure class="center">
    <img rel="zoom" src="/resources/images/Win10WSL.png" alt="initial state" height="300" > 
    <figcaption>Fig 1: Ambient space deformation showing the full grid</figcaption>
</figure> 


## More

This allows for a ton of new possibilities and gives Windows users now access to other *nix packages such as the awesome [ANTsR](https://github.com/ANTsX/ANTsR) or [SimpleITK](https://github.com/SimpleITK/SimpleITK) for image registration and processing. 
