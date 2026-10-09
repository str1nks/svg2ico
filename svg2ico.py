import io
import resvg_python
from PIL import Image, ImageChops, ImageDraw

SIZE = 1024
RADIUS = int(SIZE * 0.22)  # степень скругления

# 1. Читаем SVG файл
with open("icon.svg", "r", encoding="utf-8") as f:
    svg_data = f.read()

# 2. Рендерим в PNG (resvg_python возвращает list[int])
png_data = resvg_python.svg_to_png(svg_data)

# 3. Преобразуем list[int] в bytes для io.BytesIO и открываем в Pillow
img = Image.open(io.BytesIO(bytes(png_data))).convert("RGBA")
img = img.resize((SIZE, SIZE), Image.Resampling.LANCZOS)

# 4. Маска со скруглёнными углами
mask = Image.new("L", (SIZE, SIZE), 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, SIZE - 1, SIZE - 1), RADIUS, fill=255)
img.putalpha(ImageChops.multiply(img.getchannel("A"), mask))

# 5. Сохраняем в app.ico
img.save(
    "app.ico",
    format="ICO",
    sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
)

print("Иконка app.ico успешно создана!")