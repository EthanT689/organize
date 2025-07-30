# File Organizer (Basic Version)

This Python script helps you automatically organize files in a specified folder (like your Downloads folder) by their type. It sorts files into folders like `Images`, `Documents`, `Videos`, `Music`, `Archives`, and `Others`.

## 📁 How It Works

- Scans the specified folder (`source_folder`)
- Identifies each file's extension
- Moves files into folders based on file types:
  - `.jpg`, `.pdf`, `.mp4`, etc.
- Files that don’t match any category go into an `Others` folder

## 🛠️ Requirements

- Python 3.x
- No external libraries required (uses built-in `os` and `shutil`)

## ✏️ How to Use

1. Open the script in a text editor.
2. Change the `source_folder` path to match the folder you want to organize.
3. Run the script:

```bash
python file_organizer.py
