import bpy
import numpy as np

# 저장된 포즈 시퀀스를 불러옵니다.
pose_seq_np_n = np.load("C:/Users/user/OneDrive/바탕 화면/code/VE/HumanML3D/HumanML3D/new_joints/012314.npy", allow_pickle=True)

# Blender에서의 3D 모델에 대한 설정
model = bpy.context.object  # Blender에서 사용할 객체

print(type(model))

# 포즈 시퀀스를 애니메이션으로 변환
for frame_id, pose in enumerate(pose_seq_np_n):
    bpy.context.scene.frame_set(frame_id)  # 프레임 설정
    # 포즈 데이터를 기반으로 3D 모델의 포즈 업데이트
    model.location = pose[0]  # 예시: 위치 업데이트
    model.rotation_euler = pose[:3]  # 예시: 회전 업데이트
    model.keyframe_insert(data_path="location", frame=frame_id)
    model.keyframe_insert(data_path="rotation_euler", frame=frame_id)

# 애니메이션을 렌더링하여 비디오로 저장
bpy.context.scene.render.filepath = 'output_video.mp4'
bpy.ops.render.render(animation=True)