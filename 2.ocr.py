
import os 
import pytesseract
from PIL import Image 


outfile = "caracteres_ocr.txt"

jpgs = os.listdir("imagenes")
f = open(outfile, "a") 
for jpg in jpgs:
    
    print(f"Pasando a letra {jpg}")
    text = str(pytesseract.image_to_string(Image.open("imagenes\\"+jpg)))
    text = text.replace('-\n', '')
    f.write(text)    
f.close()       
