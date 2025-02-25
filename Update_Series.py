# Create a variable for the current ArcGIS Project
aprx = arcpy.mp.ArcGISProject("CURRENT")

# Create a variable for the Service Request Layout
lyt = aprx.listLayouts("Service Requests Layout")[0]

# Create a variable for the map series
ms = lyt.mapSeries

# Verify that the map series is enabled
ms.enabled

#Display the page count for the map series
ms.pageCount

# Set a variable for the maps
m = aprx.listMaps("Service*")[0]

# Set a variable for the map layers
lyr = m.listLayers("Service*")[0]

# Set a definition query to only show items later than the add date of 2022-05-06
lyr.definitionQuery = "ADDDATE > date '2022-05-06'"

# Refresh the map series
ms.refresh()

# Set the map series for export to .pdf in a specified file location with a specified file name
ms.exportToPDF(r"C:\EsriTraining\PythonMapSeries\PHRepairs.pdf")

# Set up a print for only those pages changed with Ward 2 boundary updates were made
ms.exportToPDF(r"C:\EsriTraining\PythonMapSeries\PHRepairs.pdf", "RANGE", ("1,2,5-8"), "PDF_MULTIPLE_FILES_PAGE_NAME")