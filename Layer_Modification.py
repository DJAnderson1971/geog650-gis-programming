# Create a variable for the current ArcGIS Project
p = arcpy.mp.ArcGISProject('CURRENT')
p
# Create a variable for the current map layer in the ArcGIS Projecct
m = p.activeMap
# Print the name of the active map
m.name
# Create a new variable to list the layers in the current map
lyr = m.listLayers("Recycling Cart Delivery")[0]
# Print the name of the layer
lyr.name
# Create a new variable to list the layers in the current map
lyr = m.listLayers("Recycling Cart Delivery")[0]
# Turn off the visibility of a layer in Python
lyr.visible = False
# Print whether the layer is visible or not
lyr.visible
