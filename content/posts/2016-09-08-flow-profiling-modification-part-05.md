---
title: Flow Profiling Modification – Part 05
author: shawndo
date: 2016-09-09T02:16:24+00:00
url: /2016/09/08/flow-profiling-modification-part-05
tags:
  - Espresso

---
A lull in this project.  
The next step was to get an appropriate solenoid valve to replace the ball valve in the current installation. Unfortunately my one-stop shop (Swagelok) doesn't make those and based on [this post][1], I figured Parker solenoids were the way to go. If it's good enough for Kees..

Finding a new retailer on top of choosing the right electricity parameters and flow factor stuff formed a speedbump. Also, I am able to pull the pre-brew style shots with the ball valve so I didn't feel a rush, but the machine is open and in the middle of the bar. I'll need to finish this before it gets closed and returned to the the corner. 

![](/images/2016/09/solenoid_01.jpg)

I finally decided on matching what most other espresso machines have and just getting a 110V AC solenoid valve. I knew I wanted a normally open "NO" type. This means that without any electricity it is open and allows water through. When you energize it with a switch, it will close.  
I found a local vendor and got a few options. Various trade-offs, including flow factor, size, seals and lead time. I told them it was for an espresso machine and they chose food-safe seals. I ended up going with a "miniature" model, which isn't really all _that_ miniature, but has a very low flow factor. '.06 Cv". It also has a weird 90 degree turn. The inlet is perpendicular to the outlet. I thought this would work for me and I could make my assembly smaller since I had to put in a bunch of pipe turns to accommodate the straight ball valve.  
I did [the math][2] based on numbers from [this La Marzocco doc][3]. I know that have a .6mm ruby flow restrictor. I compared it to the flow I actually get and its all pretty close. I tried the equation with different numbers based on various pressure ranges I might use during a shot and different flow restrictors I may have in the future (if I decided to change to a .8mm for example) None of those numbers went above .02, so .06 should be enough for me. 

So bottom line, I got part number 20CF02EV4C4F. One thing I noticed, after the fact, is they make at least 3 types of coil connection types.  

![](/images/2016/09/solenoid_02.png)

I got one that is intended to connect the wiring through conduit pipe. It will work, but will look kind of lame. I should have got the DIN model, which would allow me to just connect the cabling using spade connectors. The DIN model will have a slightly different model number. Like instead of 4C4 at the end it will be 4D6 or something. (I'm guessing from reading the manual) If I actually have to buy another solenoid in the future, I'll double check that before purchasing. Also, not 100% sure you can use spade connectors to connect to the DIN terminals.  

**Update, DIN terminals are not compatible with spade/disconnect terminals. The right model to get is either one with wires coming out and just crimp your own disconnects to it.

Next steps are
- mock up where this will go in the current assembly  
- remove the assembly from the espresso machine and redo any tubing/connectors to hook this guy up.

I'm going to hook this up to the electricity coming out of the power switch on the espresso machine, but I still need to figure out what kind of connecters I'll need so I can order some T-cabling and hook this up all proper-like.

 [1]: http://www.home-barista.com/espresso-machines/solenoid-brands-and-reliability-t17077.html
 [2]: https://en.wikipedia.org/wiki/Flow_coefficient
 [3]: http://www.lamarzoccousa.com/wp-content/uploads/2014/07/TB-95-Flow-Restrictor-Guide.docx