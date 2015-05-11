---
layout: post
tags: 
- R 
- statismo
- RvtkStatismo

date: 2015-05-11 13:50:00 +0200
title: Interactive statismo model visualization with R(vtkStatismo) and shiny
---

After having read a lot about interactive visualizations in R using [shiny](http://cran.r-project.org/web/packages/shiny/index.html) and [shinyRGL](http://cran.r-project.org/web/packages/shinyRGL/index.html), I finally found some time to create an interactive application to visualize a statismo shape model. I set up a shiny-server and hacked together a little interactive app showing a coarse mandible model (requires webGL and takes some time to load - but, **you can move it with your mouse** ;) ):

<iframe width="800px" height="800px" src="http://ckan.anthropologie.uni-freiburg.de:3838/sample-apps/shinyStatismo/" frameborder="0" allowfullscreen></iframe>
 
The code and data for this example can be found [here](https://github.com/zarquon42b/shinyapps/tree/master/shinyStatismo)