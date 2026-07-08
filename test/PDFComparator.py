import re
from pypdf import PdfReader

def pdf_comparator(pdf_path1, pdf_path2):
    flag = 0
    reader1 = PdfReader(pdf_path1)
    reader2 = PdfReader(pdf_path2)
    for page_num, page in enumerate(reader1.pages, start=1):
        text1 = page.extract_text()
    for page_num, page in enumerate(reader2.pages, start=1):
        text2 = page.extract_text()

    if text1 is None or text2 is None:
        print("Error: One or both PDF files could not be read.")
        pass
    
    if text1 != text2:
        flag = 1

    if flag == 0:
        print("Both PDF files are identical.")
    else:
        print("PDF files are different.")

INP1 = input("Enter the PDF file with absolute path: ")
INP2 = input("Enter the second PDF file with absolute path: ")
pdf_comparator(INP1, INP2)

