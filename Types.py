#Useful lists
MateTypes = ["One Point", "Two Point", "Uniform", "Partialy Matched", "UniformPartialy Matched",
"Ordered", "Blend"  ]

inputFormats = "ESRI Shapefile|*.shp|GeoJSON|*.geojson|GML|*.gml|KML|*.kml|Microstation DGN|*.dgn|ESRI FileGDB|*.gdb|Atlas BNA|*.bna"

outputFormats = "ESRI Shapefile|*.shp|GeoJSON|*.geojson|GML|*.gml|KML|*.kml|Comma Separated Value (.csv)|*.csv|Atlas BNA|*.bna"

drivers = {".shp": "ESRI Shapefile",".geojson":"GeoJSON", ".gml":"GML", ".kml":"KML", ".dgn":"Microstation DGN"
, ".gdb":"ESRI FileGDB", ".bna":"Atlas BNA", ".csv":"Comma Separated Value (.csv)"}