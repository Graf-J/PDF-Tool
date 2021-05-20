from PIL import Image

class Picture:
    def __init__(self, path):
        self.picture = Image.open(path)
        self.file_name = path.split('/')[-1].split('.')[0]

    def convertToPdf(self, out):
        self.picture.convert('RGB')
        self.picture.save(f'{ out }/{ self.file_name }.pdf')