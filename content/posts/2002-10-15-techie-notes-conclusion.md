---
title: 'Techie notes: Conclusion'
author: shawndo
type: post
date: 2002-10-15T00:00:00+00:00
url: /2002/10/15/techie-notes-conclusion
categories:
  - Journal

---
All that stuff I was talkin about yesterday, GRUB and the order numbers, etc, almost all a bunch of crap. After trying out my theory, failing, re-installing RedHat a few times, failing, I realized what I did. "Had I known" I coulda fixed it in the beginning without going through all this crap. I said "almost" because I did have to change the grub.conf to hd4. The extra IDE drive did cause the device.map to change. But even that didn't work. The issue was that I was installing the bootloader on the MBR, as I have been doing for years. For some reason that I can't think of, MBR is an IDE-only deal. It was putting the bootloader on the first IDE drive, but I was telling the bios to boot of the SCSI drive. I could have either installed the bootload on the SCSI drive, or (which I ended up doing) is tell the bios to boot off the first IDE drive, which redirected to the SCSI. All is good now. Packed up my 75 gigger for an RMA. Enjoying 320 gigs in my /pub filesystem (trying out that snazzy ext3 thing). Running a massive restore right now, and all is looking good so far (24 hours into the restore). I gotta alot-O-crap, and an old DLT library. Even then, backups kick ass!