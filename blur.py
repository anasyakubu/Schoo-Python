from PIL import Image, ImageFilter

before = Image.open("hero.webp")
after = filter(ImageFilter.BoxBlur(1))
after.save("out.webp")