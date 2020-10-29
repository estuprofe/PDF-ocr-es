from googletrans import Translator

translator=Translator()
outfile = "traducido.txt"

original= open("caracteres_ocr.txt")
f = open(outfile, "a")
for lineas in original:
    info=translator.translate(lineas, dest='es')
    
    texto=info.text.encode('cp1252', errors='ignore')
    texto=texto.decode('cp1252', errors='ignore')
    texto=texto+"\n"
    print(texto)
    f.write(texto)
f.close()
original.close()
