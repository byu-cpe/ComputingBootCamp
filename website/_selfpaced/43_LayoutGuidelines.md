---
layout: page
toc: true
title: Layout Guidelines
slug: layoutGuidelines
type: PCB
order: 4
---


# General guidelines for board layout

  * Before routing, finalize schematic review and organize all components. Reorganizing or adding additional parts is much more different after routing has begun.
  * Power and ground traces should be thick (as thick as vias or pads, whichever is thinner) - it often helps to do these last.
    * Note that Altium displays connection lines (called rats nest) between nets that need to be routed, but the lines for power and ground will change depending one which power/ground pads are nearest at any given time. Routing these last helps the engineer see how to route these to the pads that make the most sense rather than just the pads in the nearest vicinity. Also note that if you are connecting power/ground connections to a plane instead of to each other via traces, you can ignore the connection lines for these nets altogether.
  * For planes and polygon pours, avoid skinny juts or paths - this reduces the chances for current to travel/accumulate where you don't want it.
  * Every ground connection should have its own via - this provides a clear return path for each ground connection, reducing chances for current to travel where you don't want it. This is also true to power connections.
  * Be aware of how far apart capacitors/resistors are from each other - you want to be able to fit tweezers in between them.
  * You can rotate parts if it makes less of a tangle for routing. As you do so, note that you can ignore the connection lines for any nets you will be connecting to a plane (such as ground and/or power).
  * Altium has an "UnRouted Net" rule in the Design Rules. The check box for "Check for incomplete connections" is unchecked by default. Be sure to check this box so that incomplete connections will be flagged when you run a Design Rule Check.
  * Review Altium's default design rules and make changes as desired. Always run a Design Rule Check (found in the Tools dropdown menu) and ensure that all violated rules are either fixed or acceptable as is before considering your layout complete.
  * Sometimes it is bad to route signals under parts. Avoid that when you can; if you must route signals under parts, be aware what parts they are and ensure that doing so will not interfere with anything. This is only relevant if the trace you are routing is on the same layer as the part you are routing under. On different layers you do not need to worry about this.
  * Do not use blind, or in pad vias if possible. They will greatly increase the cost of the board. 
  * There should be a ground layer/place for each different voltage plane. The organization of the layers depends on the desired function of the board. For large amount of high speed differential signals signal layers should alternate with power planes. 
  * With 2 layer boards polygon pours can be used for power and ground "planes"
  * It is important to consider the orientation of connectors, make sure that they are accessible where they are placed on the board and that they are rotated correctly
  * When IC chips have large GND pads they can typically be filled by several GND vias. 
  * When routing BGA (Ball grid array) such as an FPGA, it is important to do "fan out" or spread each connection as much as possible before routing in order to ensure that there is enough place for vias in between each connection.
  * If there is any uncertainty of specific measurements (trace width, copper weight, etc.) check with the PCB manufacturer to see what their tools' minimum requirements are. 
  * Additional information can be found [here](https://resources.altium.com/p/top-5-pcb-design-guidelines-every-pcb-designer-needs-know).
