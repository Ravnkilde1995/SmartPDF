from pdf2image import convert_from_path
import pytesseract

class PDFTextExtractor:
    def extract_text(self, file_path):
        try:
            # Har prøvet at tilføje til miljø variable, men det virker ikke.
            poppler_path = r'C:\Program Files (x86)\poppler-24.07.0\Library\bin'
            images = convert_from_path(file_path, poppler_path=poppler_path)
            text = ""
            for image in images:
                text += pytesseract.image_to_string(image)
            return text
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            return ""