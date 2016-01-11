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

There are two ways to tell R, where the libraries reside:

1. Dirty solution. Copy the libs to where R can find them:

    ```bash
    cp INSTALL/lib/libvtk* INSTALL/lib/libboost* INSTALL/lib/libhdf5* /Library/Frameworks/R.framework/Resources/lib
     
    ```

2. In OS X Yosemite there seems no way to set the environment variable ```DYLD_LIBRARY_PATH```  globally, so we create a file [~/Library/LaunchAgents/statismo.plist](/resources/statismo.plist) containing the following (of course replacing the path with yours):

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
      <key>Label</key>
      <string>my.startup</string>
      <key>ProgramArguments</key>
      <array>
        <string>sh</string>
        <string>-c</string>
        <string>
        launchctl setenv DYLD_LIBRARY_PATH /Users/myuser/statismo/build/INSTALL/lib
       </string>
    
      </array>
      <key>RunAtLoad</key>
      <true/>
    </dict>
    </plist>
    ```
    Now logout and login again.

    To use RvtkStatismo in a console you need to run (works for one session only):

    ```
    export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/Users/myuser/statismo/build/INSTALL/lib
    ```


Fire up R and run 

```r
    install.packages("devtools")
    devtools::install_github("zarquon42b/RvtkStatismo",args="--configure-args='path_to_superbuild/Statismo-build'")
```


Happy holidays.
 
