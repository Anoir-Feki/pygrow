PyGrow
======

A Python project using [Django](https://www.djangoproject.com) to monitor an environment with a Raspberry Pi using a Pi Camera and DHT temperature/humidity sensor. Alerts and photo updates can be received via email or SMS.


Features
--------

- Mobile, tablet, and desktop-friendly dashboard to display overview
- Use Pi Camera for live monitoring
- Use Pi Camera for saved videos
- Use Pi Camera for saved photos
- Use Pi Camera for saved timelapses
- Use DHT temperature sensor for monitoring
- Use DHT humidity sensor for monitoring
- Store photos/videos on device
- Store sensor data in database


Usage
-----

Use Ansible to install on Raspberry Pi running [Raspbian](https://www.raspberrypi.org/downloads/raspbian) or [Ubuntu Mate](https://ubuntu-mate.org/raspberry-pi).

Ensure Pi Camera is enabled:
[https://www.raspberrypi.org/documentation/usage/camera/README.md](https://www.raspberrypi.org/documentation/usage/camera/README.md)

Test raspistill CLI tool (1 photo):
```
$ raspistill -o test-photo.jpg
```

Test raspivid CLI tool (5 second video):
```
$ raspivid -o test-video.h264 -t 10000
```


Materials
---------

Base:

- Raspberry Pi 2 Model B or 3 Model B - [link](https://smile.amazon.com/Raspberry-Pi-Model-Project-Board/dp/B00T2U7R7I)
- microSD card (Class 10 and 64 gb recommended) with [Raspbian](https://www.raspberrypi.org/downloads/raspbian) or [Ubuntu Mate](https://ubuntu-mate.org/raspberry-pi) - [link](https://smile.amazon.com/SanDisk-MicroSDHC-Standard-Packaging-SDSDQUAN-008G-G4A/dp/B00M55C0VU)
- 5V micro USB power cable - [link](https://smile.amazon.com/JBtek-Raspberry-Micro-Cable-Switch/dp/B00JU24Z3W)
- WiFi USB adapter (unless using Ethernet or Pi 3 Model B) - [link](https://smile.amazon.com/Edimax-EW-7811Un-150Mbps-Raspberry-Supports/dp/B003MTTJOY)

Peripherals:

- Raspberry Pi camera - [link](https://smile.amazon.com/gp/product/B00E1GGE40)
- DHT11 or DHT22 temperature/humidity sensor with cable - [DHT11 link](https://smile.amazon.com/uxcell-Sensitivity-Temperature-Humidity-20-90%25RH/dp/B00BXWUWRA) / [DHT22 link](https://smile.amazon.com/CHENBO-Digital-Temperature-Humidity-Sensor/dp/B014SMNBJC)


To Do
-----

- Add camera/temp/humidity status in the sidebar
- Add photo capability with raspistill
- Add timelapse capability with raspistill
- Add video capability with raspivid
- Add management for groups and permissions
- Add user accounts and logins
- Add email alerts/notifications (Django emails)
- Add SMS alerts/notifications (Twilio)
- Add scheduled photos by email
- Add temperature graph
- Add humidity graph
- Add image viewer for photos
- Add media player for videos


Author
------

Peter Schaadt

[https://github.com/peterfschaadt](https://github.com/peterfschaadt)

[http://peterschaadt.com](http://peterschaadt.com)
