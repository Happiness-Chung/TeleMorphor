import cv2
import numpy as np
import matplotlib.pyplot as plt

# 함수: 이미지 정규화 (0~1 범위로)
def normalize_image(image):
    return (image - np.min(image)) / (np.max(image) - np.min(image) + 1e-8)

# 함수: 절대 오차 맵 계산
def absolute_error_map(image1, image2):
    return image2 - image1

# 함수: MSE 계산
def calculate_mse(image1, image2):
    return np.mean((image1 - image2) ** 2)

# 함수: 절대 오차 맵 생성 및 시각화
def generate_absolute_error_map(image1_path, image2_path):
    # 이미지 불러오기 (Grayscale로 읽기)
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE).astype(np.float32)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE).astype(np.float32)

    # 정규화
    image1 = normalize_image(image1)
    image2 = normalize_image(image2)

    # 절대 오차 맵 계산
    abs_error = absolute_error_map(image1, image2)

    # MSE 계산
    mse = calculate_mse(image1, image2)

    # 시각화
    plt.figure(figsize=(10, 5))

    # 원본 이미지 1
    plt.subplot(1, 3, 1)
    plt.imshow(image1, cmap='gray')
    plt.title("Prediction")
    plt.axis('off')

    # 원본 이미지 2
    plt.subplot(1, 3, 2)
    plt.imshow(image2, cmap='gray')
    plt.title("Ground Truth")
    plt.axis('off')

    # 절대 오차 맵
    plt.subplot(1, 3, 3)
    plt.imshow(abs_error, cmap='bwr', vmin=-1, vmax=1)
    plt.title("Error Map")
    plt.colorbar()
    plt.axis('off')

    # MSE 값 그래프 위에 추가
    plt.suptitle(f"Mean Squared Error (MSE): {mse:.4f}", fontsize=16)

    # 레이아웃 정리 및 출력
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # 제목을 위한 여백 확보
    plt.show()

# 경로 입력 및 실행
image1_path = 'D:/temp/p1.png'  # 첫 번째 이미지 경로
image2_path = 'D:/temp/gt.jpg'  # 두 번째 이미지 경로

generate_absolute_error_map(image1_path, image2_path)
