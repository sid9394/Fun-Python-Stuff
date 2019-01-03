from tika import parser
import os

def doc_parser(file):

    filename, file_extension = os.path.splitext(os.path.basename(file))
    print("Name:"+filename)
    try:
        # do something
        text = parser.from_file(file)
        text = (str(text['content']))
    except:
        # handle ValueError exception
        print(file, "--> Exception in File ***")

    return text






