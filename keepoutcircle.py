#!/usr/bin/env python

import sys
import math
import json

steps = 6
if len(sys.argv) > 1:
	steps = int(sys.argv[1])
radius = 80.0
if len(sys.argv) > 2:
	radius = float(sys.argv[2])

anglestep = math.pi / 2 / steps
points = []
for step in xrange(steps + 1):
	angle = anglestep * step
	points.append([ math.cos(angle) * radius, math.sin(angle) * radius])

polys = []
for step in xrange(steps):
	polys.append([
		[ radius, radius ],
		[ points[step][0], points[step][1] ],
		[ points[step + 1][0], points[step + 1][1] ],
	])
	polys.append([
		[ -radius, radius ],
		[ -points[step][0], points[step][1] ],
		[ -points[step + 1][0], points[step + 1][1] ],
	])
	polys.append([
		[ radius, -radius ],
		[ points[step][0], -points[step][1] ],
		[ points[step + 1][0], -points[step + 1][1] ],
	])
	polys.append([
		[ -radius, -radius ],
		[ -points[step][0], -points[step][1] ],
		[ -points[step + 1][0], -points[step + 1][1] ],
	])

print json.dumps({ "default": polys })
