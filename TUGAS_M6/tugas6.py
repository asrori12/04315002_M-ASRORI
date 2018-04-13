import mapnik
m = mapnik.Map(500,250)
m.background = mapnik.Color('#40E0D0')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#7FFF00')
r.symbols.append(polygon_symbolizer)

#line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('#B22222'),1)
#line_symbolizer.stroke_width = 0.5

r.symbols.append(line_symbolizer)

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[nama]'),'DejaVu Sans Bold',5,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius = 1
r.symbols.append(basinsLabels)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)

s.rules.append(r)

#highlight = mapnik.PolygonSymbolizer()
#highlight.fill = mapnik.Color('red')
#germany = mapnik.Rule()
#germany.filter = mapnik.Expression("[NAME]='Turkey'")
#germany.symbols.append(highlight)
#s.rules.append(germany)

#LAYER1#
m.append_style('My Style',s)
ds = mapnik.Shapefile(file='tugas6.shp')
layer = mapnik.Layer('world2')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m,'world2.pdf', 'pdf')
print "rendered image to 'world2.png'"