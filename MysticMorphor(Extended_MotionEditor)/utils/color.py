import cv2
import numpy as np

# 원본 이미지를 불러옵니다. (사용자가 올린 이미지로 대체)
index = "0000"
image = cv2.imread('D:/extract/openposefull/{}.png'.format(index))

# 마우스 클릭 이벤트 함수
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # 클릭한 좌표의 BGR 값을 가져옵니다.
        b, g, r = image[y, x]
        print(f"클릭한 좌표의 BGR 값: B={b}, G={g}, R={r}")

        # 클릭한 좌표에 원을 그려 표시
        cv2.circle(image, (x, y), 5, (int(b), int(g), int(r)), -1)

        # 화면에 표시
        cv2.imshow("Image", image)

# 원본 이미지를 띄우고 마우스 이벤트 설정
cv2.imshow("Image", image)
cv2.setMouseCallback("Image", click_event)

# ESC 키를 눌러 종료할 때까지 창을 유지
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC 키
        break

cv2.destroyAllWindows()
