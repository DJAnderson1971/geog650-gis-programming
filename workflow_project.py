# Author: David J. Anderson
# Date: 1 March 2025
# Purpose: This script reads all the feature classes in a geodatabase and copies them to a new feature dataset in a new geodatabase.
# Feature classes not already in the target coordinate system are projected.

# Import Libraries and generate user output when each import is complete
import arcpy
import os
print("arcpy and the os have loaded properly.")

# Set the work environment for the script to run in
mypath = "C:/Lessons/PythonWorkflow"
gdb = "Transportation.gdb"
arcpy.env.workspace = os.path.join(mypath, gdb)
arcpy.env.overwriteOutput = True

# Set variable names for a new gdb and a new network
new_gdb = "Metro_Transport.gdb"
fds = "Metro_Network"

# Create the new gdb
new_gdb_path = arcpy.CreateFileGDB_management(mypath, new_gdb)
# Provide output that the gdb has been created
print(f"The geodatabase {new_gdb} has been created.")

# Create a new feature dataset for the new gdb and provide feedback that it has been created with the desired spatial reference (WKID ####)
arcpy.CreateFeatureDataset_management(new_gdb_path, fds, 2248)
print(f"The feature dataset {fds} has been created.")

# Create an interable list to return descriptions of feature classes in the project
# Create a list of feature classes
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    desc = arcpy.da.Describe(fc)
    sr = desc["spatialReference"]
    new_fc = os.path.join(mypath, new_gdb, fds, fc)
    # Check to see if the spatial reference is the desired WKID
    if sr.factoryCode == 2248:
        # Copy members of the feature class which are the desired WKID into the new fds
        arcpy.CopyFeatures_management(fc, new_fc)
        print(f"The feature class {fc} has been copied.")
    else:
       # Project members of the feature class which are not the desired WKID into the correct WKID and copy them to the new fds
        arcpy.Project_management(fc, new_fc, 2248)
        print(f"The feature class {fc} has been projected.")