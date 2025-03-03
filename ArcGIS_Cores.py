# Import Libraries and generate user output when each import is complete
import arcpy
print("arcpy has loaded properly.")

# Set the numbers of CPU cores ArcGIS Pro is allowed to use to 50%
arcpy.env.parallelProcessingFactor = "50%"