import pdfplumber
import docx

def read_txt(file):
    return file.read().decode("utf-8")

def read_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def load_file(file):
    if file.name.endswith(".txt"):
        return read_txt(file)
    elif file.name.endswith(".pdf"):
        return read_pdf(file)
    elif file.name.endswith(".docx"):
        return read_docx(file)
    else:
        raise ValueError("Unsupported file format")
