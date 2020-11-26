from PIL import Image, ImageDraw

filename = 'C:/Users/ADINARAYANAREDDY/Python/me.jpeg'

# load image
img = Image.open(filename)

# crop image 
width, height = img.size
x = (width - height)//2
print(height)
img_cropped = img.crop((x, 0, x+height, height))

# create grayscale image with white circle (255) on black background (0)
mask = Image.new('L', img_cropped.size)
mask_draw = ImageDraw.Draw(mask)
width, height = img_cropped.size
mask_draw.ellipse((0, 0, width, height), fill=255)
#mask.show()

# add mask as alpha channel
img_cropped.putalpha(mask)

# save as png which keeps alpha channel 
img_cropped.save('circle.png')

img_cropped.show()
