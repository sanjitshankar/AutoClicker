# AutoClicker

A simple Python auto clicker script that clicks your mouse at a fixed interval.  
Useful for repetitive clicking tasks, simple testing, or just for fun.

## 🚀 Features
- ⏱ Adjustable click interval (default: 0.5 seconds)
- ⌛ 3-second start delay so you can position your mouse
- 🛑 Stop anytime with CTRL + C
- 💻 Lightweight and beginner-friendly code

## 📦 Installation
1. Clone the repository
   git clone https://github.com/sanjitshankar/AutoClicker.git
   cd AutoClicker

2. Install dependencies
   pip install pyautogui

3. (Windows only)  
   Make sure Python and pip are added to your PATH.  
   If pyautogui doesn’t work, run:
   pip install --upgrade pip

## 🖱 Usage
Run:
   python autoclicker.py

1. After running, you’ll have 3 seconds to position your mouse.  
2. The script will start clicking at the set interval.  
3. Stop anytime by pressing CTRL + C in the terminal.

## ⚙️ Customization
Edit the interval value inside autoclicker.py to change the click speed:
   interval = 0.2  # Faster clicks  
   interval = 1.0  # Slower clicks

## 📜 License
This project is licensed under the MIT License.  
Feel free to use, modify, and share.

**Author:** [Sanjit Shankar](https://github.com/sanjitshankar)
