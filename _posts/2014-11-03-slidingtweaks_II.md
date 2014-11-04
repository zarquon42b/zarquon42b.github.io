---
layout: post
tags: 
- R 
- Morpho 

date: 2014-11-03 10:05:00 +0200
title: Benchmarking continued&#58; sliding performance using different BLAS implementations
---

Out of couriosity on how far I could tweak the performance of the sliding of semi-landmarks I also ran the benchmarks using different BLAS  (Basic Linear Algebra Subprograms) implementations:


 * [ATLAS](http://math-atlas.sourceforge.net/)
 * [OpenBLAS](https://github.com/xianyi/OpenBLAS)

**Hardware specs:** 

* **CPU**: Intel(R) Xeon(R) CPU E5-1650 v2 @ 3.50GHz (Hexacore)
* **RAM**: 32GB DDR3 @1600 MHz

**Software:**

* Ubuntu 14.04.1
* R 3.1.2

ATLAS was installed using the source package provided by Ubuntu and using the following commands to download and compile and build debian packages:

```bash
apt-get source atlas
cd atlas-3.10.1/
fakeroot debian/rules custom
``` 

OpenBLAS was simply downloaded from [https://github.com/xianyi/OpenBLAS](https://github.com/xianyi/OpenBLAS) and compiled using the default options. 

Now, one can switch between BLAS versions using ```update-alternatives```.

And the winner is....


OpenBLAS, beating ATLAS at 4000 semi-landmarks by impressive 12.2 seconds:


<figure>
  <img src="/resources/images/BLAScompare.png" alt="performance of sliding routine" width="500" >
  <figcaption><b>Fig. 1: </b>Blue: OpenBLAS, Green: ATLAS.</figcaption>
</figure> 









