import os
import shutil

def extract_egg_as_folder(egg_path, extract_to):
    """
    .egg 파일을 폴더로 변환하는 함수 (압축 해제가 아닌 경우)
    """
    if not os.path.exists(egg_path):
        print(f"⚠️ 파일이 존재하지 않습니다: {egg_path}")
        return
    
    os.makedirs(extract_to, exist_ok=True)
    shutil.copytree(egg_path, extract_to, dirs_exist_ok=True)
    print(f"✅ {egg_path} 를 폴더로 변환 완료! 📂 {extract_to} 에 저장됨.")

# 사용 예시
egg_file = "D:/autopet_ct_original.egg"  # 압축을 풀 .egg 파일 경로
output_folder = "D:/"  # 압축을 풀 폴더
extract_egg_as_folder(egg_file, output_folder)