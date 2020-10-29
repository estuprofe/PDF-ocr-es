# PDF-ocr-es
Librerías necesarias: pytesseract (para traducir), pdf2image (para convertir el PDF en imagen tipo PIL), y Pillow (para manejar las imágenes PIL y convertirlas en JPG)
Traduce al español un PDF hecho con imágenes y no con letras (primero extrae las JPG, luego saca caracteres y al final lo traduce al español)
1º paso: debes poner el PDF en la carpeta raíz y renombrarlo como "original.pdf" sustituyendo al archivo que hay.
2º paso: escribes "python 1.troceador.py" en la consola y te meterá todas las páginas del PDF como imágenes JPG dentro de la carpeta imágenes.
3º paso: escribes "python 2.ocr.py" en la consola y te creará el archivo "caracteres_ocr.txt" con todas las imágenes convertidas a letras.
4º paso: escribes"python 3.traducir.py" en la consola y te creará el archivo "Traducido.txt" con el texto ya traducido.
