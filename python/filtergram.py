import filter

def main():
    filename = input('enter the name of the image file to edit')

    img = filter.load_img(filename)

    filterchoice = input('what filter do you want? Obamicon , noice')


    if filterchoice == 'obamicon':
        newimg = filter.obamicon(img)
        filter.save_img(newimg , filename + '-obamicon.jpg')

    if filterchoice == 'noice':
        newimg = filter.noice(img)
        filter.save_img(newimg ,filename + '-noice.jpg')


if __name__ == "__main__":
  main()
