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

#basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[NAME]'),'DejaVu Sans Bold',5,mapnik.Color('black'))
#basinsLabels.halo_fill = mapnik.Color('yellow')
#basinsLabels.halo_radius = 1
#r.symbols.append(basinsLabels)

#point_sym = mapnik.PointSymbolizer()
#point_sym.allow_overlap = True
#r.symbols.append(point_sym)

s.rules.append(r)

#highlight = mapnik.PolygonSymbolizer()
#highlight.fill = mapnik.Color('red')
#germany = mapnik.Rule()
#germany.filter = mapnik.Expression("[NAME]='Turkey'")
#germany.symbols.append(highlight)
#s.rules.append(germany)

#LAYER1#
m.append_style('My Style',s)
ds = mapnik.Shapefile(file='Shp Kabupaten Jawa/batas_kab.shp')
layer = mapnik.Layer('world2')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)

#LAYER2#
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('#9400D3'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style2',s)
ds = mapnik.Shapefile(file='PL jambi/PL jambi.shp')
layer = mapnik.Layer('world2')
layer.datasource = ds
layer.styles.append('My Style2')
m.layers.append(layer)

#LAYER3#
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style3',s)
ds = mapnik.Shapefile(file='SHP_Indonesia_pantai/IND_PNT_polyline.shp')
layer = mapnik.Layer('world2')
layer.datasource = ds
layer.styles.append('My Style3')
m.layers.append(layer)

#LAYER4
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('yellow'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style4',s)
ds = mapnik.Shapefile(file='SHP_Indonesia_provinsi/INDONESIA_PROP.shp')
layer = mapnik.Layer('world2')
layer.datasource = ds
layer.styles.append('My Style4')
m.layers.append(layer)

#LAYER5#
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('#FF6347'),1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style5',s)
ds = mapnik.Shapefile(file='sungai papua lengkap/sungai papua lengkap.shp')
layer = mapnik.Layer('world2')
layer.datasource = ds
layer.styles.append('My Style5')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m,'world2.pdf', 'pdf')
print "rendered image to 'world3.png'"