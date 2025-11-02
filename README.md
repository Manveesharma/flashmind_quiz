<!-- ================================================== -->
<!-- 🎯 FlashMind AI — Smart Adaptive Quiz CLI App -->
<!-- ================================================== -->

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/CLI-App-yellow?logo=gnubash&logoColor=white" alt="CLI App"/>
  <img src="https://img.shields.io/badge/Open%20Trivia%20API-Live-brightgreen?logo=databricks&logoColor=white" alt="Trivia API"/>
  <img src="https://img.shields.io/badge/AI-Voice%20Enabled-orange?logo=openai&logoColor=white" alt="Voice Enabled"/>
  <img src="https://img.shields.io/github/license/Manveesharma/flashmind?color=purple" alt="License"/>
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg" alt="PRs Welcome"/>
</p>

<h1 align="center">🌟 FlashMind AI v3 — Adaptive Smart Quiz CLI ⚡</h1>

<p align="center">
  <i>Test your mind. Learn smarter. Level up faster. 🧠</i><br>
  <b>Interactive | Voice-Enabled | AI-Adaptive Difficulty | Open Trivia Integration</b>
</p>

---

## 🧩 Overview
**FlashMind AI** is a fast, voice-assisted, adaptive **command-line quiz app** built in Python.  
It fetches real-time questions from the [Open Trivia Database](https://opentdb.com), tracks your best score, and automatically adjusts difficulty based on your performance — just like an AI coach!  

> 🎧 Optional voice feedback via `pyttsx3` gives encouragement while you play.  
> 🧠 Includes adaptive bonuses: *Speed Bonus* ⚡, *Combo Bonus* 🔥, and Smart Difficulty Scaling 🤖.

---

## ✨ Features
✅ **Smart Difficulty Scaling** — The quiz adjusts between *easy → medium → hard* based on accuracy & response time.  
✅ **Voice Feedback (TTS)** — Encouragement via `pyttsx3` (“Well done!”, “Keep going!”).  
✅ **Memory Save** — Stores best score and wrong answers in `flashmind_mem.json`.  
✅ **Speed & Combo Bonuses** — Fast responses or streaks earn bonus points.  
✅ **Lightweight** — <50 lines of Python, no external UI needed.  
✅ **Multiple Categories** — Choose from various quiz categories or go random.  
✅ **Performance Tracking** — Detailed stats and progress tracking.  
✅ **Open Source** — Free to use, modify, and distribute.  

---

## 🚀 Quick Start

### Prerequisites
- Python **3.8+**
- Internet connection (for fetching questions)

### 📦 Required Dependencies

Install the required modules:

```bash
pip install requests pyttsx3
