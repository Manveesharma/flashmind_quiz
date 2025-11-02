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
- Python 3.8 or higher
- Internet connection (for fetching questions)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Manveesharma/flashmind.git
   cd flashmind
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   > 💡 Note: If you don't want voice features, you can skip installing `pyttsx3`.

### Running the Quiz
```bash
python Quiz.py
```

---

## 🎮 How to Play
1. **Start the Quiz**: Run the script and follow the on-screen instructions.
2. **Answer Questions**: Type the letter corresponding to your answer (A, B, C, or D).
3. **Earn Points**:
   - Base points for correct answers
   - ⚡ Speed bonus for quick responses
   - 🔥 Combo bonus for consecutive correct answers
4. **Track Progress**: View your score, accuracy, and difficulty level after each question.
5. **Review Mistakes**: Wrong answers are saved for later review.

---

## ⚙️ Configuration
You can customize your quiz experience by modifying the following in `Quiz.py`:

```python
# Quiz settings
TOTAL_QUESTIONS = 10  # Number of questions per quiz
ENABLE_VOICE = True   # Set to False to disable voice feedback
DIFFICULTY = 'medium' # Starting difficulty (easy, medium, hard, or random)
CATEGORY = 'general'  # Quiz category (see categories in the code)
```

---

## 📊 Performance Metrics
The app tracks various metrics that you can find in `flashmind_mem.json`:
- Best score
- Average response time
- Accuracy percentage
- Total questions answered
- Wrong answers with correct solutions

---

## 🤝 Contributing
Contributions are welcome! Here's how you can help:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct.

---

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments
- [OpenTDB](https://opentdb.com/) for the free trivia API
- All contributors who have helped improve this project

---

## 🧠 Demo (Console)
```
🎯 FlashMind AI — Adaptive Quiz (v3.0)
------------------------------------
🏆 Best Score: 0  |  🔥 Streak: 0

Question 1/10 [Medium]
What is the capital of France?
A) London
B) Paris
C) Berlin
D) Madrid

Your answer (A/B/C/D): B
✅ Correct! +10 points (1.2s)
```

---

## 📧 Contact
For questions or feedback, please open an issue or contact [Your Email].

<div align="center">
  Made with ❤️ by [Your Name]
</div>
