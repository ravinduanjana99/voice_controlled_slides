# 🎤 Voice-Controlled Slide Navigator

A Python-based tool that lets you control presentation slides **hands-free** with your voice.  
It uses [Vosk](https://alphacephei.com/vosk/) for offline speech recognition and [PyAutoGUI](https://pyautogui.readthedocs.io/) to simulate keyboard controls.

This project allows you to start, navigate, and stop a slideshow (PowerPoint, Google Slides, LibreOffice Impress, etc.) using simple spoken commands.

---

## 🚀 Features
- 🎙️ **Offline speech recognition** (no internet required)  
- 🖱️ **Automated keyboard control**  
- 🔑 **Hotword-based activation** (default: `"computer"`)  
- ⏭️ **Supported commands**:
  - `"computer next"` → Next slide  
  - `"computer back"` → Previous slide  
  - `"computer start"` → Start slideshow (`F5`)  
  - `"computer stop"` → End slideshow (`ESC`)  

---

## 🛠️ Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/voice-slide-navigator.git
   cd voice-slide-navigator
