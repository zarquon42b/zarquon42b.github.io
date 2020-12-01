---
layout: post
tags: 
- R 
- Morpho

date: 2020-12-01 13:25:00 +0200
title: New Im- and Export functions for 3DSlicer in Morpho
---

Hi everyone, those of you working with [3DSlicer](https://www.slicer.org/) may have seen that as of version 4.11, Slicer introduced a new json-based markup format. It now supports Curves (open and closed - pretty cool!) as well as traditional markups. 
Last week I added two new functions to Morpho: `read.slicerjson` and `write.slicerjson` that allow im- and exporting to the new format. 
As Slicer also changed the internal coordinate system to LPS, I also added the function `LPS2RAS` that converts both ways (as the transform is self-inverse).

### How to install the latest development version

```
devtools::install_github("zarquon42b/Morpho")
```

Please test it and report back issues or missing functionality.
