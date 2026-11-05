from PIL import Image, ImageDraw, ImageFont
def make(size, name, safe):
    im = Image.new("RGB", (size, size), "#0e1116")
    d = ImageDraw.Draw(im)
    s = size * safe
    o = (size - s) / 2
    r = s * 0.32
    cx = size / 2
    # pile de pièces : 3 disques dorés + signe €
    for k, dy in enumerate((0.16, 0.0, -0.16)):
        cy = cx + dy * s
        col = ("#b8901a", "#d4a620", "#e8b923")[k]
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col, outline="#0e1116", width=max(2, size // 100))
    f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", int(s * 0.42))
    cy = cx - 0.16 * s
    d.text((cx, cy), "€", font=f, fill="#0e1116", anchor="mm")
    im.save(name)
make(192, "icon-192.png", 0.9)
make(512, "icon-512.png", 0.9)
make(512, "icon-maskable-512.png", 0.6)
