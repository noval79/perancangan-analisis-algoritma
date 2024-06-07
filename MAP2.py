from PIL import Image, ImageDraw
import random

# Ukuran peta
map_size = (150, 150)
cell_size = 30  # Ukuran sel dalam piksel
road_width = cell_size // 4  # Lebar jalan seperempat dari ukuran sel
dotted_line_length = 5  # Panjang garis putus-putus
dotted_line_gap = 5  # Jarak antara garis putus-putus

# Membuat gambar baru dengan ukuran peta
img = Image.new('RGB', map_size, color='green')
d = ImageDraw.Draw(img)

# Fungsi untuk menggambar jalan horizontal
def draw_horizontal_road(y_cell, start_x_cell, end_x_cell):
    start_x = start_x_cell * cell_size
    end_x = end_x_cell * cell_size
    y = y_cell * cell_size + (cell_size - road_width) // 2
    d.rectangle([start_x, y, end_x + cell_size, y + road_width], fill='black')
    
    # Menggambar garis putus-putus di tengah jalan
    middle_y = y + road_width // 2
    for x in range(start_x, end_x + cell_size, dotted_line_length + dotted_line_gap):
        d.line([(x, middle_y), (x + dotted_line_length, middle_y)], fill='white', width=1)

# Fungsi untuk menggambar jalan vertikal
def draw_vertical_road(x_cell, start_y_cell, end_y_cell):
    start_y = start_y_cell * cell_size
    end_y = end_y_cell * cell_size
    x = x_cell * cell_size + (cell_size - road_width) // 2
    d.rectangle([x, start_y, x + road_width, end_y + cell_size], fill='black')
    
    # Menggambar garis putus-putus di tengah jalan
    middle_x = x + road_width // 2
    for y in range(start_y, end_y + cell_size, dotted_line_length + dotted_line_gap):
        d.line([(middle_x, y), (middle_x, y + dotted_line_length)], fill='white', width=1)

# Menggambar jalan utama horizontal dan vertikal
draw_horizontal_road(3, 0, 10)
draw_vertical_road(2, 0, 4)

# Menyimpan gambar
img.save('map2.png')
