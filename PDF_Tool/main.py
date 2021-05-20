import argparse
from PDF_Tool.src import Validator, PDF, Picture

# Arguments
parser = argparse.ArgumentParser(description="Run <pdf info> for more Information")
parser.add_argument('action', type=str, metavar='action', help='Enter the Action you want to execute')
parser.add_argument('-i', '--input', type=str, metavar='', default='', help='Enter your Input File(s) [ multiple Files like: file1.pdf,file2.pdf,file3.pdf ]')
parser.add_argument('-o', '--output', type=str, metavar='', default='.', help='Enter your Output Directory')
parser.add_argument('-d', '--degree', type=int, metavar='', default=None, help='Enter degrees you want to rotate the PDF')
args = parser.parse_args()


def print_info():
    print("""
                        <<DB Tool>>

This Tool provides some Feature to edit your PDF Files.

Run it like pdf <action> -i <intput File(s)> -o <output Files>


actions:    - split:        Splits all Pages of a PDF and outputs all those
                            Pages in seperate Files.
            
            - merge:        Here you select more than one Input Files. Those
                            will get merged in the selected sequence into one
                            PDF File.

            - standardize:  If some Pages of your PDF have a different size than
                            the others, you can use this command. It calculates
                            the most common size of your PDF pages and resizes
                            the other pages due to this size.

            - rotate:       Rotates your all Pages of your PDF to a certain degree.
                            Here you have to use the -d or --degree flag to add the
                            number of degrees your pages should rotate clockwise.

            - imgToPdf      Converts a Image to a PDF.


-i          Here you specify your input File(s). If you need more than Input Files
            e.g. for the command merge, make sure to use the correct syntax like 
            this: file_1.pdf,file_2.pdf,file_3.pdf


-o          Here you specify the output Directory of your new PDF. By default the
            PDF(s) will get generate in your current directory
    """)


def validate():
    if args.action != 'info':
        inputs = args.input.strip().split(',')

        Validator.check_action(args.action)
        Validator.check_inputs(inputs)
        Validator.check_output(args.output)


def process():
    inputs = args.input.strip().split(',')

    if args.action == 'info':
        print_info()

    elif args.action == 'rotate':
        Validator.check_rotate_params(inputs, args.degree)
        pdf = PDF(inputs[0])
        pdf.rotate(inputs[0], args.output, args.degree)

    elif args.action == 'imgToPdf':
        Validator.check_imgToPdf_params(inputs, args.degree)
        picture = Picture(inputs[0])
        picture.convertToPdf(args.output)

    elif args.action == 'standardize':
        Validator.check_standardize_params(inputs, args.degree)
        pdf = PDF(inputs[0])
        pdf.standardize(args.output)

    elif args.action == 'merge':
        Validator.check_merge_params(inputs, args.degree)
        PDF.merge(inputs, args.output)

    elif args.action == 'split':
        Validator.check_split_params(inputs, args.degree)
        pdf = PDF(inputs[0])
        pdf.split(args.output)
        


def main():
    validate()
    process()