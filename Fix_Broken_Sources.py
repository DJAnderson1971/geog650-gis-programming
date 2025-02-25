# Import libraries needed to execute the code
import arcpy, pprint

# Create a variable for the current ArcGIS Project
aprx = arcpy.mp.ArcGISProject("CURRENT")

# Update connection properties for the entire project
aprx.updateConnectionProperties(current_connection_info = "DDOT_Test",
                             new_connection_info = "DDOT_Prod")

# Find and list any broken data sources

# Create a variable and list all maps in the project
for m in aprx.listMaps(): 
   
    #print each map by name
    print("Map:{0}".format(m.name)) 
   
    #loop through each map and list its layers
    for lyr in m.listLayers(): 
       
        #check the layer's data source
        if lyr.isBroken: 
           
            #if the layer's data source is broken, print BROKEN
            print("(BROKEN)" + lyr.name) 
        else:
            print(""+lyr.name)

# Print the connection properties dictionary

# Limit m to only the Transit layer since it is known to still be problematic
m = aprx.listMaps("Transit")[0]

# Limit lyr to only be in the BicycleLanes_DC layer since it is still known to be problematic
lyr = m.listLayers("BicycleLanes_DC")[0]

# Print out the connection properties for the BicycleLanes_DC layer
pprint.pprint(lyr.connectionProperties)

# Change the connection properties to match the new DOTT_Prod database
old_cp = {'connection_info': {'database': 'C:\\EsriTraining\\PythonDataFix\\DDOT_Test.gdb'},
                'dataset': 'BicycleLanes_DC',
                'workspace_factory': 'File Geodatabase'}  
new_cp = {'connection_info': {'database': 'C:\\EsriTraining\\PythonDataFix\\DDOT_Prod.gdb'},
                'dataset': 'BicycleLanes_DC',
                'workspace_factory': 'File Geodatabase'}