# -*- coding: utf-8 -*-
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

"""
This should be rewritten to implement a more general and less
Shapely dependent way to represent geometries

https://gist.github.com/2217756

I wonder if the "geojson" package fits
the purpose or it's rather better to implement to protocol from scratch.

"""
try:
    from shapely.geometry import Point, LineString, Polygon
    from shapely.geometry import MultiPoint, MultiLineString, MultiPolygon
    from shapely.geometry.polygon import LinearRing

except ImportError:
    from pygeoif.geometry import Point, LineString, Polygon
    from pygeoif.geometry import MultiPoint, MultiLineString, MultiPolygon
    from pygeoif.geometry import LinearRing
