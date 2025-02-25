# Create a variable for the current ArcGIS Project
p = arcpy.mp.ArcGISProject('CURRENT')

# Create a variable for the current map layer in the ArcGIS Projecct
m = p.activeMap

# Create a new variable to list the layers in the current map
lyr = m.listLayers("Ward 6 Requests")[0]

# Modify the Definition Query for the Ward 6 Requests Layer to find potholes
lyr.definitionQuery = "SERVICEC_1 = 'Pothole'"