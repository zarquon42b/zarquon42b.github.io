---
layout: post
tags: 
- R 
- Morpho 

date: 2014-10-31 10:05:00 +0200
title: Morpho&#58; massive improvements in performance of semi-landmark sliding
---

On my visit of the MPI in Leipzig (which was great, thanks a lot!!), Philip Gunz told me about a method ([proposed by Demetris Halazonetis](http://www.dhal.com/downloads/CompactSlidingSemilandmarks.pdf)) that could improve computation time and memory footprint for the relaxation of semi-landmarks, which are serious restrictions on the maximum amount of coordinates usable with this method. So I spend the best part of Wednesday night and the 6-hour train ride home to tweak the underlying subroutines, making use of the excellent R-package ```Matrix``` and its large variety of classes for all kinds of sparse/triangle/symmetric matrices.
At the end I was able to run the examples in my package on my netbook as fast as the untweaked version on my desktop workstation. 

So when I arrived at the office this morning, I was eager to compare benchmarks between those version on my machine. The hardware specs are:

**CPU**: Intel(R) Xeon(R) CPU E5-1650 v2 @ 3.50GHz (Hexacore)</br>
**RAM**: 32GB DDR3 @1600 MHz

  

```r
### first create a benchmarking function

benchslide <- function(nofl=c(50,100,200,500,1000,2000,3000,4000)) {
    require(Morpho)
    require(Rvcg)
    data(nose)
    tmp <- NULL
    for (i in 1 : length(nofl)) {
        cat(paste0("running function with ",nofl[i]," semi-landmarks\n"))
        semi <- vcgSample(shortnose.mesh,SampleNum = nofl[i])
        semilong <- tps3d(semi,shortnose.lm,longnose.lm)
        tmp[i] <- system.time(relax <- relaxLM(semi,semilong, mesh=shortnose.mesh, iterations=1,SMvector=1:nrow(semi), deselect=F,surp=1:nrow(semi)))[3]
        cat(paste0("finished with ",nofl[i]," in ", tmp[i], " seconds\n")) 
    }
    return(list(timing=tmp,nofl=nofl))
}


### now install pretweaked version from github:
require(devtools)

install_github("zarquon42b/Morpho", ref="c8f3652bea901f40d93ce5efc645d2fb75b8a6da")

##run the benchmark function

old <- benchmark()
save(old,file="old")##save the results to disk


### now close the old workspace and open a new one

### get the tweaked version:
install_github("zarquon42b/Morpho", ref="ccb67d3f96d2810176490f32b0cdd0df66d51155")
new <- benchmark()
save(new,file="new")##save the results to disk

## now load timings from the old version and visualize them:
load("old")
plot(old$nofl,old$timing,col=2,cex=1.5,pch=19, xlab="no. of semi-landmarks", ylab="elapsed time in seconds")
lines(spline(old$nofl,old$timing),lwd=4,col=2)##create nice splines

load("new")#not necessary if you are still in your "new" workspace
points(new$nofl,new$timing,col=3,cex=1.5,pch=19)
lines(spline(new$nofl,new$timing),lwd=4,col=3)##create nice splines

```
Here are the graphs:
<figure>
  <img src="/resources/images/semitweak.png" alt="weak sliding routine" width="500" >
  <figcaption><b>Fig</b>.: Green: improved version; Red: old version.</figcaption>
</figure> 

Hereby the timing for 4000 semi-landmarks was 507.6 secs for the old version, compared to 33.5 secs for the tweaked version. Quite impressive, isn't it?



