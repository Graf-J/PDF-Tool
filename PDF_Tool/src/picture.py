from PIL import Image
from fpdf import FPDF

class Picture:
    def __init__(self, path):
        self.picture = Image.open(path)
        self.path = path
        self.file_name = path.split('/')[-1].split('.')[0]

    def convertToPdf(self, out):
        width, height = self.picture.size
        pdf = FPDF(unit='pt', format=[width, height])
        pdf.add_page()
        pdf.image(self.path, 0, 0)
        pdf.output(f'{ out }/{ self.file_name }.pdf', 'F')