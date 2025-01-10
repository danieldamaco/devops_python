"""
Create a script that accepts the file name and puts its extension to output. If there is no extension - an exception should be raised.
"""

import argparse
errors = {"NotLinesFound": "The file is empty", }

try:
    parser = argparse.ArgumentParser(description="Read file and show the extension")
    parser.add_argument('filename', help='read the file')
    args = parser.parse_args()
    f= open(args.filename)

    with f:
        lines = len(f.readlines())
        if lines == 0:
            raise Exception("NotLinesFound")
        else:
            print("The number of lines are: ", lines)
except FileNotFoundError as err:
    print('File not found')
except Exception as err:
    print(errors[err.args[0]])