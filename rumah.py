from PIL import Image, ImageDraw

# Definisikan ukuran sel dan ukuran gambar
cell_size = 50  # Ukuran setiap sel dalam piksel
width_cells = 10  # Lebar dalam jumlah sel
height_cells = 5  # Tinggi dalam jumlah sel

# Ukuran gambar dalam piksel
img_width = width_cells * cell_size
img_height = height_cells * cell_size

# Buat gambar baru dengan latar belakang transparan
image = Image.new('RGBA', (img_width, img_height), (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Gambar kotak biru
box_top_left = (3 * cell_size, 3 * cell_size)
box_bottom_right = (7 * cell_size, 5 * cell_size)
draw.rectangle([box_top_left, box_bottom_right], fill='blue', outline='black')

# Gambar segitiga merah di atas kotak
triangle_top = (5 * cell_size, 1 * cell_size)
triangle_left = (3 * cell_size, 3 * cell_size)
triangle_right = (7 * cell_size, 3 * cell_size)
draw.polygon([triangle_top, triangle_left, triangle_right], fill='red', outline='black')

# Simpan gambar
image.save('house.png')

# Tampilkan gambar
image.show()
