from PIL import Image
image1 = Image.open(r'C:\Users\ADINARAYANAREDDY\Pictures\Screenshots\page2.png')
image2 = Image.open(r'C:\Users\ADINARAYANAREDDY\Pictures\Screenshots\page1.png')
im1 = image1.convert('RGB')
im2 = image2.convert('RGB')
imagelist = [im2]
im1.save(r'C:\Users\ADINARAYANAREDDY\Python\Tickets.pdf',save_all=True, append_images=imagelist)