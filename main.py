import os
from PyPDF2 import PdfMerger

def pdf_merger(path):

    merger = PdfMerger()
    
    chng_dir = os.chdir(path)
    list_content = os.listdir(chng_dir)

    pdf_files = [pdf_file for pdf_file in list_content if pdf_file.endswith('.pdf')]

    print(f"\nPDF Files in '{path}'")
    for i in range(len(pdf_files)):
        print(f"{i+1}: {pdf_files[i]}")
    print()

    print(f"\nNumber of files you want to Merge")
    number = int(input("Enter the number = "))

    print("\nIndex of PDF file you want to Merge")
    for i in range(number):
        file = int(input(f"Enter the index of {i+1} file ="))
        merger.append(pdf_files[file-1])
    print()

    output = input("Enter the output file name: ")
    merger.write(output+".pdf") 
    merger.close()


path = input("Enter the location of files you want to merge: ")
pdf_merger(path)
