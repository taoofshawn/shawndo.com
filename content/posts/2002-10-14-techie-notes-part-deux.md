---
title: 'Techie Notes: part deux'
author: shawndo
type: post
date: 2002-10-14T00:00:00+00:00
url: /2002/10/14/techie-notes-part-deux
tags:
  - Journal

---
Almost nothing goes according to plan. Well, the Sparc project went fine. I borrowed a SUN keyboard and mouse to do all the network card stuff, and I did that in 10 minutes. No problem. The hard drives are a different story. First of all, I tried all the GRUB hd numbers up to 7, and I couldn't find something that worked. I could have tried some other stuff, but I backed up all the conf files I needed, and I wanted to give the LVM in RH 8.0 a try. So screw it, I decide to just reinstall the OS. To recap, I have:  
  
- 1x 9gB ultra160 scsi drive  
- 2x 75 gB IDE's  
- 2x 120 gB IDE's  
  
Since I have 4 IDE's and am too lazy to pull out my scsi cdrom from my other box, I need to install over the network. Took me a while before I found that the http method through my workstation was the best way. I set up the partitions and all that, checked for bad blocks. I then found that one of my 75 giggers is bad! Weird clicks comin out of it and all that. I could have made the partitions around the bad portions, but it's still under warranty, so I decide to plug in an old 20 gigger in its space. So now, for IDE space, I got about 320 gigs. That should hold me until the bad 75'er comes back. Doing that bad block test on a 120 gig drive takes forEVER!. not to mention 2 of them plus a couple 75'ers. So, I left the installation chuggin away while I'm at work. see what happens in a few hours.