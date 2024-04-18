import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

try:

    for file in os.listdir(os.curdir):
        if file.endswith(".pdf"):
            merger.append(file)
            merger.write("merged.pdf")

            print("Done!")

except Exception as e:
    print(f"erorr: {e}")
        
