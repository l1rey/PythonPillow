from PIL import Image

def main():
    im = Image.open("pythonpillow.jpg")
    print(im.format, im.size, im.mode)

    size = (128, 128)
    outfile = "picturepython.jpg"
    im.thumbnail(size)
    im.save(outfile, "JPEG")

if __name__ == '__main__':
    main()
