import arcpy
import os
import zipfile

# Workspace and datasets
arcpy.env.workspace = "C:/Lessons/PythonTool/DC.gdb"  # Geodatabase where feature classes to be clipped reside
clip_fc = "C:/Lessons/PythonTool/neighborhood.shp"    # Full path of clip polygons
gdb = "C:/Lessons/PythonTool/Clip.gdb"                # Full path of output geodatabase
gdb_path, new_gdb = os.path.split(gdb)                # Split full path for output gdb into folder and gdb name
out_zip = "C:/Lessons/PythonTool/Clip.zip"            # Full path of the output ZIP archive

# Create a new geodatabase to store the result
arcpy.CreateFileGDB_management(gdb_path, new_gdb)
print(f"Output geodatabase {gdb} created")
    
# Clip each input feature class
inputs = arcpy.ListFeatureClasses()
print(inputs)
for fc in inputs:
    fc_name = arcpy.da.Describe(fc)["baseName"]       # Remove folder and any file extensions from full path
    new_fc = os.path.join(gdb, fc_name)               # Create full path for output feature class
    arcpy.analysis.Clip(fc, clip_fc, new_fc)
    print(f"Output feature class {new_fc} created")
        
# Create a ZIP file for the new geodatabase
with zipfile.ZipFile(out_zip, "w") as myzip:
    for f in os.listdir(gdb):                         # Iterate over all the files in the geodatabase folder
        if not f.endswith(".lock"):                   # Skips any files with .lock extension
            file_name = os.path.join(gdb, f)          # Original file name with full path
            arc_name = os.path.join(new_gdb, f)       # Archive name with gdb name only
            myzip.write(file_name, arc_name)          # Write original file to new geodatabase
