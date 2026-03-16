import os
from PIL import Image

pairs = [
    ("3 portes avant.jpg", "3 portes apres.jpg", "3_portes_combined.jpg"),
    ("mur blanc avatn.jpg", "mur blanc apres.jpg", "mur_blanc_combined.jpg"),
    ("2024-10-29.jpg", "2025-11-10.jpg", "facade_maison_combined.jpg")
]

source_dir = r"D:\1. AI\Antigravity\a. images renovationnDefrance"
dest_dir = r"D:\1. AI\Antigravity\renovation-defrance-v2"

for img1, img2, out_name in pairs:
    try:
        path1 = os.path.join(source_dir, img1)
        path2 = os.path.join(source_dir, img2)
        out_path = os.path.join(dest_dir, out_name)
        
        img_avant = Image.open(path1)
        img_apres = Image.open(path2)
        
        # Determine target height (we want them to be exactly the same height)
        target_height = min(img_avant.height, img_apres.height)
        
        # Resize images to match target_height while maintaining aspect ratio
        w_avant = int((target_height / img_avant.height) * img_avant.width)
        img_avant = img_avant.resize((w_avant, target_height), Image.Resampling.LANCZOS)
        
        w_apres = int((target_height / img_apres.height) * img_apres.width)
        img_apres = img_apres.resize((w_apres, target_height), Image.Resampling.LANCZOS)
        
        width = img_avant.width + img_apres.width
        
        # Create new image
        combined = Image.new('RGB', (width, target_height))
        combined.paste(img_avant, (0, 0))
        combined.paste(img_apres, (img_avant.width, 0))
        
        combined.save(out_path)
        print(f"Saved: {out_name}")
    except Exception as e:
        print(f"Error processing {out_name}: {e}")
