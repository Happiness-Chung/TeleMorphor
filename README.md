# MysticMorphor
## 🕹️ Simultaneous Motion-Location Editing for In-the-Wild Videos

<p align="left"> <i> Prompt: "The boy flies in the greenary forest" </i> </p>
<table align="left">
<tr>
<td align="left">
<b>Source</b><br>
<img src="Assets/result.gif" width="320"/>
</td>

<td align="left">
<b>Edited</b><br>
<img src="Assets/source.gif" width="320"/>
</td>
</tr>
</table>

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

<br>

---

## Bottom-Up Problem Analysis: What Makes the Editing Difficult?

👓 **Large motion gaps:** differences between source and target motions <br>
👓 **Location shifts:** change of the protagonist’s spatial position <br>
👓 **Complex backgrounds:** dynamic and complicated backgrounds <br>
👓 **Camera movement:** change of camera position <br>
👓 **Character-background similarity:** similar appearance between the character and the background  <br>
👓 **Temporal inconsistency:** large gap between frames <br>

---

## Our Solution: MysticMorphor
<p align="left">
  <img src="Assets/schematic.png" width="70%">
</p>

**Source Video:** <br>
YouTube & AI video generator ([Hailuo AI](https://artlist.io/ai/models/hailuo-ai?utm_source=google&utm_medium=cpc&utm_campaign=23088929427&utm_content=197649277633&utm_term=&keyword=&ad=807679767737&matchtype=a&device=c&gad_source=1&gad_campaignid=23088929427&gbraid=0AAAAACuwFJ2-djoohOGlAI6BAN4kGfyk8&gclid=Cj0KCQjwz9_QBhD_ARIsADnSCfBrQd1NVLxargFICjwoVgLkMGgmk4eUBQLKN3B0cGOlALLxpRkYLXIaAs5dEALw_wcB), [Pexel](https://www.pexels.com/))

**How Simultaneous Motion-Location Editing Is Possible?** <br>
🪢 Foreground-background disentangled editing <br>
🤾‍♀️ Guided by motion priors <br>
💄 Training-free protagonist guidance

---

## Result Analysis

### 🔍 Functional Comparison


| Method | Motion Editing | Location Editing | Training Requirement | Limitation |
|:------:|:------:|:--------:|:-------------------:|:---------------:|
| Follow-Your-Pose | ✅ | ❌ | Training Required | Appearance drift |
| ControlVideo | ⚠️ | ❌ | Training-Free | Weak motion alignment |
| MasaCtrl | ⚠️ | ❌ | Training-Free | Poor motion controllability |
| MotionDirector | ✅ | ❌ | One-Shot | Appearance inconsistency |
| MotionEditor | ✅ | ❌ | One-Shot | Motion conflict & flickering |
| **MysticMorphor** | ✅ | ✅ | One-Shot + Training-Free Guidance | Color shift of protagonist |

### 🔍 Quantitative Comparison

| Method | L-S ↓ | L-N ↓ | L-T ↓ | L-B ↓ | L-P ↓ | CLIP ↑ |
|:---|---:|---:|---:|---:|---:|---:|
| Source Video | ≤0.001 | 0.082 | 0.708 | ≤0.001 | 0.264 | 28.63 |
| Target Motion Prior | 0.709 | 0.053 | ≤0.001 | 0.659 | ≤0.001 | 24.52 |
| Follow-Your-Pose | 0.562 | 0.164 | 0.702 | 0.501 | 0.153 | 28.00 |
| ControlVideo | 0.330 | 0.069 | 0.767 | 0.362 | 0.266 | 29.52 |
| MasaCtrl | 0.513 | 0.096 | 0.566 | 0.428 | 0.123 | 27.94 |
| MotionDirector | 0.604 | 0.075 | 0.695 | 0.581 | 0.285 | 29.40 |
| MotionEditor | 0.348 | 0.148 | 0.666 | 0.252 | 0.094 | 29.35 |
| **MysticMorphor (Ours)** | **0.309** | **0.099** | **0.655** | **≤0.001** | **0.074** | **30.01** |

### 🔍 Qualitative Comparison (User Study)

| Method | M-A ↑ | A-A ↑ | T-A ↑ |
|:---|---:|---:|---:|
| Follow-Your-Pose | 97.1% | 94.6% | 91.5% |
| ControlVideo | 84.2% | 69.4% | 83.3% |
| MasaCtrl | 92.5% | 94.5% | 91.2% |
| MotionDirector | 93.7% | 93.3% | 85.2% |
| MotionEditor | 75.3% | 81.2% | 79.9% |

LPIPS-s, LPIPS-N, LPIPS-T, and CLIP, and newly defined LPIPS-B, LPIPS-P are used for quantitative evaluation (left table). This work also conducted a user study (right table). The questions of the study were as follows: (I) Which video exhibits better alignment with the target motion? (M-A) (II) Which video better preserves the appearance of the source video? (AA) (III) Which video better aligns with the given text prompt? (T-A). A higher percentage represents the superiority of the results from our proposed method.

<br>

**<i>Entire results archive:<i>** [Google Drive](https://drive.google.com/drive/folders/1vraKY_h7Zr3oox_XR7DCvOjB8kSs_6CD?usp=drive_link)

---

## Acknowledgement
Our project is heavily based on [MotionEditor](https://github.com/Francis-Rings/MotionEditor) (CVPR 2024). <br>
We thank the authors for publicly releasing their code.<br>
This project followed the software environment of MotionEditor. <br>

```bibtex
@inproceedings{tu2024motioneditor,
  title={Motioneditor: Editing video motion via content-aware diffusion},
  author={Tu, Shuyuan and Dai, Qi and Cheng, Zhi-Qi and Hu, Han and Han, Xintong and Wu, Zuxuan and Jiang, Yu-Gang},
  booktitle={CVPR},
  year={2024}
}
```
---

## Quick Start

1. Follow [MotionEditor](https://github.com/Francis-Rings/MotionEditor) installation.
2. Prepare inputs in the folder "sample_input".
3. Segment the protagonist from the background using a pre-trained segmentor (can be anything).
4. Inpaint background using a pre-trained segmentor (can be anything).
5. Run MysticMorphor(Extended_MotionEditor)/train/train_bg.py
6. Run MysticMorphor(Extended_MotionEditor)/train/train_adaptor.py
7. Run MysticMorphor(Extended_MotionEditor)/inference.py.

