# Import libraries 



from pdf2image import pdfinfo_from_path,convert_from_path

print("1")
# Path of the pdf 
pdf_file = "original.pdf"

''' 
Part #1 : Converting PDF to images 
'''
# Store all the pages of the PDF in a variable
for i in range(1,500, 10):
    print("2")
    pages= convert_from_path(pdf_file, first_page=i,last_page=i+9 , fmt='jpeg') 
    print("3")
# Counter to store images of each page of PDF to image 
    image_counter=i

# Iterate through all the pages stored above
    for page in pages:

    # Declaring filename for each page of PDF as JPG 
    # For each page, filename will be: 
    # PDF page 1 -> page_1.jpg 
    # PDF page 2 -> page_2.jpg 
    # PDF page 3 -> page_3.jpg 
    # .... 
    # PDF page n -> page_n.jpg
        if image_counter < 10:
            filename = "imagenes\pagina_00"+str(image_counter)+".jpg"
        elif image_counter<100:
            filename = "imagenes\pagina_0"+str(image_counter)+".jpg"
        else:
            filename="imagenes\pagina_"+str(image_counter)+".jpg"
    
    # Save the image of the page in system 
        page.save(filename, 'JPEG') 

    # Increment the counter to update filename 
        image_counter = image_counter + 1
        print(f"extrayendo {filename}")





