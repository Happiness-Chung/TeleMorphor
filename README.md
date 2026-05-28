## 🕹️ Motion&Location Editing of a Character of the Videos In-The-Wild

<p align="center">
  <img src="assets/teaser.gif" width="90%">
</p>

---

## Bottom-Up Problem Analysis: What Makes the Editing Difficult?

👓 Large motion gaps: differences between source and target motions <br>
👓 Location shifts: change of the protagonist’s spatial position <br>
👓 Complex backgrounds: dynamic and complicated backgrounds <br>
👓 Camera movement: change of camera position <br>
👓 Character-background similarity: similar appearance between the character and the background  <br>
👓 Temporal inconsistency: large gap between frames <br>

## Our Solution: MysticMorphor
<p align="center">
  <img src="assets/framework.png" width="95%">
</p>

**Source Video:** <br>
YouTube & AI video generator ()

**Key Functions:** <br>
🪢 Foreground-background disentangled editing <br>
🤾‍♀️ Guided by motion priors <br>
💄 Training-free protagonist guidance

---

## Quantitative Performance

<p align="center">
  <img src="assets/results.png" width="95%">
</p>

---
## Acknowledgement
Our project is heavily based on [MotionEditor](https://github.com/Francis-Rings/MotionEditor)

```bibtex
@inproceedings{tu2024motioneditor,
  title={Motioneditor: Editing video motion via content-aware diffusion},
  author={Tu, Shuyuan and Dai, Qi and Cheng, Zhi-Qi and Hu, Han and Han, Xintong and Wu, Zuxuan and Jiang, Yu-Gang},
  booktitle={CVPR},
  year={2024}
}
```
---

## Installation

```bash
git clone https://github.com/yourname/MysticMorphor.git
cd MysticMorphor

conda create -n mystic python=3.10
conda activate mystic

pip install -r requirements.txt
