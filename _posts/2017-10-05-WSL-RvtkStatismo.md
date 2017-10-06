---
layout: post
tags: 
- R 
- RvtkStatismo
- Linux
- Windows

date: 2017-10-06 08:25:00 +0200
title: Howto&#58; Installing RvtkStatismo on Windows 10 using WSL
---

Until recently, there was no feasible way to install RvtkStatismo on Windows due the virtual impossibility of compiling VTK and R with the same toolchain. However, Murat Maga (thanks for the heads up) brought my attention to the relatively new  Windows Subsystem for Linux (WSL) that can be installed on the latest Windows 10 builds. So I tried to install RvtkStatismo plus the popular R IDE Rstudio to allow for statistical shape modelling in R. Surprisingly, it worked pretty well. Below you can find a walk-through for doing so on your Windows 10 PC.


## Install WSL

I would definitely recommend to install the [Windows 10 Creators Update](https://support.microsoft.com/de-de/help/4028685/windows-get-the-windows-10-creators-update)

Then follow the steps outlined here: [https://msdn.microsoft.com/de-de/commandline/wsl/install_guide](https://msdn.microsoft.com/de-de/commandline/wsl/install_guide)

## Add the required repositories

To do so, run the "Bash on Ubuntu on Windows" App which will open a terminal window. Issue the following commands, adding a repo for the latest R-version, as well as my ppa with the prebuilt Statismo binaries (I will use the development version here):

```bash
sudo apt-add-repository ppa:marutter/rruttter
sudo apt-add-repostiory ppa:zarquon42/statismo-develop
sudo apt update
sudo apt install statismo-dev r-base-dev
```

## Optional: Install X-server and Rstudio

If you do not need an IDE, your are set now to install RvtkStatismo using the terminal (see below for the commands). If not, you need an X-server. The easiest way is to download and install [MobaXterm](https://mobaxterm.mobatek.net/download-home-edition.html). Then open it and select Session => Shell => Terminal Shell => Ubuntu Bash (WSL). Do this everytime you want to use the WSL.

Download [Rstudio version for ubuntu 16.04](https://www.rstudio.com/products/rstudio/download/) which will be a .deb file. To install it, use the MobaXterm terminal to run

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

Almost there now: We need to install the `devtools`package and then install RvtkStatismo

```r
install.packages("devtools")
devtools::install_github("zarquon42b/RvtkStatismo",ref="develop") 
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
