import cv2
import numpy as np

global index
index = 0

# 원본 이미지를 불러옵니다. (사용자가 올린 이미지로 대체)
name = "4"
image = cv2.imread('D:/temp/iter{}.png'.format(name))

# 포즈 맵을 그릴 빈 캔버스를 원본 이미지 크기로 생성 (검정 배경)
pose_map = np.zeros_like(image)

# 마우스로 클릭한 관절 좌표를 저장할 리스트
points_group1 = []
points_group2 = []
points_group3 = []

# 색상 리스트 (RGB 포맷으로 다양한 색상 설정)
dots1 = [ # 9
    (170, 0, 255),
    (255, 0, 255),
    (0, 85, 255),
    (0, 170, 255),
    (0, 255, 255),
    (0, 255, 170),
    (0, 255, 255),
    (0, 170, 255),
    (0, 85, 255),
    (0, 255, 85),
    (170, 0, 255),
    (255, 0, 255),
    (0, 85, 255),
    (0, 170, 255),
    (0, 255, 255),
    (0, 255, 170),
    (0, 255, 255),
    (0, 170, 255),
    (0, 85, 255),
    (0, 255, 85),
]

dots2 = [ # 9
    (170, 0, 255),
    (255, 0, 255),
    (0, 85, 255),
    (0, 170, 255),
    (0, 255, 255),
    (0, 255, 170),
    (0, 255, 255),
    (0, 170, 255),
    (0, 85, 255),
    (0, 255, 85),
]

dots3 = [ # 8
    (0, 255, 0),
    (85, 255, 0),
    (0, 255, 0),
    (0, 255, 85),
    (0, 85, 255),
    (170, 255, 0),
    (255, 255, 0),
    (255, 170, 0),
]

lines1 = [ # 8
    (153, 0, 102),
    (153, 0, 0),
    (0, 0, 153),
    (0, 102, 153),
    (0, 153, 153),
    (0, 153, 153),
    (0, 102, 153),
    (0, 0, 153),
]

lines2 = [ # 8
    (153, 0, 102),
    (153, 0, 0),
    (0, 0, 153),
    (0, 102, 153),
    (0, 153, 153),
    (0, 153, 153),
    (0, 102, 153),
    (0, 0, 153),
]

lines3 = [ # 7
    (0, 51, 153),
    (0, 153, 102),
    (0, 153, 51),
    (0, 153, 51),
    (0, 153, 102),
    (0, 51, 153),
    (0, 153, 0)
]

# 작업 그룹 선택 (1: dots, lines / 2: dots2, lines2)
mode = 1

# 마우스 클릭 이벤트 함수
def click_event(event, x, y, flags, param):
    global index, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        if mode == 1:
            points_group1.append((x, y))
            dot_index = (len(points_group1) - 1) % len(dots1)
            cv2.circle(pose_map, (x, y), 10, dots1[dot_index], -1)

            if len(points_group1) > 1:
                line_index = (len(points_group1) - 2) % len(lines1)
                cv2.line(pose_map, points_group1[-2], points_group1[-1], lines1[line_index], 7)
        elif mode == 2:
            points_group2.append((x, y))
            dot_index = (len(points_group2) - 1) % len(dots2)
            cv2.circle(pose_map, (x, y), 10, dots2[dot_index], -1)

            if len(points_group2) > 1:
                line_index = (len(points_group2) - 2) % len(lines2)
                cv2.line(pose_map, points_group2[-2], points_group2[-1], lines2[line_index], 7)
        elif mode == 3:
            points_group3.append((x, y))
            dot_index = (len(points_group3) - 1) % len(dots3)
            cv2.circle(pose_map, (x, y), 10, dots3[dot_index], -1)

            if len(points_group3) > 1:
                line_index = (len(points_group3) - 2) % len(lines3)
                cv2.line(pose_map, points_group3[-2], points_group3[-1], lines3[line_index], 7)

        # 원본 이미지와 포즈 맵을 중첩하여 화면에 표시
        combined_image = cv2.addWeighted(image, 0.5, pose_map, 0.5, 0)
        cv2.imshow("Pose Map", combined_image)

# 원본 이미지를 띄우고 마우스 이벤트 설정
cv2.imshow("Pose Map", image)
cv2.setMouseCallback("Pose Map", click_event)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        # '1'을 누르면 dots, lines 사용 (그룹 1)
        mode = 1
        print("Switched to mode 1 (dots, lines)")
    elif key == ord('2'):
        # '2'를 누르면 dots2, lines2 사용 (그룹 2)
        mode = 2
        print("Switched to mode 2 (dots2, lines2)")
    elif key == ord('3'):
        # '2'를 누르면 dots2, lines2 사용 (그룹 2)
        mode = 3
        print("Switched to mode 2 (dots2, lines2)")
    elif key == ord('s'):
        # 's'를 누르면 포즈 맵만 저장
        cv2.imwrite('D:/extract/extract/sending/{}.png'.format(name), pose_map)
    elif key == ord('q'):
        # 'q'를 누르면 종료하고, 최종 포즈 맵을 저장
        cv2.imwrite('D:/temp/{}.png'.format(name), pose_map)
        break

cv2.destroyAllWindows()