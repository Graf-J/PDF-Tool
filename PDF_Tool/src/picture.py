from PIL import Image

class Picture:
    def __init__(self, path):
        self.picture = Image.open(path)

    def convertToPdf(self, out):
        self.picture.convert('RGB')
        self.picture.save(f'{ out }/image.pdf')