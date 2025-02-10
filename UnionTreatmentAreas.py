# Import Libraries and generate user output when each import is complete
import arcpy
print("arcpy has loaded properly.")

# Set up geoprocessing environment
arcpy.env.workspace = r"C:\EsriTraining\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True

# Create a list of treatment area feature classes
treatmentList = ["RoadBuffers", "WaterBuffers"]
# Verify treatmentList is complete
print("treatmentList is built")

# Create a Union_analysis of the items in treatmentList
arcpy.Union_analysis(treatmentList, "NonChemical")
#Verify NonChemical has been created
print("NonChemical has been successfully created")