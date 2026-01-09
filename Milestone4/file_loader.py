import pdfplumber
from docx import Document

def load_file(uploaded_file):
    name = uploaded_file.name.lower()

    if name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
        return text

    elif name.endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join(p.text for p in doc.paragraphs)

    elif name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8", errors="ignore")

    else:
        return ""
