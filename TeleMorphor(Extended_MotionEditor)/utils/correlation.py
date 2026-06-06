import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 함수: 이미지 정규화
def normalize_image(image):
    return (image - np.min(image)) / (np.max(image) - np.min(image) + 1e-8)

# 함수: 상관 관계 분석 및 시각화
def pixel_correlation(image1_path, image2_path):
    # 이미지 불러오기 (Grayscale로 읽기)
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE).astype(np.float32)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE).astype(np.float32)

    # 정규화
    image1 = normalize_image(image1)
    image2 = normalize_image(image2)

    # 픽셀 값을 1차원 벡터로 변환
    pixels1 = image1.flatten()
    pixels2 = image2.flatten()

    # 회귀선 계산
    slope, intercept, r_value, p_value, std_err = linregress(pixels1, pixels2)

    # 산점도 시각화
    plt.figure(figsize=(8, 6))
    plt.scatter(pixels1, pixels2, alpha=0.5, s=10, color="gray", label="Pixel Values")

    # 회귀선 추가
    x_vals = np.linspace(0, 1, 100)
    y_vals = slope * x_vals + intercept
    plt.plot(x_vals, y_vals, color="red", label=f"Regression Line (R² = {r_value**2:.2f})")

    # 그래프 설정
    plt.title("Pixel Value Correlation with Regression Line")
    plt.xlabel("Prediction")
    plt.ylabel("Ground Truth")
    plt.legend()
    plt.grid()
    plt.show()


# 경로 입력 및 실행
image1_path = 'D:/temp/aa.png'  # 첫 번째 이미지 경로
image2_path = 'D:/temp/enlarged_2.png'  # 두 번째 이미지 경로

pixel_correlation(image1_path, image2_path)
