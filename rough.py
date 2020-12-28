from PIL import Image
image1 = Image.open(r'C:\Users\ADINARAYANAREDDY\Pictures\Screenshots\activity.png')
im1 = image1.convert('RGB')
im1.save(r'C:\Users\ADINARAYANAREDDY\Python\Saved.pdf')