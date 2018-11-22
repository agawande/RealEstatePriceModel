import json
from shapely.geometry import Polygon

with open('output.json') as f:
    data = json.load(f)

f.close()

housingData = data['Planning_Cadastre.PARCEL_POLYGON_CAMP']['features']

output = open("crittenden.csv", "w")

head="propertyShape,latitude,longitude,gid,srce_date,ow_src_dat,cty,state,zip,type,assess_val,\
imp_val,land_val,total_val,assess_dat,schl_code,acre_area,calc_acre"

output.write(head)
output.write("\n")

for line in housingData:
    csvLine = ""
    # Shape of the property - Polygon or MultiPolygon
    propertyShape = line['geometry']['type']
    if propertyShape == 'GeometryCollection' or propertyShape == "MultiPolygon":
        continue
    # Coordinates of the polygon, todo: calculate median
    # One idea is to classify the shape of the house as another feature?
    # Can play around with Shapely polygon to get differences from school etc.:
    # http://toblerity.org/shapely/shapely.geometry.html
    coordinates = line['geometry']['coordinates']
    centroid = Polygon(coordinates[0]).centroid
    latitude = centroid.y
    longitude = centroid.x
    # GID
    gid = line['properties']['gid']
    # Geometry Source Date
    srce_date = line['properties']['srce_date']
    # Owner Source Date
    ow_src_dat = line['properties']['ow_src_dat']
    city = line['properties']['ph_cty_nm']
    state = line['properties']['ph_st_nm']
    zip = line['properties']['ph_zip']
    # Parcel Type Code
    # CV: Commercial Vacant, AM: Agriculture Miscellaneous, RI: Residential Improved, MN: Minerals, IM: Industrial Miscellaneous
    # RV: Residential Vacant, VP: Voided Parcel, IG: Industrial Agriculture Improved
    # CT: Commercial Transitional, IV: Industrial Vacant, PS: Public Service Commission, II: Industrial Improved,
    # CE: Commercial Excess, CA: Commercial Agriculture Vacant, IA: Industrial Agriculture Vacant,
    # CI: Commercial Improved, CR: Commercial Residential, AB: Agriculture Building, RB: Residential Building Only,
    # IO: Improvement Only, CB: Commercial Building Only, CM: Commercial Miscellaneous, EC: Exempt Commercial,
    # RM: Residential Miscellaneous, RC: Reference Card, CG: Commercial Miscellaneous, AV: Agriculture Vacant,
    # CP: Commercial Mobile Home Park, EX: Exempt, AI: Agriculture Improved, MH: Mobile Home Only
    type = line['properties']['type']
    # Assessed Value
    assess_val = line['properties']['assess_val']
    # Improved Value
    imp_val = line['properties']['imp_val']
    # Land Value
    land_val = line['properties']['land_val']
    # Total Value
    total_val = line['properties']['total_val']
    # Assessed Date
    assess_dat = line['properties']['assess_dat']
    # School Code
    schl_code = line['properties']['schl_code']
    # Acre Area as listed in CAMA, Computer Assisted Mass Appraisal
    acre_area = line['properties']['acre_area']
    # Calculated Acreage
    calc_acre = line['properties']['calc_acre']
    # Begin Date, column to determine the age of the data for a given county
    # begin_date
    # edit_date, Date data was updated in GeoStor
    csvLine = "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(propertyShape,latitude,longitude,gid,\
              srce_date,ow_src_dat,city,state,zip,type,assess_val,imp_val,land_val,total_val,assess_dat,schl_code,\
              acre_area,calc_acre)
    output.write(csvLine)
    output.write("\n")

output.close()
