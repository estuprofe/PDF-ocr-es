import PyPDF2
import os

def extrae_texto():
    
    f = open(outfile, "a") 
    for i in range(total_paginas):
        pagina=pdf.getPage(i)
        contenido=pagina.extractText()
        print(contenido)
        f.write(contenido) 
    f.close()


outfile = "caracteres_ocr.txt"
pdf_archivo = open("original.pdf", 'rb')
pdf = PyPDF2.PdfFileReader(pdf_archivo)
modo_pagina = pdf.getPageMode()
print(f"modo de página: {modo_pagina}")#.encode("utf8").decode("cp1252")
total_paginas = pdf.getNumPages()
print(f"páginas: {total_paginas}")
print(pdf.documentInfo)
extrae_texto()



