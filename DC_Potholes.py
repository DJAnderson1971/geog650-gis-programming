# Create a variable for the current ArcGIS Project
p = arcpy.mp.ArcGISProject('CURRENT')

# Create a variable for the current map layer in the ArcGIS Projecct
m = p.activeMap

# Create a layer list of all the layers in the current map
lyrList = m.listLayers()

# Iterate through the list to see which layers are feature layers
for lyr in lyrList:
    if lyr.isFeatureLayer:
        #Print the names of all feature layers
        print(lyr.name)
        # Set the definition query to find potholes in all feature layers
        lyr.definitionQuery = "SERVICEC_1 = 'Pothole'"