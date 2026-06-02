import zipfile
import os

def extract_egg(egg_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with zipfile.ZipFile(egg_path, 'r') as egg_file:
        egg_file.extractall(output_dir)
        print(f"Extracted {egg_path} to {output_dir}")

# 사용 예제
egg_path = "C:/Users/user/OneDrive/바탕 화면/data/MLLM/hector2021.egg"  # .egg 파일 경로
output_dir = "C:/Users/user/OneDrive/바탕 화면/data/MLLM"  # 압축 해제할 폴더 경로
extract_egg(egg_path, output_dir)
