import subprocess
import sys

try:
    import pypdf
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    import pypdf

reader = pypdf.PdfReader("EduGenie-Google Gemini Powered Learning Assistant_Document.docx.pdf")
text = ""
for page in reader.pages:
    extracted = page.extract_text()
    if extracted:
        text += extracted + "\n"

with open("srs.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("Done extracting PDF to srs.txt")
