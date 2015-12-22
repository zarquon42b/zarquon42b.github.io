---
layout: post
tags: 
- R 
- RvtkStatismo
- Statismo


date: 2015-12-22 15:45:00 +0200
title: RvtkStatismo&#58; Now working on OSX
---

As I got hands on a VM running OSX Yosemite, I managed to install RvtkStatismo on OSX. Unfortunately in Yosemite, the hombrew packages seem not work correctly, so let us do the statismo superbuild.

Install R and XCODE, run the following lines in your terminal:

```
 git clone https://github.com/statismo/statismo.git
 mkdir build && cd build
 cmake ../statismo/superbuild 
 make ## make a coffee or go for lunch
 ```

Here comes the dirty part (people familiar with both R and OSX might want to show me the light please, as setting DYLD\_LIBRARY\_PATH did not make R find the libs):
Copy the libs to where R can find them:

```bash
 cp INSTALL/lib/libvtk* INSTALL/lib/libboost* INSTALL/lib/libhdf5* /Library/Frameworks/R.framework/Resources/lib
 
``` 

Fire up R and run 

```r
    install.packages("devtools")
    devtools::install_github("zarquon42b/RvtkStatismo")
```

Happy holidays.
 
