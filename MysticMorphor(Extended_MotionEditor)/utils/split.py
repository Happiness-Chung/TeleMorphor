import os
import cv2

for i in range(7,25):

    # if i == 3 or i == 4 or i == 12 or i == 13 or i == 14:
    #     continue

    # mp4 파일들이 있는 폴더
    input_folder = f"resolution/case-{i}/MysticMorph"
    output_base_folder = f"resolution/case-{i}/MysticMorph/background"

    os.makedirs(output_base_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(f"b{i}.webm"):
            video_path = os.path.join(input_folder, filename)
            video_name = os.path.splitext(filename)[0]
            output_folder = os.path.join(output_base_folder, video_name)
            os.makedirs(output_folder, exist_ok=True)

            cap = cv2.VideoCapture(video_path)
            frame_idx = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame_filename = os.path.join(output_folder, f"{frame_idx:04d}.png")
                cv2.imwrite(frame_filename, frame)
                frame_idx += 1

            cap.release()
            print(f"✅ Saved {frame_idx} frames from '{filename}' to '{output_folder}'")