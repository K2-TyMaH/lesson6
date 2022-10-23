import re


KIRILIK = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
LATINIC = ("a", "b", "v", "g", "d", "e", "e", "j", "z",
           "i", "y", "k", "l", "m", "n", "o", "p", "r", "s",
           "t", "u", "f", "h", "c", "ch", "sh", "sch", "",
           "u", "", "e", "yu", "ya", "e", "i", "i", "g")

TRANSLAT = {}

for kir, lat in zip(KIRILIK, LATINIC):
   TRANSLAT[ord(kir)] = lat
   TRANSLAT[ord(kir.upper())] = lat.upper()


def normalize(name: str) -> str:
    new_name = name.translate(TRANSLAT)
    new_name = re.sub(r'\W', '_', new_name)
    return new_name

