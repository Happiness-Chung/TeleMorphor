from smplx import SMPLX
import torch
import trimesh
import pyrender
import imageio
import numpy as np
from tqdm import tqdm
import os
from scipy.spatial.transform import Rotation as R

cam_pose = np.eye(4)
cam_pose[:3, 3] = [0, -0.5, 2.0]  # X=0 (정중앙), Y=-2.0 (앞에서), Z=1.2 (약간 위)
cam_pose[:3, :3] = R.from_euler('x', 0, degrees=True).as_matrix()  # 살짝 내려보게


# os.environ["PYOPENGL_PLATFORM"] = "egl"
data = np.load("C:/Users/user/OneDrive/바탕 화면/code/VE/smpl_data/001200.npy", allow_pickle=True).item()
# SMPLX 모델 불러오기
model = SMPLX(model_path='C:/Users/user/OneDrive/바탕 화면/code/VE/models/smplx', gender='male')

# 예시용 랜덤 모션 시퀀스 만들기 (여기엔 60프레임)
num_frames = 60
body_poses = torch.randn(num_frames, 63) * 0.2
global_orients = torch.zeros(num_frames, 3)
transls = torch.zeros(num_frames, 3)

body_poses = torch.tensor(data['bdata_poses'])
global_poses = torch.tensor(data['bdata_trans'])[:, :3]
transls = torch.tensor(data['bdata_trans'])[:, 3:]

# # bdata_poses 값 (예: data['bdata_poses'])
# bdata_poses = data['bdata_poses']

# # bdata_trans 값 (예: data['bdata_trans'])
# bdata_trans = data['bdata_trans']

# ## 데이터의 첫 60프레임만 사용하려면 인덱싱을 통해 적절한 프레임만 선택
# bdata_poses_60 = bdata_poses[:60, :63]  # 첫 60프레임과 첫 63개의 요소 선택
# bdata_trans_60 = bdata_trans[:60, :]    # 첫 60프레임에 대한 전체 translation 값

# # 데이터를 body_poses에 할당
# body_poses[:, :] = torch.tensor(bdata_poses_60)  # 63D pose 데이터 할당

# # global_orients는 bdata_trans의 첫 3개의 값을 사용할 수 있음 (예: translation에서 global_orientation 추출)
# global_orients[:, :] = torch.tensor(bdata_trans_60)[:, :3]  # 첫 3개 값 (x, y, z)를 오리엔테이션으로 사용

# # transls는 bdata_trans의 나머지 부분을 사용 (예: translation 데이터의 나머지 부분 사용)
# transls[:, :] = torch.tensor(bdata_trans_60)[:, 3:]  # translation 값 할당

# 결과 확인
print("body_poses:", body_poses)
print("global_orients:", global_orients)
print("transls:", transls)

# 렌더링 설정
width, height = 640, 480
renderer = pyrender.OffscreenRenderer(viewport_width=width, viewport_height=height)
scene = pyrender.Scene()
camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0)
light = pyrender.DirectionalLight(color=np.ones(3), intensity=2.0)
scene.add(camera, pose=cam_pose)
scene.add(light, pose=np.eye(4))

images = []

# 프레임별로 mesh 만들고 렌더링
for i in tqdm(range(num_frames)):
    output = model(
        body_pose=body_poses[i].unsqueeze(0),
        global_orient=global_orients[i].unsqueeze(0),
        transl=transls[i].unsqueeze(0)
    )
    vertices = output.vertices.detach().cpu().numpy().squeeze()
    faces = model.faces
    color_rgba = np.tile([135, 206, 235, 255], (vertices.shape[0], 1))  # 밝은 살색 RGBA
    mesh = trimesh.Trimesh(vertices, faces, vertex_colors=color_rgba, process=False)

    # 씬 초기화 및 mesh 추가
    scene.clear()
    scene.add(pyrender.Mesh.from_trimesh(mesh), 'mesh')
    scene.add(camera, pose=cam_pose)
    scene.add(light, pose=cam_pose)

    color, _ = renderer.render(scene)
    images.append(color)

renderer.delete()

# mp4로 저장
imageio.mimsave('smplx_motion.mp4', images, fps=30)
print("✅ 저장 완료: smplx_motion.mp4")