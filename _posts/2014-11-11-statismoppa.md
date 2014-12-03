---
layout: post
tags: 
- statismo 

date: 2014-11-11 10:05:00 +0200
title: Statismo&#58; install statismo from PPA for Ubuntu 14.04 and 14.10
---
UPDATE: now also available for Ubuntu 14.10

Inspired by Arnaud's effort to package [statismo for Mac](https://groups.google.com/d/msg/statismo-users/6awZIpduiZI/H3fTSkYu2XcJ), I packaged statismo (0.10.1) for Ubuntu and uploaded it to my [PPA](https://launchpad.net/~zarquon42/+archive/ubuntu/ppa). At the moment I only packaged for Ubuntu 14.04 and 14.10 but if you need it for a different version, drop me a line in the comment section.
Users of Ubuntu 14.04 and 14.10 can install it by issuing the following command in a terminal:


```bash
sudo apt-add-repository ppa:zarquon42/ppa
sudo apt-get update
sudo apt-get install statismo

```