from app.services.ocr_service import PDFTextExtractor
import re
import os

class FileRenamer:
    
    def extract_recipient(self, text):
        match = re.search(r'Full name, signature, and date of pick-up\.\s*(.*)', text, re.DOTALL)
    
        if match:
        # Extract the recipient from the found section
            recipient = match.group(1).strip()
        # Split recipient_text to get the first non-empty line
            lines = recipient.split('\n')
            for line in lines:
                if line.strip():  # Check if line is not empty
                    return line.strip()
    
        return "Unknown"
    
    def extract_order_number(self, text):
        match = re.search(r'(REQ|INC)[A-Z0-9]+', text, re.IGNORECASE)
        return match.group(0) if match else "Unknown"
    
    def rename_file(self, file_path):
        try:
            text = PDFTextExtractor().extract_text(file_path)
            recipient = self.extract_recipient(text)
            order_number = self.extract_order_number(text)

            if order_number != "Unknown":
                new_filename = f"{recipient} - {order_number}.pdf"
            else:
                new_filename = "Manual_check.pdf"

            new_filepath = os.path.join(os.path.dirname(file_path), new_filename)
            os.rename(file_path, new_filepath)
            return new_filename
        except Exception as e:
            print(f"Error renaming file {file_path}: {e}")
            return None