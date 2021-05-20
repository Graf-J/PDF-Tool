from PyPDF2 import PdfFileReader, PdfFileWriter

class PDF:
    def __init__(self, path):
        self.pdf = PdfFileReader(open(path, 'rb'))


    def split(self, output):
        for i in range(self.pdf.numPages):
            self.write(self.pdf.getPage(i), f'{ output }/page_{ i + 1 }')
            

    def write(self, pdf, name):
        output = PdfFileWriter()
        output.addPage(pdf)
        with open(name + '.pdf', 'wb') as outputStream:
            output.write(outputStream)


    def standardize(self, output):
        pages = []
        for i in range(self.pdf.numPages):
            pages.append(self.pdf.getPage(i))

        common_size = self.calc_main_size(pages)
        self.resize(pages, common_size, output)


    def calc_main_size(self, pages):
        sizes = []
        for page in pages:
            sizes.append((page.mediaBox.lowerLeft, page.mediaBox.lowerRight, page.mediaBox.upperLeft, page.mediaBox.upperRight))

        most_common = max(set(sizes), key=sizes.count)
        return most_common[3]

    
    def resize(self, pages, common_size, out):
        output = PdfFileWriter()

        for page in pages:
            page.scaleTo(float(common_size[0]), float(common_size[1]))
            output.addPage(page)

        with open(f'{ out }/standardized.pdf', 'wb') as outputStream:
            output.write(outputStream)


    def rotate(self, out, deg):
        output = PdfFileWriter()

        for i in range(self.pdf.numPages):
            page = self.pdf.getPage(i)
            page.rotateClockwise(deg)
            output.addPage(page)

        with open(f'{ out }/rotate{ deg }.pdf', 'wb') as outputStream:
            output.write(outputStream)
    
    @staticmethod
    def merge(inputs, out):
        output = PdfFileWriter()

        for i in inputs:
            pdf = PdfFileReader(open(i, 'rb'))

            for pageNum in range(pdf.numPages):
                page = pdf.getPage(pageNum)
                output.addPage(page)

        with open(f'{ out }/merge.pdf', 'wb') as outputStream:
            output.write(outputStream)

        