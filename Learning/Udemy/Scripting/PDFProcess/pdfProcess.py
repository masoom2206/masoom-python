# Using PyPDF2 library (pip3 install PyPDF2==1.26  --break-system-packages)

import PyPDF2
import sys

# with open("Learning/Udemy/Scripting/PDFProcess/dummy1.pdf", "r") as filePDF:
#   # print(filePDF)
#   reader = PyPDF2.PdfFileReader(filePDF)
#   print(reader.numPages)# Error: PdfReadWarning: PdfFileReader stream/file object is not in binary mode.

# To resolved the binary error, we will use "rb" mode
# with open("Learning/Udemy/Scripting/PDFProcess/dummy1.pdf", "rb") as filePDF:
#   # print(filePDF)# result >> <_io.BufferedReader name='Learning/Udemy/Scripting/PDFProcess/dummy1.pdf'>
#   reader = PyPDF2.PdfFileReader(filePDF)
#   print(reader.numPages)# result >> 1

# with open("Learning/Udemy/Scripting/PDFProcess/LD-Banner.pdf", "rb") as filePDF:
#   # print(filePDF)# result >> <_io.BufferedReader name='Learning/Udemy/Scripting/PDFProcess/dummy1.pdf'>
#   reader = PyPDF2.PdfFileReader(filePDF)
#   print(reader.numPages)# result >> 1

# with open("Learning/Udemy/Scripting/PDFProcess/dummy1.pdf", "rb") as filePDF:
#   # print(filePDF)# result >> <_io.BufferedReader name='Learning/Udemy/Scripting/PDFProcess/dummy1.pdf'>
#   reader = PyPDF2.PdfFileReader(filePDF)
#   print(reader.getPage(0))# result >> get page object.

# -------------------
# Rotate the PDF to 90 deg
# with open("Learning/Udemy/Scripting/PDFProcess/dummy1.pdf", "rb") as filePDF1:
#   # print(filePDF)# result >> <_io.BufferedReader name='Learning/Udemy/Scripting/PDFProcess/dummy1.pdf'>
#   reader = PyPDF2.PdfFileReader(filePDF1)
#   page = reader.getPage(0)
#   page.rotateCounterClockwise(90)
#   writer = PyPDF2.PdfFileWriter()
#   writer.addPage(page)
#   with open("Learning/Udemy/Scripting/PDFProcess/tilt.pdf", "wb") as filePDF2:
#     writer.write(filePDF2)
#   print(reader.getPage(0))# result >> get page object.

# # -------------------
# # Merge/combine the PDF files
# # /opt/homebrew/bin/python3 /Users/masoom2206/coading/python/masoom-python/Learning/Udemy/Scripting/PDFProcess/pdfProcess.py dummy1.pdf LD-Banner.pdf tilt.pdf

# inputs = sys.argv[1:]

# def pdfCombiner(pdf_list):
#   merger = PyPDF2.PdfFileMerger()
#   for pdf in pdf_list:
#     merger.append(f"Learning/Udemy/Scripting/PDFProcess/{pdf}")
#     print(pdf)
#   merger.write("Learning/Udemy/Scripting/PDFProcess/super.pdf")

# pdfCombiner(inputs)


# -------------------
# Add watermark in the PDF file

# template = PyPDF2.PdfFileReader(open("Learning/Udemy/Scripting/PDFProcess/super.pdf", "rb"))
# watermark = PyPDF2.PdfFileReader(open("Learning/Udemy/Scripting/PDFProcess/water.pdf", "rb"))
# output = PyPDF2.PdfFileWriter()
# for i in range(template.getNumPages()):
#   page = template.getPage(i)
#   page.mergePage(watermark.getPage(0))
#   output.addPage(page)
# with open("Learning/Udemy/Scripting/PDFProcess/water-output.pdf", "wb") as filePDF:
#   output.write(filePDF)


# -------------------
# Merge/combine and add watermark in the PDF files

inputs = sys.argv[1:]

def pdfCombiner(pdf_list):
  merger = PyPDF2.PdfFileMerger()
  for pdf in pdf_list:
    merger.append(f"Learning/Udemy/Scripting/PDFProcess/{pdf}")
    print(pdf)
  merger.write("Learning/Udemy/Scripting/PDFProcess/merger-output.pdf")
  # After merge the PDF add watermark
  pdf_file = PyPDF2.PdfFileReader(open(f"Learning/Udemy/Scripting/PDFProcess/merger-output.pdf", "rb"))
  watermark = PyPDF2.PdfFileReader(open("Learning/Udemy/Scripting/PDFProcess/water.pdf", "rb"))
  output = PyPDF2.PdfFileWriter()
  for i in range(pdf_file.getNumPages()):
    page = pdf_file.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open("Learning/Udemy/Scripting/PDFProcess/super-watermark.pdf", "wb") as filePDF:
      output.write(filePDF)

pdfCombiner(inputs)

