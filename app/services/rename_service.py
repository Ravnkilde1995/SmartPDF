from app.services.ocr_service import PDFTextExtractor
import re
import os

class FileRenamer:
    def extract_recipient(self, text):
        match = re.search(r'Recipient Name\s*([a-zA-Z ]+)', text, re.IGNORECASE)
    
        if match:
            recipient = match.group(1).strip()
            return recipient
        
        return "Unknown"
    
    def extract_order_number(self, text):
        match = re.search(r'(REQ|INC)[O0-9]+', text, re.IGNORECASE)
        
        if match:
            order_number = match.group(0)
            order_number = order_number.replace('O', '0').replace('o', '0')
            return order_number
        return "Unknown"
    
    def generate_unique_filename(self, directory, filename):
        base_name, extension = os.path.splitext(filename)
        counter = 1
        new_filename = filename
        while os.path.exists(os.path.join(directory, new_filename)):
            new_filename = f"{base_name}_{counter}{extension}"
            counter += 1
        return new_filename
    
    def rename_file(self, file_path):
        try:
            text = PDFTextExtractor().extract_text(file_path)
            recipient = self.extract_recipient(text)
            order_number = self.extract_order_number(text)

            if order_number != "Unknown" and recipient != "Unknown":
                new_filename = f"{recipient} - {order_number}.pdf"
            else:
                new_filename = "Manual_check.pdf"

            new_filename = self.generate_unique_filename(
                os.path.dirname(file_path),
                new_filename
            )

            new_filepath = os.path.join(os.path.dirname(file_path), new_filename)
            os.rename(file_path, new_filepath)
            return new_filename
        except Exception as e:
            print(f"Error renaming file {file_path}: {e}")
            return None