# Add commands to import modules here.
from PIL import Image


#funtions
def load_img(name):
    img = Image.open(name)
    return img

def show_img(img):
    img.show()

# Parameters: The image object to save, the name to save the file as (string)
def save_img( newimg, filename):
    newimg.save(filename , "JPEG")

#       Returns: A New Image object with the filter applied.
def obamicon(img):
    pixels = img.getdata()
    newpix = []
    #intensity = 0

    darkBlue =(0,51,76)
    red = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)

    for pixel in pixels:
        intensity = sum(pixel)
        #print(intesity)
        if intensity < 182:
            newpix.append(darkBlue)
        elif intensity >= 182 or intensity < 364:
            newpix.append(red)
        elif intensity >= 364 or intensity < 546:
            newpix.append(lightBlue)
        else:
            newpix.append(yellow)

    newimg = Image.new('RGB' , img.size)
    newimg.putdata(newpix)

    return newimg
