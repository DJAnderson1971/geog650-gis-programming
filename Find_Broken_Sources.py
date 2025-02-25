

# Create a variable for the current ArcGIS Project
aprx = arcpy.mp.ArcGISProject('CURRENT')

# Create a variable to store a list of all broken data sources at the project level
brkn = aprx.listBrokenDataSources()

# Print the list of broken data sources in the project
print (brkn)

# Check for broken data sources on the Streets map
m = aprx.listMaps("Streets")[0]

# Create a variable to store a list of all broken data sources Streets map
mbrkn = aprx.listBrokenDataSources()

# Print the list of broken data sources in the project
print (mbrkn)

# Find the layers with broken data sources in the Streets Map
# Create a variable to hold a list of the layers in the map
lyrs = m.listLayers()

# Iterate through the layers to identify which ones are broken and which are not
for l in lyrs: 
   if l.isBroken: 
        print("(BROKEN)" + l.name) 
   else: 
       print(" " + l.name)

# Expand the search for broken data sources to all maps with all layers in the maps
# Change the variable m to be part of the aprx.listMaps iteration and iterate through the list
for m in aprx.listMaps(): 
    
    # Print the lit of maps
    print("Map:{0}".format(m.name))
    
    # Create the variable lyr and iterate through the list of layers in all maps which are broken
    for lyr in m.listLayers(): 
        if lyr.isBroken: 
            # Print the layers in the maps which have broken data sources
            print("(BROKEN)" + lyr.name)
            