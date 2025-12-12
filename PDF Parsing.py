import PyPDF2
pdf_path = "sample.pdf"
with open(pdf_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""
    print(full_text)
# Output
"""
SAMPLE PDF DOCUMENT
INTRODUCTION
This PDF is created for testing Python PDF extraction tasks.
FEATURES
This document contains:
- normal text
- uppercase headings
- an email ID
- a sample table
- mixed content
CONTACT
For more info, email support@example.com
TABLE
Name Age City
Alex 22 Chennai
Sara 21 Delhi
CONCLUSION
This file is perfect for testing PyPDF2, pdfplumber, metadata extraction, and regex.
"""
#2
with open("sample.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    page1_text = reader.pages[0].extract_text()
    print(page1_text)
# Output
"""
SAMPLE PDF DOCUMENT
INTRODUCTION
This PDF is created for testing Python PDF extraction tasks.
FEATURES
This document contains:
- normal text
- uppercase headings
- an email ID
- a sample table
- mixed content
CONTACT
For more info, email support@example.com
TABLE
Name Age City
Alex 22 Chennai
Sara 21 Delhi
CONCLUSION
This file is perfect for testing PyPDF2, pdfplumber, metadata extraction, and regex.
"""
#3
with open("sample.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    print("Total pages:", len(reader.pages))
# Output
# Total pages: 1
#4

with open("sample.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    extracted = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            extracted += text
if extracted.strip() == "":
    print("Scanned PDF detected (no extractable text)")
else:
    print("PDF is not scanned")
# Output
# PDF is not scanned
# 5
with open("sample.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    headings = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            for line in text.split("\n"):
                if line.strip().isupper():
                    headings.append(line.strip())
print("Headings detected:")
for h in headings:
    print("-", h)
# Output
"""
Headings detected:
- SAMPLE PDF DOCUMENT
- INTRODUCTIO:
- FEATURES
- CONTACT
- TABLE
- CONCLUSION
"""
# 6
import pdfplumber
tables = []   
with pdfplumber.open("sample.pdf") as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:      
            tables.append(table)
print("Extracted Tables:")
if not tables:
    print("No tables found in this PDF")
else:
    for t in tables:
        for row in t:
            print(row)
# Output
"""
Extracted Tables:
No tables found in this PDF
"""
# 7
with open("sample.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    meta = reader.metadata
print("Title:", meta.title)
print("Author:", meta.author)
print("Created:", meta.creation_date)
#Output
"""
Title: (anonymous)
Author: (anonymous)
Created: 2025-12-12 06:43:57+00:00
"""
# 8
with open("sample.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(full_text)
print("Saved to output.txt")
# Output
#  Saved to output.txt
# 9
import re
with open("sample.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print("Emails found:", emails)
# Output
# Emails found: ['support@example.com']
# 10

pdf_path = "sample.pdf"
def extract_pdf(pdf_path):
    # First try PyPDF2
    py_text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            t = page.extract_text()
            if t:
                py_text += t
    if py_text.strip():
        return "Extracted using PyPDF2:\n" + py_text
    plumb_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                plumb_text += t
    if plumb_text.strip():
        return "Extracted using pdfplumber:\n" + plumb_text
    return "Scanned PDF detected (no extractable text)"
print(extract_pdf(pdf_path))
# Output
"""
Extracted using PyPDF2:
SAMPLE PDF DOCUMENT
INTRODUCTION
This PDF is created for testing Python PDF extraction tasks.
FEATURES
This document contains:
- normal text
- uppercase headings
- an email ID
- a sample table
- mixed content
CONTACT
For more info, email support@example.com
TABLE
Name Age City
Alex 22 Chennai
Sara 21 Delhi
CONCLUSION
This file is perfect for testing PyPDF2, pdfplumber, metadata extraction, and regex.
"""
