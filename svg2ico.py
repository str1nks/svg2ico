import io
import resvg_python
from PIL import Image, ImageChops, ImageDraw

SIZE = 1024
RADIUS = int(SIZE * 0.22)  # степень скругления

with open("icon.svg", "r", encoding="utf-8") as f:
    svg_data = f.read()

png_data = resvg_python.svg_to_png(svg_data)

img = Image.open(io.BytesIO(bytes(png_data))).convert("RGBA")
img = img.resize((SIZE, SIZE), Image.Resampling.LANCZOS)

mask = Image.new("L", (SIZE, SIZE), 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, SIZE - 1, SIZE - 1), RADIUS, fill=255)
img.putalpha(ImageChops.multiply(img.getchannel("A"), mask))

img.save(
    "app.ico",
    format="ICO",
    sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
)

print("Иконка app.ico успешно создана!")
