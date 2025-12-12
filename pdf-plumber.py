import pdfplumber
import csv
# 1
with pdfplumber.open("sample.pdf") as pdf:
    page1 = pdf.pages[0]
    text = page1.extract_text()
    print(text)
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
# 2
with pdfplumber.open("sample.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"\n----- Page {i+1} -----")
        print(page.extract_text())
# Output
"""
----- Page 1 -----
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
# 3
with pdfplumber.open("sample.pdf") as pdf:
    print("Total pages:", len(pdf.pages))
# Output
# Total pages: 1
# 4
with pdfplumber.open("sample.pdf") as pdf:
    full_text = ""
    for page in pdf.pages:
        t = page.extract_text()
        if t:
            full_text += t

if full_text.strip() == "":
    print("Scanned PDF detected (no extractable text)")
else:
    print("PDF is not scanned")
# Output
# PDF is not scanned
# 5
with pdfplumber.open("sample.pdf") as pdf:
    page1 = pdf.pages[0]
    table = page1.extract_table()

    if table:
        print("First Table on Page 1:")
        for row in table:
            print(row)
    else:
        print("No table found on page 1")
# Output
# No table found on page 1
# 6
tables = []

with pdfplumber.open("sample.pdf") as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            tables.append(table)
print("Extracted Tables:")
if not tables:
    print("No tables found")
else:
    for t in tables:
        for row in t:
            print(row)
# Output
"""
Extracted Tables:
No tables found
"""
# 7
with pdfplumber.open("sample.pdf") as pdf:
    page = pdf.pages[0]
    words = page.extract_words()
    for word in words:
        print(word)
# Output
"""
{'text': 'SAMPLE', 'x0': 78.0, 'x1': 118.57000000000001, 'top': 92.07000000000005, 'doctop': 92.07000000000005, 'bottom': 102.07000000000005, 'upright': True, 'height': 10.0, 'width': 40.57000000000001, 'direction': 'ltr'}
{'text': 'PDF', 'x0': 121.35000000000001, 'x1': 141.35000000000002, 'top': 92.07000000000005, 'doctop': 92.07000000000005, 'bottom': 102.07000000000005, 'upright': True, 'height': 10.0, 'width': 20.000000000000014, 'direction': 'ltr'}
{'text': 'DOCUMENT', 'x0': 144.13, 'x1': 201.90000000000003, 'top': 92.07000000000005, 'doctop': 92.07000000000005, 'bottom': 102.07000000000005, 'upright': True, 'height': 10.0, 'width': 57.77000000000004, 'direction': 'ltr'}
{'text': 'INTRODUCTION', 'x0': 78.0, 'x1': 154.66, 'top': 128.07000000000005, 'doctop': 128.07000000000005, 'bottom': 138.07000000000005, 'upright': True, 'height': 10.0, 'width': 76.66, 'direction': 'ltr'}
{'text': 'This', 'x0': 78.0, 'x1': 96.89, 'top': 152.07000000000005, 'doctop': 152.07000000000005, 'bottom': 162.07000000000005, 'upright': True, 'height': 10.0, 'width': 18.89, 'direction': 'ltr'}
{'text': 'PDF', 'x0': 99.67, 'x1': 119.67, 'top': 152.07000000000005, 'doctop': 152.07000000000005, 'bottom': 162.07000000000005, 'upright': True, 'height': 10.0, 'width': 20.0, 'direction': 'ltr'}
{'text': 'is', 'x0': 122.45, 'x1': 129.67000000000002, 'top': 152.07000000000005, 'doctop': 152.07000000000005, 'bottom': 162.07000000000005, 'upright': True, 'height': 10.0, 'width': 7.220000000000013, 'direction': 'ltr'}
{'text': 'created', 'x0': 132.45, 'x1': 165.8, 'top': 152.07000000000005, 'doctop': 152.07000000000005, 'bottom': 162.07000000000005, 'upright': True, 'height': 10.0, 'width': 33.35000000000002, 'direction': 'ltr'}
{'text': 'for', 'x0': 168.58, 'x1': 180.25000000000003, 'top': 152.07000000000005, 'doctop': 152.07000000000005, 'bottom': 162.07000000000005, 'upright': True, 'height': 10.0, 'width': 11.670000000000016, 'direction': 'ltr'}
{'text': 'testing', 'x0': 183.03000000000003, 'x1': 212.49, 'top': 152.07000000000005, 'doctop': 152.07000000000005, 'bottom': 162.07000000000005, 'upright': True, 'height': 10.0, 'width': 29.45999999999998, 'direction': 'ltr'}
{'text': 'Python', 'x0': 215.27, 'x1': 246.4, 'top': 152.07000000000005, 'doctop': 152.07000000000005, 'bottom': 162.07000000000005, 'upright': True, 'height': 10.0, 'width': 31.129999999999995, 'direction': 'ltr'}
{'text': 'PDF', 'x0': 249.18, 'x1': 269.18, 'top': 152.07000000000005, 'doctop': 152.07000000000005, 'bottom': 162.07000000000005, 'upright': True, 'height': 10.0, 'width': 20.0, 'direction': 'ltr'}
{'text': 'extraction', 'x0': 271.96000000000004, 'x1': 315.31, 'top': 152.07000000000005, 'doctop': 152.07000000000005, 'bottom': 162.07000000000005, 'upright': True, 'height': 10.0, 'width': 43.349999999999966, 'direction': 'ltr'}
{'text': 'tasks.', 'x0': 318.09000000000003, 'x1': 344.21000000000004, 'top': 152.07000000000005, 'doctop': 152.07000000000005, 'bottom': 162.07000000000005, 'upright': True, 'height': 10.0, 'width': 26.120000000000005, 'direction': 'ltr'}
{'text': 'FEATURES', 'x0': 78.0, 'x1': 131.34, 'top': 188.07000000000005, 'doctop': 188.07000000000005, 'bottom': 198.07000000000005, 'upright': True, 'height': 10.0, 'width': 53.34, 'direction': 'ltr'}
{'text': 'This', 'x0': 78.0, 'x1': 96.89, 'top': 212.07000000000005, 'doctop': 212.07000000000005, 'bottom': 222.07000000000005, 'upright': True, 'height': 10.0, 'width': 18.89, 'direction': 'ltr'}
{'text': 'document', 'x0': 99.67, 'x1': 143.58, 'top': 212.07000000000005, 'doctop': 212.07000000000005, 'bottom': 222.07000000000005, 'upright': True, 'height': 10.0, 'width': 43.91000000000001, 'direction': 'ltr'}
{'text': 'contains:', 'x0': 146.36, 'x1': 186.38000000000002, 'top': 212.07000000000005, 'doctop': 212.07000000000005, 'bottom': 222.07000000000005, 'upright': True, 'height': 10.0, 'width': 40.02000000000001, 'direction': 'ltr'}
{'text': '-', 'x0': 78.0, 'x1': 81.33, 'top': 236.07000000000005, 'doctop': 236.07000000000005, 'bottom': 246.07000000000005, 'upright': True, 'height': 10.0, 'width': 3.3299999999999983, 'direction': 'ltr'}
{'text': 'normal', 'x0': 84.11, 'x1': 114.67, 'top': 236.07000000000005, 'doctop': 236.07000000000005, 'bottom': 246.07000000000005, 'upright': True, 'height': 10.0, 'width': 30.560000000000002, 'direction': 'ltr'}
{'text': 'text', 'x0': 117.45, 'x1': 133.57000000000002, 'top': 236.07000000000005, 'doctop': 236.07000000000005, 'bottom': 246.07000000000005, 'upright': True, 'height': 10.0, 'width': 16.12000000000002, 'direction': 'ltr'}
{'text': '-', 'x0': 78.0, 'x1': 81.33, 'top': 260.07000000000005, 'doctop': 260.07000000000005, 'bottom': 270.07000000000005, 'upright': True, 'height': 10.0, 'width': 3.3299999999999983, 'direction': 'ltr'}
{'text': 'uppercase', 'x0': 84.11, 'x1': 130.8, 'top': 260.07000000000005, 'doctop': 260.07000000000005, 'bottom': 270.07000000000005, 'upright': True, 'height': 10.0, 'width': 46.69000000000001, 'direction': 'ltr'}
{'text': 'headings', 'x0': 133.58, 'x1': 174.16000000000003, 'top': 260.07000000000005, 'doctop': 260.07000000000005, 'bottom': 270.07000000000005, 'upright': True, 'height': 10.0, 'width': 40.58000000000001, 'direction': 'ltr'}
{'text': '-', 'x0': 78.0, 'x1': 81.33, 'top': 284.07, 'doctop': 284.07, 'bottom': 294.07, 'upright': True, 'height': 10.0, 'width': 3.3299999999999983, 'direction': 'ltr'}
{'text': 'an', 'x0': 84.11, 'x1': 95.23, 'top': 284.07, 'doctop': 284.07, 'bottom': 294.07, 'upright': True, 'height': 10.0, 'width': 11.120000000000005, 'direction': 'ltr'}
{'text': 'email', 'x0': 98.01, 'x1': 121.9, 'top': 284.07, 'doctop': 284.07, 'bottom': 294.07, 'upright': True, 'height': 10.0, 'width': 23.89, 'direction': 'ltr'}
{'text': 'ID', 'x0': 124.68, 'x1': 134.68, 'top': 284.07, 'doctop': 284.07, 'bottom': 294.07, 'upright': True, 'height': 10.0, 'width': 10.0, 'direction': 'ltr'}
{'text': '-', 'x0': 78.0, 'x1': 81.33, 'top': 308.07, 'doctop': 308.07, 'bottom': 318.07, 'upright': True, 'height': 10.0, 'width': 3.3299999999999983, 'direction': 'ltr'}
{'text': 'a', 'x0': 84.11, 'x1': 89.67, 'top': 308.07, 'doctop': 308.07, 'bottom': 318.07, 'upright': True, 'height': 10.0, 'width': 5.560000000000002, 'direction': 'ltr'}
{'text': 'sample', 'x0': 92.45, 'x1': 124.68, 'top': 308.07, 'doctop': 308.07, 'bottom': 318.07, 'upright': True, 'height': 10.0, 'width': 32.230000000000004, 'direction': 'ltr'}
{'text': 'table', 'x0': 127.46000000000001, 'x1': 149.14000000000001, 'top': 308.07, 'doctop': 308.07, 'bottom': 318.07, 'upright': True, 'height': 10.0, 'width': 21.680000000000007, 'direction': 'ltr'}
{'text': '-', 'x0': 78.0, 'x1': 81.33, 'top': 332.07, 'doctop': 332.07, 'bottom': 342.07, 'upright': True, 'height': 10.0, 'width': 3.3299999999999983, 'direction': 'ltr'}
{'text': 'mixed', 'x0': 84.11, 'x1': 110.78, 'top': 332.07, 'doctop': 332.07, 'bottom': 342.07, 'upright': True, 'height': 10.0, 'width': 26.67, 'direction': 'ltr'}
{'text': 'content', 'x0': 113.56, 'x1': 146.36, 'top': 332.07, 'doctop': 332.07, 'bottom': 342.07, 'upright': True, 'height': 10.0, 'width': 32.80000000000001, 'direction': 'ltr'}
{'text': 'CONTACT', 'x0': 78.0, 'x1': 126.33, 'top': 368.07, 'doctop': 368.07, 'bottom': 378.07, 'upright': True, 'height': 10.0, 'width': 48.33, 'direction': 'ltr'}
{'text': 'For', 'x0': 78.0, 'x1': 93.0, 'top': 392.07, 'doctop': 392.07, 'bottom': 402.07, 'upright': True, 'height': 10.0, 'width': 15.0, 'direction': 'ltr'}
{'text': 'more', 'x0': 95.78, 'x1': 118.56, 'top': 392.07, 'doctop': 392.07, 'bottom': 402.07, 'upright': True, 'height': 10.0, 'width': 22.78, 'direction': 'ltr'}
{'text': 'info,', 'x0': 121.34, 'x1': 140.24, 'top': 392.07, 'doctop': 392.07, 'bottom': 402.07, 'upright': True, 'height': 10.0, 'width': 18.900000000000006, 'direction': 'ltr'}
{'text': 'email', 'x0': 143.02, 'x1': 166.91, 'top': 392.07, 'doctop': 392.07, 'bottom': 402.07, 'upright': True, 'height': 10.0, 'width': 23.889999999999986, 'direction': 'ltr'}
{'text': 'support@example.com', 'x0': 169.69, 'x1': 272.65000000000003, 'top': 392.07, 'doctop': 392.07, 'bottom': 402.07, 'upright': True, 'height': 10.0, 'width': 102.96000000000004, 'direction': 'ltr'}
{'text': 'TABLE', 'x0': 78.0, 'x1': 109.67999999999999, 'top': 428.07, 'doctop': 428.07, 'bottom': 438.07, 'upright': True, 'height': 10.0, 'width': 31.679999999999993, 'direction': 'ltr'}
{'text': 'Name', 'x0': 78.0, 'x1': 104.67, 'top': 452.07, 'doctop': 452.07, 'bottom': 462.07, 'upright': True, 'height': 10.0, 'width': 26.67, 'direction': 'ltr'}
{'text': 'Age', 'x0': 107.45, 'x1': 125.24000000000001, 'top': 452.07, 'doctop': 452.07, 'bottom': 462.07, 'upright': True, 'height': 10.0, 'width': 17.790000000000006, 'direction': 'ltr'}
{'text': 'City', 'x0': 128.02, 'x1': 145.24, 'top': 452.07, 'doctop': 452.07, 'bottom': 462.07, 'upright': True, 'height': 10.0, 'width': 17.22, 'direction': 'ltr'}
{'text': 'Alex', 'x0': 78.0, 'x1': 97.45, 'top': 476.07, 'doctop': 476.07, 'bottom': 486.07, 'upright': True, 'height': 10.0, 'width': 19.450000000000003, 'direction': 'ltr'}
{'text': '22', 'x0': 100.23, 'x1': 111.35000000000001, 'top': 476.07, 'doctop': 476.07, 'bottom': 486.07, 'upright': True, 'height': 10.0, 'width': 11.120000000000005, 'direction': 'ltr'}
{'text': 'Chennai', 'x0': 114.13000000000001, 'x1': 151.37000000000003, 'top': 476.07, 'doctop': 476.07, 'bottom': 486.07, 'upright': True, 'height': 10.0, 'width': 37.24000000000002, 'direction': 'ltr'}
{'text': 'Sara', 'x0': 78.0, 'x1': 99.12, 'top': 500.07, 'doctop': 500.07, 'bottom': 510.07, 'upright': True, 'height': 10.0, 'width': 21.120000000000005, 'direction': 'ltr'}
{'text': '21', 'x0': 101.9, 'x1': 113.02000000000001, 'top': 500.07, 'doctop': 500.07, 'bottom': 510.07, 'upright': True, 'height': 10.0, 'width': 11.120000000000005, 'direction': 'ltr'}
{'text': 'Delhi', 'x0': 115.80000000000001, 'x1': 138.58, 'top': 500.07, 'doctop': 500.07, 'bottom': 510.07, 'upright': True, 'height': 10.0, 'width': 22.78, 'direction': 'ltr'}
{'text': 'CONCLUSION', 'x0': 78.0, 'x1': 144.67, 'top': 536.0699999999999, 'doctop': 536.0699999999999, 'bottom': 546.0699999999999, 'upright': True, 'height': 10.0, 'width': 66.66999999999999, 'direction': 'ltr'}
{'text': 'This', 'x0': 78.0, 'x1': 96.89, 'top': 560.0699999999999, 'doctop': 560.0699999999999, 'bottom': 570.0699999999999, 'upright': True, 'height': 10.0, 'width': 18.89, 'direction': 'ltr'}
{'text': 'file', 'x0': 99.67, 'x1': 112.45, 'top': 560.0699999999999, 'doctop': 560.0699999999999, 'bottom': 570.0699999999999, 'upright': True, 'height': 10.0, 'width': 12.780000000000001, 'direction': 'ltr'}
{'text': 'is', 'x0': 115.23, 'x1': 122.45, 'top': 560.0699999999999, 'doctop': 560.0699999999999, 'bottom': 570.0699999999999, 'upright': True, 'height': 10.0, 'width': 7.219999999999999, 'direction': 'ltr'}
{'text': 'perfect', 'x0': 125.23, 'x1': 155.8, 'top': 560.0699999999999, 'doctop': 560.0699999999999, 'bottom': 570.0699999999999, 'upright': True, 'height': 10.0, 'width': 30.570000000000007, 'direction': 'ltr'}
{'text': 'for', 'x0': 158.58, 'x1': 170.25000000000003, 'top': 560.0699999999999, 'doctop': 560.0699999999999, 'bottom': 570.0699999999999, 'upright': True, 'height': 10.0, 'width': 11.670000000000016, 'direction': 'ltr'}
{'text': 'testing', 'x0': 173.03000000000003, 'x1': 202.49, 'top': 560.0699999999999, 'doctop': 560.0699999999999, 'bottom': 570.0699999999999, 'upright': True, 'height': 10.0, 'width': 29.45999999999998, 'direction': 'ltr'}
{'text': 'PyPDF2,', 'x0': 205.27000000000004, 'x1': 245.28, 'top': 560.0699999999999, 'doctop': 560.0699999999999, 'bottom': 570.0699999999999, 'upright': True, 'height': 10.0, 'width': 40.00999999999996, 'direction': 'ltr'}
{'text': 'pdfplumber,', 'x0': 248.06, 'x1': 300.86, 'top': 560.0699999999999, 'doctop': 560.0699999999999, 'bottom': 570.0699999999999, 'upright': True, 'height': 10.0, 'width': 52.80000000000001, 'direction': 'ltr'}
{'text': 'metadata', 'x0': 303.64000000000004, 'x1': 345.33000000000004, 'top': 560.0699999999999, 'doctop': 560.0699999999999, 'bottom': 570.0699999999999, 'upright': True, 'height': 10.0, 'width': 41.69, 'direction': 'ltr'}
{'text': 'extraction,', 'x0': 348.11, 'x1': 394.23999999999995, 'top': 560.0699999999999, 'doctop': 560.0699999999999, 'bottom': 570.0699999999999, 'upright': True, 'height': 10.0, 'width': 46.12999999999994, 'direction': 'ltr'}
{'text': 'and', 'x0': 397.0199999999999, 'x1': 413.69999999999993, 'top': 560.0699999999999, 'doctop': 560.0699999999999, 'bottom': 570.0699999999999, 'upright': True, 'height': 10.0, 'width': 16.680000000000007, 'direction': 'ltr'}
{'text': 'regex.', 'x0': 416.4799999999999, 'x1': 444.26999999999987, 'top': 560.0699999999999, 'doctop': 560.0699999999999, 'bottom': 570.0699999999999, 'upright': True, 'height': 10.0, 'width': 27.789999999999964, 'direction': 'ltr'}
"""
# 8
with pdfplumber.open("sample.pdf") as pdf:
    page = pdf.pages[0]
    images = page.images
    if not images:
        print("No images found on page")
    else:
        for img in images:
            print(img)
# Output
# No images found on page
# 9
with pdfplumber.open("sample.pdf") as pdf:
    page = pdf.pages[0]
    curves = page.curves
    lines  = page.lines
    rects  = page.rects
    print("Lines:", lines)
    print("Curves:", curves)
    print("Rectangles:", rects)
# Output
"""
Lines: []
Curves: []
Rectangles: []
"""
# 10
with pdfplumber.open("sample.pdf") as pdf:
    page = pdf.pages[0]
    table = page.extract_table()

    if table:
        with open("output_table.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(table)
        print("Table saved as output_table.csv")
    else:
        print("No table found to save")
# Output
# No table found to save