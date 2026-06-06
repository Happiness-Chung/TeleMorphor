import cv2
import numpy as np

# 함수: 이미지 축소 및 패딩 처리
def shrink_and_pad_resize(image_path, target_size, scale_factor):
    """
    이미지를 scale_factor만큼 축소한 후, 가운데 정렬하여 나머지 영역을 0으로 패딩하고 최종 크기로 리사이즈.
    
    :param image_path: str, 이미지 파일 경로
    :param target_size: tuple, (width, height)로 지정한 최종 이미지 크기
    :param scale_factor: float, 이미지를 축소할 배율
    :return: numpy.ndarray, 축소, 패딩 및 리사이즈된 이미지
    """
    # 이미지 읽기
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if image is None:
        raise ValueError(f"Image not found at {image_path}")

    # 원본 이미지 크기 가져오기
    original_height, original_width = image.shape[:2]

    # 이미지 축소
    shrunk_width = int(original_width * scale_factor)
    shrunk_height = int(original_height * scale_factor)
    shrunk_image = cv2.resize(image, (shrunk_width, shrunk_height), interpolation=cv2.INTER_LINEAR)

    # 패딩 크기 계산
    target_width, target_height = target_size
    pad_width = max(target_width - shrunk_width, 0) // 2
    pad_height = max(target_height - shrunk_height, 0) // 2

    # 이미지 패딩 처리
    padded_image = cv2.copyMakeBorder(
        shrunk_image,
        top=pad_height,
        bottom=pad_height,
        left=pad_width,
        right=pad_width,
        borderType=cv2.BORDER_CONSTANT,
        value=0  # 패딩 값을 검정색(RGB: 0, 0, 0)으로 설정
    )

    # 패딩 후 크기 조정 (지정된 크기로 리사이즈)
    resized_image = cv2.resize(padded_image, (target_width, target_height), interpolation=cv2.INTER_LINEAR)

    return resized_image

# 경로와 타겟 크기 설정
image_path = "D:/temp/enlarged_2.png"  # 이미지 경로
target_size = (512, 512)  # 최종 크기 (width, height)
scale_factor = 0.8  # 이미지 축소 비율

# 축소, 패딩 및 리사이즈 실행
result_image = shrink_and_pad_resize(image_path, target_size, scale_factor)

# 결과 이미지 저장 및 확인
cv2.imwrite("D:/temp/shrunk_and_padded_2.png", result_image)
# cv2.imshow("Shrunk, Padded, and Resized Image", result_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
