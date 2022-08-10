from PIL import Image
from os import system
system("title Convert WEBP TO PNG - T.ME/MAILNGON")
from easygui import fileopenbox,filesavebox
def convert_webp_png(PATH_WEBP):
    im = Image.open(r'{}'.format(PATH_WEBP))
    try:
        PATH_PNG = filesavebox('Save File !')+'.png'
        convert = im.save(PATH_PNG,format="png",lossless=True)
    except:
        print("Convert False ",PATH_WEBP)
while True:
    PATH_WEBP = fileopenbox("Choice File Need Convert")
    convert_webp_png(PATH_WEBP)