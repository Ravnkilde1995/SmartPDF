import io
import os
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter

class PDFService:
    def __init__(self, output_folder, template_folder):
        self.output_folder = output_folder
        self.template_folder = template_folder

    def generate_pdf(self, form_data):
        recipient_name = form_data.get('recipient_name')
        req_number = form_data.get('req_number')
        date = form_data.get('date')
        serial_number = form_data.get('serial_number')

        template_file = os.path.join(self.template_folder, 'template.pdf')
        output_file = os.path.join(self.output_folder, 'generated.pdf')

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=(612, 792))
        
        x_offset_text = 310
        x_offset_item = 100
        x_offset_SN = 315
        x_offset_qty = 450
        y_offset = 635
        line_height = 25

        can.drawString(x_offset_text, y_offset, recipient_name)
        can.drawString(x_offset_text, y_offset - line_height, req_number)
        can.drawString(x_offset_text, y_offset - 2 * line_height, date)

        for i in range(1, 12):
            item = form_data.get(f'item{i}', '')
            item_qty = form_data.get(f'item{i}_qty', '')
            if item:
                can.drawString(x_offset_item, y_offset - (4 + i) * line_height, item)
                can.drawString(x_offset_qty, y_offset - (4 + i) * line_height, item_qty)

        can.drawString(x_offset_SN, y_offset - 18.5 * line_height, serial_number)
        can.save()

        packet.seek(0)
        new_pdf = PdfReader(packet)
        existing_pdf = PdfReader(template_file)
        output = PdfWriter()

        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

        os.makedirs(self.output_folder, exist_ok=True)
        with open(output_file, 'wb') as outputStream:
            output.write(outputStream)

        return output_file