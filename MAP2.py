from PIL import Image, ImageDraw

# Ukuran peta dalam cells
map_size_cells = (150, 150)

# Ukuran peta dalam piksel
map_size = (map_size_cells[0]*10, map_size_cells[1]*10)

# Membuat gambar baru dengan ukuran peta
img = Image.new('RGB', map_size, color='green')
d = ImageDraw.Draw(img)

# Fungsi untuk menggambar rumah kecil dengan segitiga merah di atasnya
def draw_house(map_img, pos):
    cell_size = 10  # Ukuran setiap sel dalam piksel
    house_size = (1 * cell_size, 2 * cell_size)  # Ukuran rumah dalam piksel
    house_img = Image.new('RGBA', house_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(house_img)

    # Gambar kotak biru (bagian rumah)
    box_top_left = (0, cell_size)
    box_bottom_right = (1 * cell_size, 2 * cell_size)
    draw.rectangle([box_top_left, box_bottom_right], fill='blue', outline='black')

    # Gambar segitiga merah (atap rumah)
    triangle_top = (cell_size // 2, 0)
    triangle_left = (0, cell_size)
    triangle_right = (1 * cell_size, cell_size)
    draw.polygon([triangle_top, triangle_left, triangle_right], fill='red', outline='black')

    pos_pixels = (pos[0]*cell_size, pos[1]*cell_size)  # Posisi rumah dalam piksel
    map_img.paste(house_img, pos_pixels, house_img)

# Fungsi untuk menggambar bangunan
def draw_building(map_img, pos, size, color, inner_squares=0):
    cell_size = 10  # Ukuran setiap sel dalam piksel
    building_size = (size[0]*cell_size, size[1]*cell_size)  # Ukuran bangunan dalam piksel
    building_img = Image.new('RGBA', building_size, color)
    if inner_squares > 0:
        draw = ImageDraw.Draw(building_img)
        square_size = (1.5*cell_size, 1.5*cell_size)  # Ukuran kotak dalam di dalam bangunan dalam piksel
        total_inner_width = inner_squares * square_size[0] + (inner_squares - 1) * cell_size
        start_x = (building_size[0] - total_inner_width) // 2
        for i in range(inner_squares):
            square_pos = (start_x + i * (square_size[0] + cell_size), (building_size[1] - square_size[1]) // 2)  # Posisi kotak di dalam bangunan
            draw.rectangle([square_pos, (square_pos[0] + square_size[0], square_pos[1] + square_size[1])], fill='gray')
    pos_pixels = (pos[0]*cell_size, pos[1]*cell_size)  # Posisi bangunan dalam piksel
    map_img.paste(building_img, pos_pixels, building_img)

# Menggambar bangunan besar
draw_building(img, (20, 20), (10, 5), 'blue', 2)  # Bangunan besar

# Menggambar bangunan sedang
for i in range(4):
    draw_building(img, (30 + i * 15, 30), (5, 3), 'red', 1)  # Bangunan sedang

# Menggambar bangunan kecil berwarna kuning
for i in range(10):
    draw_building(img, (10 + i * 15, 50), (2, 2), 'yellow')  # Bangunan kecil

# Menggambar rumah berwarna biru dengan atap merah
for i in range(10):
    draw_house(img, (10 + i * 15, 70))  # Rumah

# Menggambar jalan
d.line((0, map_size[1] // 2, map_size[0], map_size[1] // 2), fill='black', width=10)

# Simpan gambar
img.save('city_map.png')

# Tampilkan gambar
img.show()
