import os
from PIL import Image

def create_gif_from_folder(folder_path, gif_name="output.gif", duration=100):
    image_files = sorted([
        file for file in os.listdir(folder_path)
        if file.lower().endswith(('.png', '.jpg', '.jpeg'))
    ])

    if not image_files:
        print(f"[!] No images found in {folder_path}")
        return

    images = [Image.open(os.path.join(folder_path, f)).convert("RGB") for f in image_files]
    output_path = os.path.join("D:/extract/VE_results/case-25", gif_name)

    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        duration=duration,  # duration per frame in milliseconds
        loop=0
    )
    print(f"[✔] Saved GIF: {output_path}")

def create_gifs_in_root(root_dir):
    cnt = 1
    for subfolder in os.listdir(root_dir):
        subfolder_path = os.path.join(root_dir, subfolder)
        if os.path.isdir(subfolder_path):
            create_gif_from_folder(subfolder_path, gif_name='25-' + str(cnt) + '.gif')
            cnt += 1

# 사용 예시
root_directory = "D:/extract/VE_results/case-25"
create_gifs_in_root(root_directory)