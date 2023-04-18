---
layout: page
toc: false
title: Networking Tools
slug: networking-tools
type: networking
order: 2
---

## Lecture Video
On June 9, 2021 Prof Lundrigan discussed some common networking tools. The video is embedded below. 

<iframe width="800" height="500" allow="fullscreen" src="https://www.youtube.com/embed/r-z62olDMQM"> </iframe>

### Timestamps

[0:00](https://www.youtube.com/watch?v=r-z62olDMQM&t=0s) Introduction<br>
[1:19](https://www.youtube.com/watch?v=r-z62olDMQM&t=79s) ifconfig and ip address<br>
[6:59](https://www.youtube.com/watch?v=r-z62olDMQM&t=419s) ping<br>
[10:34](https://www.youtube.com/watch?v=r-z62olDMQM&t=634s) dig and nslookup<br>
[16:18](https://www.youtube.com/watch?v=r-z62olDMQM&t=978s) traceroute<br>
[21:05](https://www.youtube.com/watch?v=r-z62olDMQM&t=1265s) curl/wget/httpie<br>
[30:04](https://www.youtube.com/watch?v=r-z62olDMQM&t=1804s) arp<br>
[31:53](https://www.youtube.com/watch?v=r-z62olDMQM&t=1913s) nmap<br>
[37:28](https://www.youtube.com/watch?v=r-z62olDMQM&t=2248s) nc<br>
[40:38](https://www.youtube.com/watch?v=r-z62olDMQM&t=2438s) tcpdump/wireshark/tshark<br>
[52:06](https://www.youtube.com/watch?v=r-z62olDMQM&t=3126s) Wrap-up

## Tools

- [ifconfig](https://linux.die.net/man/8/ifconfig) or [ip](https://linux.die.net/man/8/ip)
  - Shows information about your computer's networking interfaces (e.g., MAC address, IP address).

- [ping](https://linux.die.net/man/8/ping)
  - Sends small message to a computer. Helpful to see if a computer is connected and the latency between computers.

- [dig](https://linux.die.net/man/1/dig) or [nslookup](https://linux.die.net/man/1/nslookup)
  - Run a DNS lookup.

- [traceroute](https://linux.die.net/man/8/traceroute)
  - List all routers between computers.

- [curl](https://curl.se)
  - Make HTTP request. By default the output is displayed in the terminal.

- [wget](https://www.gnu.org/software/wget/)
  - Make an HTTP request. By default the output is downloaded as a file.

- [httpie](https://httpie.io)
  - Better version of curl.

- [arp](https://www.man7.org/linux/man-pages/man8/arp.8.html)
  - Do an ARP lookup.

- [nmap](https://nmap.org)
  - Networking multi-tool. Typically used for penetration testing.

- [netcat (nc)](http://netcat.sourceforge.net)
  - Create a simple TCP or UDP server/client. 

- [tcpdump](https://www.tcpdump.org)
  - Trace all packets that are incoming or outgoing on your computer.

- [wireshark](https://www.wireshark.org)
  - Better than tcpdump with a graphical interface.

- [tshark](https://www.wireshark.org/docs/man-pages/tshark.html)
  - Terminal version of Wireshark.
