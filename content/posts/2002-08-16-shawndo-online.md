---
title: shawndo online
author: shawndo
date: 2002-08-16T00:00:00+00:00
url: /2002/08/16/shawndo-online
tags:
  - Journal

---
Finally got internet at home. Pretty fast, i got the 2 login 1.5mbit connection. Faster than advertised so far, since the network is still pretty new and underused. The installer said only about 15% of the bandwidth is being used right now. the irksome thing is that its setup with PPPoE. I guess this is common with DSL. I compiled my linux kernel a LONG time ago, and got it just right after several days of messin with settings. So I forgot to set up PPP support, which apparently is required for PPPoE. Now, I can either try and remember all those settings and add PPP support, or wimp out and get a DSL router. So I broke down and got a DSL router, but I'm justifying it to myself because it also has the wireless capability so I can use my laptop anywhere. So now, I can phase out my faithfull 5x86 "Jeddah" but I don't wanna! Without doing ipchains, it's only task will be to handle login accounts and SSH, which can easily be handled by my dual-933 fileserver. I guess I can claim "security" and keep it seperate. I guess I'll use the extra NIC in there for another 2 port Etherchannel for no good reason.