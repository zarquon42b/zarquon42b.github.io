---
layout: post
tags: 
- statismo

date: 2024-10-01 16:25:00 +0200
title: Statismo packages now available for Ubuntu 24.04 LTS (Noble Numbat)
---

Hi everyone,

I am a bit late this time but as I am probably the only user, this doesn't matter (LOL). After the release of 24.04 LTS (Noble Numbat), I had to repackage the [*statismo*](https://github.com/statismo/statismo) C++ library, which I use to build the R-package [RvtkStatismo](https://github.com/zarquon42b/RvtkStatismo) that allows shape modelling in R. I also had to fix some issues due to changes in boost > 1.8.

The software packages can be found in my [PPA](https://launchpad.net/%7Ezarquon42/+archive/ubuntu/statismo-develop).


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
