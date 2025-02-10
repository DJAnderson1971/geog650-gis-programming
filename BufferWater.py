# Import Libraries and generate user output when each import is complete
import arcpy
print("arcpy has loaded properly.")

# Set up geoprocessing environment
arcpy.env.workspace = r"C:\EsriTraining\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True

# Create a list of feature classes in the SanJuan.gdb
fcList = arcpy.ListFeatureClasses()
# Verify fcList is complete
print("fcList is built")

# Create a loop to buffer Lakes and Streams
bufferList = []
for fc in fcList:
    if fc == "Lakes" or fc == "Streams":
        arcpy.Buffer_analysis(fc, fc + "Buffer", "1000 meters", "FULL", "ROUND", "ALL")
        bufferList.append(fc + "Buffer")
# Verify Lakes and Streams Buffers have been created
print ("LakesBuffer and StreamsBuffer created successfully")

# Create Union Buffer Polygons
arcpy.Union_analysis(bufferList, "WaterBuffers")
#Verify WaterBuffers has been created
print("WatersBuffer has been successfully created")