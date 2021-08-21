import base64
import random
import string

from pywhatkit import pywhatkit as pwt


letters = string.ascii_letters


class Captcha:
    def __init__(self, index):
        self.img = None
        self.index = index
        self.__captcha = None
        self.text = None
        self.__img = None
        self.generate()
        self.convert()

    def generate(self):
        self.text = ''.join(random.choice(letters) for i in range(6))
        pwt.text_to_handwriting(self.text, rgb=(0, 0, 255), save_to=f"img_cache/{self.index}.png")

    def convert(self):
        with open(f"img_cache/{self.index}.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            self.img = encoded_string
