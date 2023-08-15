from PIL import Image


im = Image.open("pythonpillow.jpg")


def main():
    print(im.format, im.size, im.mode)

    size = (128, 128)
    outfile = "picturepython.jpg"
    im.thumbnail(size)
    im.save(outfile, "JPEG")


def crop_image():
    box = (110, 110, 400, 400)
    region = im.crop(box)
    im.save("picturepython2.jpg", "JPEG")


if __name__ == '__main__':
    main()
