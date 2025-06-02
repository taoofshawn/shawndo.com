---
title: Flow Profiling Modification – Part 01
author: shawndo
type: post
date: 2016-06-25T19:09:23+00:00
url: /2016/06/25/flow-profiling-modification-part-01
tags:
  - Espresso

---
This is to document my effort to add a flow profiling modification to my espresso machine. Most of what I’ll be doing is learning about this stuff, since I barely know what a “solenoid” is. I was trying to figure out the best place to save this info when I remembered that I had a blog somewhere..  
There will be some learning involved here, so this is definitely not the recording of an expert. A goal is to have a simple list of parts for anyone to be able to reproduce this on their own machine.

I got a basic design from an espresso ibuddy which is the same way a [Slayer espresso][1] machine achieves this flow control.

![](/images/2016/06/flow-restrict-drawing.jpg)

This is connected between the line-out of the water pump and the line-in of the brew group (where the coffee is brewed)

The idea is that if the solenoid valve is closed, the water will be forced through the needle valve, which will restrict the water flow. After some amount of time, the solenoid valve will be opened and the water will be routed through the other path and continue brewing the coffee at full flow.

The design is simple and this is mainly a detail-oriented effort of finding all the right parts. Parts that will fit to each other and be powered properly, electricity-wise. 

I plan to do this is 2 phases. First phase is proof-of-concept where I will do everything in plastic and power externally. Once I prove that it works and produces the desired effect, the second phase will be to power it using the internal espresso machine power supply and replace the tubing with brass.

Proof of concept  
1. Figure out the size of the tubing to connect to the pump and brew group  
2. purchase the polypropene tubing and compression fittings  
3. find the right needle valve with the right fittings. Probably a [Swagelok][2] brass metering valve.  
4. find the right solenoid valve with the right fittings and voltage. Probably a [Parker][3] 110v, normally open, brass  
5. Get a switch and power supply for the solenoid  
6. Figure out some purple blinky LED thing to activate when the solenoid is active.

 [1]: https://prima-coffee.com/equipment/slayer/single-group
 [2]: http://www.swagelok.com/en/catalog/Valves/Metering
 [3]: http://ph.parker.com/us/en/solenoid-fluid-control-valves