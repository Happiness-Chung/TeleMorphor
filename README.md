## 🕹️ Simultaneous Motion-Location Editing of a Character in the Videos In-The-Wild

<p align="center">
  <img src="assets/teaser.gif" width="90%">
</p>

---

## Bottom-Up Problem Analysis: What Makes the Editing Difficult?

👓 Large motion gaps <br>
👓 Location shifts <br>
👓 Complex backgrounds <br>
👓 Camera movement <br>
👓 Human-background ambiguity <br>
👓 Temporal inconsistency <br>

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

## Installation

```bash
git clone https://github.com/yourname/MysticMorphor.git
cd MysticMorphor

conda create -n mystic python=3.10
conda activate mystic

pip install -r requirements.txt
