import json
import numpy as np

def quaternion_to_rotation_matrix(qw, qx, qy, qz):
    """쿼터니언을 3x3 회전 행렬로 변환"""
    q = np.array([qw, qx, qy, qz], dtype=np.float64)
    n = np.dot(q, q)
    if n < np.finfo(q.dtype).eps:
        return np.identity(3)
    q *= np.sqrt(2.0 / n)
    q = np.outer(q, q)
    rot_matrix = np.array([
        [1.0 - q[2, 2] - q[3, 3], q[1, 2] - q[3, 0], q[1, 3] + q[2, 0]],
        [q[1, 2] + q[3, 0], 1.0 - q[1, 1] - q[3, 3], q[2, 3] - q[1, 0]],
        [q[1, 3] - q[2, 0], q[2, 3] + q[1, 0], 1.0 - q[1, 1] - q[2, 2]]
    ], dtype=np.float64)
    return rot_matrix

def parse_colmap_images_file(images_file):
    """COLMAP에서 생성된 images.txt 파일을 파싱하여 포즈를 추출"""
    frames = []
    with open(images_file, 'r') as f:
        for line in f.readlines():
            # 각 라인이 숫자로 시작하는지 확인하여 카메라 포즈 정보가 포함된 줄만 파싱
            if line[0].isdigit():
                elems = line.split()
                if len(elems) == 10 and elems[9].endswith(".png"):
                    qw, qx, qy, qz = map(float, elems[1:5])  # 쿼터니언
                    tx, ty, tz = map(float, elems[5:8])  # 번역
                    image_name = elems[9].split(".")[0]  # 파일 이름
                    
                    # 쿼터니언을 회전 행렬로 변환
                    rotation_matrix = quaternion_to_rotation_matrix(qw, qx, qy, qz)
                    
                    # 4x4 변환 행렬을 생성
                    transform_matrix = np.eye(4)
                    transform_matrix[:3, :3] = rotation_matrix  # 3x3 회전 행렬
                    transform_matrix[:3, 3] = [tx, ty, tz]  # 번역 벡터
                    
                    frame = {
                        "file_path": f"./images/{image_name}.png",  # 이미지 파일 경로
                        "rotation": 0.0,  # 필요에 따라 회전 값 수정 가능
                        "transform_matrix": transform_matrix.tolist()  # 리스트로 변환
                    }
                    
                    frames.append(frame)

    # NeRF 포맷에 맞게 JSON 파일로 변환
    output = {
        "camera_angle_x": 0.6911112070083618,  # 카메라 FOV (필요에 따라 수정 가능)
        "frames": frames
    }
    return output

# COLMAP 이미지 파일 경로
nerf_data = parse_colmap_images_file("C:/Users/user/OneDrive/바탕 화면/code/VE/images.txt")

# NeRF 포맷에 맞게 JSON으로 저장
with open('camera_poses3.json', 'w') as f:
    json.dump(nerf_data, f, indent=4)

print("camera_poses.json 파일이 생성되었습니다.")
