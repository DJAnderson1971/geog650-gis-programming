# Create a variable to open an existing .pdf document
pdfDoc = arcpy.mp.PDFDocumentOpen(r"C:\EsriTraining\PythonMapSeries\PHRepairs.pdf")

# Get the number of pages from the document to be modified
pdfDoc.pageCount

# Delete the modified pages from the existing .pdf
pdfDoc.deletePages("1-2")

# Save changes to the existing .pdf
pdfDoc.saveAndClose()

# Get the number of pages from the updated document
pdfDoc.pageCount

# Reopen an existing .pdf document to insert additional pages
pdfDoc = arcpy.mp.PDFDocumentOpen(r"C:\EsriTraining\PythonMapSeries\PHRepairs.pdf")

# Insert the update second page (inserting it first because otherwise it will not be the second page in the report)
pdfDoc.insertPages(r"C:\EsriTraining\PythonMapSeries\PHRepairs_2.pdf")

# Insert the update first page(inserting it second because otherwise it will not be the first page in the report)
pdfDoc.insertPages(r"C:\EsriTraining\PythonMapSeries\PHRepairs_1.pdf")

# Save changes to the existing .pdf
pdfDoc.saveAndClose()

# Get the number of pages from the updated document
pdfDoc.pageCount

# Create a new document for the updated pages 5 - 8
newDoc = arcpy.mp.PDFDocumentCreate(r"C:\EsriTraining\PythonMapSeries\PHRepairs_5-8.pdf")

# Append the updated pages 5 - 8 from the previous exercise into newDoc
newDoc.appendPages(r"C:\EsriTraining\PythonMapSeries\PHRepairs_5.pdf")
newDoc.appendPages(r"C:\EsriTraining\PythonMapSeries\PHRepairs_6.pdf")
newDoc.appendPages(r"C:\EsriTraining\PythonMapSeries\PHRepairs_7.pdf")
newDoc.appendPages(r"C:\EsriTraining\PythonMapSeries\PHRepairs_8.pdf")

# Save and close the changes to newDoc
newDoc.saveAndClose()

# Reopen an existing .pdf document to delete and append additional pages from PHRepairs_5-8.pdf
pdfDoc = arcpy.mp.PDFDocumentOpen(r"C:\EsriTraining\PythonMapSeries\PHRepairs.pdf")

# Delete pages 5-8 from PHRepairs.pdf
pdfDoc.deletePages("5-8")

# Append PHRepairs_5-8.pdf to the end of pdfDoc
pdfDoc.appendPages(r"C:\EsriTraining\PythonMapSeries\PHRepairs_5-8.pdf")

# Save and close the changes to pdfDoc
pdfDoc.saveAndClose()

# Get the number of pages from the updated document
pdfDoc.pageCount