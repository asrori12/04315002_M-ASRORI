import mapnik
m = mapnik.Map(1280,720)
m.background = mapnik.Color('#86fff2')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('white')
r.symbols.append(polygon_symbolizer)


line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
line_symbolizer.stroke_width =  10.0

r.symbols.append(line_symbolizer)

s = mapnik.Style()
r = mapnik.Rule()

point_sym = mapnik.MarkersSymbolizer()
point_sym.filename = "image/pantai.png"
point_sym.width	= mapnik.Expression("20")
point_sym.height = mapnik.Expression("20")
point_sym.allow_overlap = True
r.symbols.append(point_sym)


text_sym = mapnik.TextSymbolizer(mapnik.Expression('[NAME]'), 'DejaVu Sans Bold',8,mapnik.Color('black'))
#basinsLabels.halo_fill = mapnik.Color('yellow')
text_sym.halo_radius = 1
text_sym.allow_overlap = True
text_sym.allow_edges = False
r.symbols.append(text_sym)

point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap= True
r.symbols.append(point_sym)


s.rules.append(r)
m.append_style("kenpark point", s)

ds = mapnik.MemoryDatasource()
f = mapnik.Feature(mapnik.Context(), 1)
f["NAME"] = "KENJERAN PARK SURABAYA"
f.add_geometries_from_wkt("POINT(-7.2162706 112.7543832)")
ds.add_feature(f)

player = mapnik.Layer("kenpark_layer")
player.datasource = ds
player.styles.append("kenpark point")
m.layers.append(player)

m.append_style('My Style',s)
ds = mapnik.Shapefile(file="shp1/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)

m.zoom_all()
mapnik.render_to_file(m, 'kenjpark_point.pdf', 'pdf')
print "rendered image to 'kenjpark_point.png' "
