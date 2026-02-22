import PyPDF2
import re

class ResumeParser:
    @staticmethod
    def extract_text_from_pdf(pdf_file):
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return ResumeParser.clean_text(text)
        except Exception as e:
            raise Exception(f"Error parsing PDF: {str(e)}")
    
    @staticmethod
    def clean_text(text):
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text
