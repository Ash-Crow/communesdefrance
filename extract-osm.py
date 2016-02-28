import os               # Files and folder manipulations
import shapefile        # Shapefile manipulations

sf = shapefile.Reader("resources/OSM/communes-20160119.shp")

records = sf.records()
records = sorted(records)

def writecsv(text, file):
    if len(text):
        with open(file,"w") as f:
            f.write(text)
            f.close()

output = ""
errors = ""
for r in records:
    output += '"{}" ; "{}" ; "{}"\n'.format(r[0], r[1], r[2])
    if r[2].strip == '':
        output += '"{}" ; "{}"\n'.format(r[0], r[1])

writecsv(output, 'resources/OSM/extract-osm.csv')
writecsv(output, 'resources/OSM/extract-osm-missing-wikipedia-articles.csv')