import os

class config():
    c_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = f'{c_dir}\\images\\'
    pdf_path = f'{c_dir}\\pdf_files\\'
    csv_path = f'{c_dir}\\csv_files\\'

    if not os.path.exists(img_path):
        os.makedirs(img_path)