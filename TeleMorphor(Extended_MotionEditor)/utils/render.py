import os
import trimesh
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import io
from tqdm import tqdm

folder_path = "C:/Users/user/OneDrive/바탕 화면/code/VE/exported_objs"
output_path = "D:/videos/output.mp4"

obj_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".obj")])
frames = []

for obj_file in tqdm(obj_files):
    try:
        mesh = trimesh.load(os.path.join(folder_path, obj_file))
        
        # 빈 mesh 건너뛰기
        if mesh.is_empty:
            print(f"⚠️ Skipped empty mesh: {obj_file}")
            continue

        scene = mesh.scene()
        png_data = scene.save_image(resolution=(640, 480), visible=True)

        # 바이너리에서 이미지 읽기
        image = imageio.imread(io.BytesIO(png_data))

        # numpy array만 append
        if isinstance(image, (list, tuple)) or image is None:
            raise ValueError(f"Invalid image from {obj_file}")
        frames.append(image)

    except Exception as e:
        print(f"❌ Failed to render {obj_file}: {e}")

# 마지막 점검
if not frames:
    raise ValueError("No valid frames rendered. Cannot create video.")

# mp4 저장
imageio.mimsave(output_path, frames, fps=30)
print(f"✅ 저장 완료: {output_path}")