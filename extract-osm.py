import os               # Files and folder manipulations
import shapefile        # Shapefile manipulations

sf = shapefile.Reader("resources/OSM/communes-20160119.shp")

fields = sf.fields

#print(fields)

records = sf.records()
records = sorted(records)

output = ""
for r in records:
    output += '"{}" ; "{}" ; "{}"\n'.format(r[0], r[1], r[2])

if len(output):
    file = 'resources/OSM/extract-osm.csv'
    with open(file,"w") as f:
        f.write(output)
        f.close()