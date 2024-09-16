import pdf2image
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pandas as pd

class FileProcessor:
    def __init__(self, pdf_file, f_page=0, l_page=0):
        self.pdf_to_process = pdf_file

        if f_page == 0 and l_page == 0:
            self.first_page = 1
            self.last_page = self.get_num_of_pages()
        else:
            self.first_page = f_page
            self.last_page = l_page
        self.image_set = self.convert_pdf_to_images()

    def convert_pdf_to_images(self):
        images = enumerate(pdf2image.convert_from_path(self.pdf_to_process, first_page=self.first_page, last_page=self.last_page))
        return images

    def get_image_text(self):
        text_for_images = []
        for pg, img in self.image_set:
            text = pytesseract.image_to_string(img)
            text_for_images.append(text)
        return text_for_images

    def create_textonly_df(self, img, pg):
        img_data = pytesseract.image_to_data(img)
        data_list = list(map(lambda x: x.split('\t'), img_data.split('\n')))
        temp_df = pd.DataFrame(data_list[1:], columns=data_list[0])
        temp_df.dropna(inplace=True)
        temp_df['conf'] = temp_df['conf'].astype(float).astype(int)
        temp_df['page'] = pg
        usable_df = temp_df.query('conf > 30')
        img_df = pd.DataFrame()
        img_df['page_num'] = usable_df['page']
        img_df['text'] = usable_df['text']
        return img_df


    def create_all_images_df(self):
        all_images_df = pd.DataFrame()
        for pg, img in self.image_set:
            temp_df = self.create_textonly_df(img, pg)
            all_images_df = pd.concat((all_images_df, temp_df))
        return all_images_df




    def get_num_of_pages(self):
        attr_dict = pdf2image.pdf2image.pdfinfo_from_path(self.pdf_to_process)
        print(attr_dict['Pages'])
        return attr_dict['Pages']


