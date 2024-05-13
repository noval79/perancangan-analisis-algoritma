from PIL import Image, ImageDraw
import random

# Ukuran peta
map_size = (150, 150)

# Membuat gambar baru dengan ukuran peta
img = Image.new('RGB', map_size, color = 'green')
d = ImageDraw.Draw(img)

# Fungsi untuk menggambar bangunan


# Menggambar jalan


# Menggambar bangunan


# Menambahkan detail pohon dan lapangan



img.save('city_map.png')
