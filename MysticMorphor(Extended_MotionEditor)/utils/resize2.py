import cv2
import numpy as np

# 함수: 이미지 확대, 패딩 및 리사이즈
def enlarge_and_pad_resize(image_path, target_size, scale_factor):
    """
    이미지를 scale_factor만큼 확대한 후, 가운데 놓고 나머지 픽셀을 0으로 패딩 처리한 후, 원하는 크기로 리사이즈.
    
    :param image_path: str, 이미지 파일 경로
    :param target_size: tuple, (width, height)로 지정한 최종 이미지 크기
    :param scale_factor: float, 이미지를 확대할 배율
    :return: numpy.ndarray, 확대, 패딩 및 리사이즈된 이미지
    """
    # 이미지 읽기
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if image is None:
        raise ValueError(f"Image not found at {image_path}")

    # 원본 이미지 크기 가져오기
    original_height, original_width = image.shape[:2]

    # 이미지 확대
    enlarged_width = int(original_width * scale_factor)
    enlarged_height = int(original_height * scale_factor)
    enlarged_image = cv2.resize(image, (enlarged_width, enlarged_height), interpolation=cv2.INTER_LINEAR)

    # 패딩 크기 계산
    target_width, target_height = target_size
    pad_width = max(target_width - enlarged_width, 0) // 2
    pad_height = max(target_height - enlarged_height, 0) // 2

    # 이미지 패딩 처리
    padded_image = cv2.copyMakeBorder(
        enlarged_image,
        top=pad_height,
        bottom=pad_height,
        left=pad_width,
        right=pad_width,
        borderType=cv2.BORDER_CONSTANT,
        value=0  # 패딩 값을 0으로 설정
    )

    # 패딩 후 크기 조정 (지정된 크기로 리사이즈)
    resized_image = cv2.resize(padded_image, (target_width, target_height), interpolation=cv2.INTER_LINEAR)

    return resized_image

# 경로와 타겟 크기 설정
image_path = "D:/temp/original2.png"  # 이미지 경로
target_size = (512, 512)  # 최종 크기 (width, height)
scale_factor = 1.6  # 이미지 확대 비율

# 확대, 패딩 및 리사이즈 실행
result_image = enlarge_and_pad_resize(image_path, target_size, scale_factor)

# 결과 이미지 저장 및 확인
cv2.imwrite("D:/temp/enlarged_2.png", result_image)
# cv2.imshow("Enlarged, Padded, and Resized Image", result_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
