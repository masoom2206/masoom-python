# Using Pillow libraray

from PIL import Image, ImageFilter

img = Image.open("Learning/Udemy/Scripting/ImageProcess/Pokedesk/pikachu.jpg")

# # Image object with detail like: <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x1033470E0>
# print(img)
# # Get image format
# print(img.format)
# # Get image size
# print(img.size)
# # Get image color mode
# print(img.mode)
# # Get image methods 
# print(dir(img))
# # Get image width/height
# print(img.width)
# print(img.height)

# # Save image as BLUR
# filtered_image  = img.filter(ImageFilter.BLUR)
# filtered_image.save("Learning/Udemy/Scripting/ImageProcess/PokeUpdated/pikachu-blur.png", "png")

# # # Save image as SMOOTH
# filtered_image  = img.filter(ImageFilter.SMOOTH)
# filtered_image.save("Learning/Udemy/Scripting/ImageProcess/PokeUpdated/pikachu-smooth.png", "png")

# # # Save image as SHARPEN
# filtered_image  = img.filter(ImageFilter.SHARPEN)
# filtered_image.save("Learning/Udemy/Scripting/ImageProcess/PokeUpdated/pikachu-sharpen.png", "png")


# # # Save/convert image as gray (Black/White)
# filtered_image  = img.convert("L")
# filtered_image.save("Learning/Udemy/Scripting/ImageProcess/PokeUpdated/pikachu-gray.png", "png")
# # Open the converted image
# filtered_image.show()

# # # Rotate the image
# filtered_image  = img.rotate(90)
# filtered_image.save("Learning/Udemy/Scripting/ImageProcess/PokeUpdated/pikachu-rotate-90.png", "png")
# filtered_image  = img.rotate(45)
# filtered_image.save("Learning/Udemy/Scripting/ImageProcess/PokeUpdated/pikachu-rotate-45.png", "png")
# # Open the converted image
# filtered_image.show()


# # Resize the image
# filtered_image  = img.resize((300, 300))
# filtered_image.save("Learning/Udemy/Scripting/ImageProcess/PokeUpdated/pikachu-resize-300x300.png", "png")
# # Open the converted image
# filtered_image.show()

# # Crop the image
# box = (100, 100, 400, 400)
# filtered_image  = img.crop(box)
# filtered_image.save("Learning/Udemy/Scripting/ImageProcess/PokeUpdated/pikachu-crop-100x100x400x400.png", "png")
# # Open the converted image
# filtered_image.show()

# # resize the image with aspect ration
# img.thumbnail((100,50))
# img.save("Learning/Udemy/Scripting/ImageProcess/PokeUpdated/pikachu-thumb-100x50", "png")
# img.show()
