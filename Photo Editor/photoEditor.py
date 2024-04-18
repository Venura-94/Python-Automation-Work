from PIL import Image,ImageEnhance,ImageFilter
import os 

path = './imgs' #folder for unedited images
pathout = './Automation/output' #folder for edited images

try:

    for filename in os.listdir(path):
        img= Image.open(f"{path}/{filename}")

        # Sharpnig and BW # Image processing steps...
        edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-180)


        #Contrast
        factor = 2.7
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)
        ####

        clean_name = os.path.splitext(filename)[0] #since os.path is returning the tuple and we call the first element by using 0
    
        # Debugging print statements
        print("Pathout:", pathout)
        print("Clean Name:", clean_name)

        edit.save(f'.{pathout}/{clean_name}_edited.jpg')

except Exception as e:
    #Error handling
    print(f'Error : {e}')




