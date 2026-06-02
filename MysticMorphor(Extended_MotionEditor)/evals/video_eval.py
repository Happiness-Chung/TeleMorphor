import os
import torch
import torchvision.transforms as T
from PIL import Image
import lpips
import clip
from tqdm import tqdm

device = "cuda" if torch.cuda.is_available() else "cpu"

# LPIPS 모델 로드
lpips_fn = lpips.LPIPS(net='alex').to(device)

# CLIP 모델 로드
clip_model, clip_preprocess = clip.load("ViT-B/32", device=device)

# 기본 Transform
transform = T.Compose([
    T.Resize((512,512)),
    T.ToTensor()
])

def load_images_from_folder(folder):
    images = []
    filenames = sorted(os.listdir(folder))
    for filename in filenames:
        if filename.lower().endswith(('png', 'jpg', 'jpeg')):
            img_path = os.path.join(folder, filename)
            img = Image.open(img_path).convert('RGB')
            images.append(transform(img).unsqueeze(0))  # (1, 3, H, W)
    return images

def compute_lpips(img1, img2):
    d = lpips_fn(img1.to(device), img2.to(device))
    return d.item()

def compute_clip_score(images, text_prompt="a girl is performing ballet"):
    text = clip.tokenize([text_prompt]).to(device)
    with torch.no_grad():
        image_features = []
        for img in images:
            img_clip = clip_preprocess(T.ToPILImage()(img.squeeze(0))).unsqueeze(0).to(device)
            image_features.append(clip_model.encode_image(img_clip))
        image_features = torch.cat(image_features, dim=0)
        text_features = clip_model.encode_text(text).repeat(image_features.size(0), 1)
        similarity = torch.cosine_similarity(image_features, text_features, dim=1)
    return similarity.mean().item()

def evaluate_video_frames(folder1, folder2, folder3, prompt):
    images = load_images_from_folder(folder1)
    sources = load_images_from_folder(folder2)
    targets = load_images_from_folder(folder3)
    # images = sources

    n = len(images)
    if n == 0:
        return None

    lpips_s_list = []
    lpips_n_list = []
    lpips_t_list = []

    for i in range(n):
        lpips_s = compute_lpips(sources[i], images[i])
        lpips_s_list.append(lpips_s)

        if i > 0:
            lpips_n = compute_lpips(images[i-1], images[i])
            lpips_n_list.append(lpips_n)

        
        lpips_t = compute_lpips(images[i], targets[i])
        lpips_t_list.append(lpips_t)

    lpips_s_mean = sum(lpips_s_list) / len(lpips_s_list)
    lpips_n_mean = sum(lpips_n_list) / len(lpips_n_list) if lpips_n_list else 0
    lpips_t_mean = sum(lpips_t_list) / len(lpips_t_list) if lpips_t_list else 0
    clip_score = compute_clip_score(images, prompt)

    return {
        "LPIPS-S": lpips_s_mean,
        "LPIPS-N": lpips_n_mean,
        "LPIPS-T": lpips_t_mean,
        "CLIP": clip_score
    }

# 사용 예시
base_folder = 'resolution'
prompt = 'A girl is doing a ballet jump with her arms opened and her leg folded" from the top'
i = 24
case_path = os.path.join(base_folder, f'case-{i}', f'MotionEditor/openposefull')
source_path = os.path.join(base_folder, f'case-{i}', 'images')
target_path = os.path.join(base_folder, f'case-{i}', f'target_condition/openposefull')

result = evaluate_video_frames(case_path, source_path, target_path, prompt)
print(result)