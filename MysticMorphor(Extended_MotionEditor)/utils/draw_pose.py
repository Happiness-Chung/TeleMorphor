import cv2
import numpy as np

global index
index = 0

# 원본 이미지를 불러옵니다. (사용자가 올린 이미지로 대체)
name = "0000"
image = cv2.imread('resolution/case-24/MotionEditor256/{}.png'.format(name))

# 포즈 맵을 그릴 빈 캔버스를 원본 이미지 크기로 생성 (검정 배경)
pose_map = np.zeros_like(image)

# 마우스로 클릭한 관절 좌표를 저장할 리스트
points = []

# 색상 리스트 (RGB 포맷으로 다양한 색상 설정)
dots = [
    (170,0,255),
    (255,0,255),
    (0,85,255),
    (0,170,255),
    (0,255,255),
    (0,255,170),
    (0,255,255),
    (0,170,255),
    (0,85,255),
    (0,255,85),
    (0,255,0),
    (85,255,0),
    (0,255,0),
    (0,255,85),
    (0,85,255),
    (170,255,0),
    (255,255,0),
    (255,170,0),
    (255,255,0),
    (170,255,0),
    (0,85,255),
    (255,85,0),
    (255,0,0),
    (255,0,85)
]

lines = [
    (153,0,102),
    (153,0,0),
    (0,0,153),
    (0,102,153),
    (0,153,153),
    (0,153,153),
    (0,102,153),
    (0,0,153),
    (0,51,153),
    (0,153,102),
    (0,153,51),
    (0,153,51),
    (0,153,102),
    (0,51,153),
    (0,153,0),
    (0,153,0),
    (51,153,0),
    (102,153,0),
    (51,153,0),
    (0,153,0),
    (153,153,0),
    (153,102,0),
    (153,51,0)
]

# 마우스 클릭 이벤트 함수
def click_event(event, x, y, flags, param):
    global index
    if event == cv2.EVENT_LBUTTONDOWN:
        
        # 좌표를 저장
        points.append((x, y))

        # 클릭한 좌표에 포즈 맵(검정 배경) 상에서 원 그리기
        dot_index = (len(points) - 1) % len(dots)  # 클릭 순서에 따른 색상 선택
        print(dot_index)
        cv2.circle(pose_map, (x, y), 7, dots[index], -1)

        # 두 개 이상의 포인트가 있으면 선으로 연결
        line_index = (len(points) - 1) % len(dots) - 1
        if len(points) > 1:
            cv2.line(pose_map, points[-2], points[-1], lines[index-1], 5)

        # 원본 이미지와 포즈 맵을 중첩하여 화면에 표시
        combined_image = cv2.addWeighted(image, 0.5, pose_map, 0.5, 0)
        cv2.imshow("Pose Map", combined_image)
        index += 1

# 원본 이미지를 띄우고 마우스 이벤트 설정
cv2.imshow("Pose Map", image)
cv2.setMouseCallback("Pose Map", click_event)
new_name = str(int(name) + 1).zfill(len(name))
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # 's'를 누르면 포즈 맵만 저장
        cv2.imwrite('D:/extract/c1/pose/{}.png'.format(name), pose_map)
    elif key == ord('q'):
        # 'q'를 누르면 종료하고, 최종 포즈 맵을 저장
        cv2.imwrite('resolution/case-24/MotionEditor256/openposefull/{}.png'.format(name), pose_map)
        break

cv2.destroyAllWindows()
