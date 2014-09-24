---
layout: post
tags: 
- RvtkStatismo 
- R 
- S4
date: 2014-07-02 11:25:00 +0200
title: RvtkStatismo now supports im- and export of ModelInfo
---

After struggeling with the documentation of statismo, I found out that things had changed: 
Instead of 

```c
KeyValueList DataInfo = model->GetModelInfo().GetDataInfo() 
```

I had to do

```c
BuilderInfoList binfo = model->GetModelInfo().GetBuilderInfoList();
if (binfo.size() > 0) { 
   KeyValueList DataInfo = binfo[0].GetDataInfo();
   ...
```
For implementing the modelinfo into ```pPCA```, I created a new private S4 class called ```modelinfo``` that stores the lists ```datainfo``` and ```paraminfo```. Both contain two-valued character vectors - similar as in statismo. These contain the first entry of the ```BuilderInfoList```:

```c
BuilderInfoList binfo = model->GetModelInfo().GetBuilderInfoList();
KeyValueList DataInfo = binfo[0].GetDataInfo();
KeyValueList BuildInfo = binfo[0].GetParameterInfo();

```


