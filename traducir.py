from googletrans import Translator

translator=Translator()
outfile = "traducido.txt"

original= open("caracteres_ocr.txt")
f = open(outfile, "a")
contador=1
for lineas in original:
    info=translator.translate(lineas, dest='es')
    
    texto=info.text.encode('cp1252', errors='ignore')
    texto=texto.decode('cp1252', errors='ignore')
    texto=texto+"\n"
    print(texto)
    f.write(texto)
    print(f"-----------------------------Frase añadida {contador}---------------------")
    contador += 1
f.close()
original.close()
