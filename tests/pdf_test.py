import os

def form_data(): 
    return {
        'recipient_name': 'John Doe',
        'req_number': 'REQ123456',
        'date': '2023-08-29',
        'serial_number': 'SN12345',
        'item1': 'Item 1',
        'item1_qty': '1',
        'item2': 'Item 2',
        'item2_qty': '2',
    }

def test_generate_pdf(client, test_folder, form_data):
    

    return ""