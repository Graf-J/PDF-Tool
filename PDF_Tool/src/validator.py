import os

class Validator:
    # General Validations
    @staticmethod
    def check_action(action):
        if not action in ['info', 'rotate', 'merge', 'split', 'imgToPdf', 'standardize', 'resize']:
            print('Action not correct')
            exit(1)

    @staticmethod
    def check_inputs(paths):
        for path in paths:
            if not os.path.isfile(path):
                print('Input(s) not correct')
                exit(1)
    
    @staticmethod
    def check_output(path):
        if not os.path.isdir(path):
            print('Output not correct')
            exit(1)
        
    @staticmethod
    def check_filetype(inputs, expectation):
        types = [i.split('.')[-1].lower() for i in inputs]
        for t in types:
            if t != expectation:
                print(f'Only Files of type {expectation} are accepted')
                exit(1)

    @staticmethod
    def check_filetypes(inputs, expectations):
        types = [i.split('.')[-1].lower() for i in inputs]
        for t in types:
            if t not in expectations:
                print(f'Only Files of types {expectations} are accepted')
                exit(1)

    @staticmethod
    def forbid_degrees(deg):
        if deg != None:
            print('You cant specify a degree Argument here')
            exit(1)

    @staticmethod
    def allow_degrees(deg):
        if deg == None:
            print('You have to specify the degree Argument here')
            exit(1)
        if deg not in [0, 90, 180, 270]:
            print('Your degree Argument hast to be in [0, 90, 180, 270, 360]')
            exit(1)

    @staticmethod
    def allow_one_file(inputs):
        if len(inputs) > 1:
            print('Only one Input File allowed')
            exit(1)

    @staticmethod
    def allow_sizes(width, height):
        if width == None:
            print('You have to specify the width Argument here')
            exit(1)
        if height == None:
            print('You have to specify the height Argument here')
            exit(1)

    @staticmethod
    def forbid_sizes(width, height):
        if width != None:
            print('You cant specify a width Argument here')
            exit(1)
        if height != None:
            print('You cant specify a height Argument here')
            exit(1)

    # Action Specific Validations
    @staticmethod
    def check_split_params(inputs, deg, w, h):
        Validator.allow_one_file(inputs)
        Validator.check_filetype(inputs, 'pdf')
        Validator.forbid_degrees(deg)
        Validator.forbid_sizes(w, h)

    @staticmethod
    def check_merge_params(inputs, deg, w, h):
        Validator.check_filetype(inputs, 'pdf')
        Validator.forbid_degrees(deg)
        Validator.forbid_sizes(w, h)

    @staticmethod
    def check_resize_params(inputs, deg, w, h):
        Validator.allow_one_file(inputs)
        Validator.check_filetype(inputs, 'pdf')
        Validator.forbid_degrees(deg)
        Validator.allow_sizes(w, h)

    @staticmethod
    def check_imgToPdf_params(inputs, deg, w, h):
        Validator.allow_one_file(inputs)
        Validator.check_filetypes(inputs, ['png', 'jpg', 'jpeg'])
        Validator.forbid_degrees(deg)
        Validator.forbid_sizes(w, h)

    @staticmethod
    def check_standardize_params(inputs, deg, w, h):
        Validator.allow_one_file(inputs)
        Validator.check_filetype(inputs, 'pdf')
        Validator.forbid_degrees(deg)
        Validator.forbid_sizes(w, h)

    @staticmethod
    def check_rotate_params(inputs, deg, w, h):
        Validator.allow_one_file(inputs)
        Validator.check_filetype(inputs, 'pdf')
        Validator.allow_degrees(deg)
        Validator.forbid_sizes(w, h)

