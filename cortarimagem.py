from PIL import Image
import os

def slice_image(image_path, output_dir, rows=8, cols=8):
    # Abra a imagem
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Dimensões das sub-imagens
   Number_of_blocks_width = int(img_width/8)
   Number_of_blocks_height = int(img_height/8)

    # Certifique-se de que o diretório de saída existe
    os.makedirs(output_dir, exist_ok=True)

    # Fatiar a imagem em 8x8
    for row in range(Number_of_blocks_width):
        for col in range(Number_of_blocks_height):
            left = col * cols
            upper = row * rows
            right = (col + 1) * cols
            lower = (row + 1) * rows

            # Recortar a sub-imagem
            sub_img = img.crop((left, upper, right, lower))

            # Salvar a sub-imagem
            sub_img_name = f"sub_img_{row}_{col}.png"
            sub_img.save(os.path.join(output_dir, sub_img_name))

    print(f"Imagem fatiada em {rows*cols} sub-imagens.")

# Exemplo de uso:
image_path = 'sua_imagem.png'  # Substitua pelo caminho da sua imagem
output_dir = 'output_images'  # Substitua pelo diretório de saída desejado

slice_image(image_path, output_dir)
