from utils.file_processor import FileProcessor
import pandas as pd

def test_get_text():
    temp = FileProcessor("/Users/catherineimes/Downloads/mskrecords.pdf", 2, 6)
    temp_list = temp.get_image_text()
    for page in temp_list:
        print(page)
def test_get_df(file_name):
    temp = FileProcessor("/Users/catherineimes/Downloads/mskrecords.pdf", 2, 6)
    temp_df = temp.create_all_images_df()
    temp_df.to_csv(file_name, sep='\t', mode='w', index='False')


if __name__ == '__main__':
   test_get_df("testout.tsv")