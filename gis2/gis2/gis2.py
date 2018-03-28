import mapnik
m = mapnik.Map(700,400)
m.background = mapnik.Color('Lime')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#9932CC')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('red'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file='SHP_Indonesia_kecamatan/INDONESIA_KEC.shp')
layer = mapnik.Layer('kecamatan')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'kecamatan.jpeg', 'jpeg')
print "rendered image to 'kecamatan.jpeg'"