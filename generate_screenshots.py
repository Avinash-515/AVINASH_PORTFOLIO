from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

out = Path('screenshots')
out.mkdir(exist_ok=True)
labels = [
    'Hide Data Screen',
    'Success & Blockchain Confirm',
    'Extract Data Screen',
    'Verify & Analytics'
]
for i, label in enumerate(labels, start=1):
    img = Image.new('RGB', (900, 520), (32, 44, 90))
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('arial.ttf', 40)
    except Exception:
        f = ImageFont.load_default()
    bbox = d.textbbox((0, 0), label, font=f)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((900-w)/2, (520-h)/2), label, font=f, fill=(184, 233, 255))
    img.save(out / f'steg-0{i}.png')
print('Created', len(labels), 'screenshots in', out)
