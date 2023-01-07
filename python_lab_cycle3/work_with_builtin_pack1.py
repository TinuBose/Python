from PIL import Image

a = input("enter image name or path:")
img = a.strip('"')
n = 3
with Image.open(img) as im:
    if img[-n:] == "png":
        b = img.strip(".png")
        im.save(b + ".jpg")
        print("png converted to jpg")
    elif img[-n:] == "jpg":
        b = img.strip(".jpg")
        im.save(b + ".png")
        print("jpg converted to png")
    else:
        print("invalid format")
