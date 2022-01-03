import json

from django.test import TestCase

# Create your tests here.


class Prod:
    def __init__(self, name, desc, image_src, image_href, alt):
        self.name = name
        self.desc = desc
        self.image_src = image_src
        self.image_href = image_href
        self.alt = alt

    @staticmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def __repr__(self):
        return f"Prod {self.name}"


with open("/home/ubuntudesrus/Рабочий стол/djangoBasis/geekshop/mainapp/data_json/products.json", "r") as ffjj:
    dd = json.loads(ffjj.read())["products"]
    r = [Prod(**i) for i in dd]
    print(r)
