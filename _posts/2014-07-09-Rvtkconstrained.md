---
layout: post
tag: RvtkStatismo R
date: 2014-07-09 15:25:00 +0200
title: RvtkStatismo - constrained model
---

Today I implemented methods for constraining models using statismo: at the moment these are ```statismoConstrainModel``` and ```statismoConstrainModelSafe```. The latter evaluates the point pairings and only uses those pairs that are within a definable probability range. This is done using the Mahalanobisdistance and its connection to the χ²-distribution.