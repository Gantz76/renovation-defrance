from PIL import Image, ImageDraw, ImageFont

img_avant = Image.open('avant.jpg')
img_apres = Image.open('apres.jpg')

# Calculate dimensions
width = img_avant.width + img_apres.width
height = max(img_avant.height, img_apres.height)

# Create new image
combined = Image.new('RGB', (width, height))
combined.paste(img_avant, (0, 0))
combined.paste(img_apres, (img_avant.width, 0))

# Try to add text if possible
try:
    draw = ImageDraw.Draw(combined)
    # Simple text without custom font
    draw.text((10, 10), "AVANT", fill="white")
    draw.text((img_avant.width + 10, 10), "APRES", fill="white")
except:
    pass

combined.save('avant_apres_combined.jpg')
print("Image saved as avant_apres_combined.jpg")
