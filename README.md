# Clean Folder Generator

Clean Folder Generator is a simple cross-platform desktop application that creates a predefined folder structure for projects with a single click.

It is built using **Python** and **Tkinter** and works on **Windows, macOS, and Linux**.

-----------------------------------------------------------------------------

## ✨ Features

- Graphical user interface (GUI)
- Select base folder using native file dialog
- Custom project name input
- Automatically creates a clean, structured folder hierarchy
- Open the generated folder in Explorer / Finder / File Manager
- Cross-platform (Windows, macOS, Linux)
- Can be packaged as a standalone executable

-----------------------------------------------------------------------------

## 📁 Default Folder Structure
```bash
Clean Folder/
├── 00 Proj
├── 01 Video
│ ├── K 1
│ ├── K 2
│ ├── K 3
│ └── Audio
├── 02 Additional
├── 03 Music
├── 04 SFX
└── 05 Export
```

(The structure can be modified directly in the `STRUCTURE` dictionary inside the source code.)

---

🖥 Requirements (for running from source)

- Python **3.9+** (recommended)
- Tkinter (included with most Python installations)

Check Python version:
```bash
python --version
# or
python3 --version
```
-----------------------------------------------------------------------------

## ▶️ Running the Application (from source)
🪟 Windows (.exe)
```bash 
pyinstaller --onefile --windowed clean_folder.py
```
Output:
```bash
dist/clean_folder.exe
```
Double-click to run.

🍎 macOS (.app)
(Must be built on macOS)
```bash
pyinstaller --onefile --windowed clean_folder.py
```
Output:
```bash
dist/clean_folder.app
```
Double-click to run (Finder).

🐧 Linux (Executable)
```bash
pyinstaller --onefile clean_folder.py
```

Output:
```bash
dist/clean_folder
```

Run with:
```bash
./clean_folder
```
-----------------------------------------------------------------------------
## ⚠️ Important Notes

-Executables must be built on the target OS in mind
-Windows → .exe
-macOS → .app
-Linux → ELF binary
-macOS may ask for permission to access folders (normal behavior).
-The first launch of a packaged app may be slower (PyInstaller extraction).

-----------------------------------------------------------------------------

## 🛠 Customization

You can customize the folder layout by editing the STRUCTURE dictionary:
```python
STRUCTURE = {
    "Docs": {},
    "Media": {
        "Video": {},
        "Audio": {}
    }
}
```
-----------------------------------------------------------------------------
## 📌 Future Improvements (Ideas)

-Multiple structure presets
-Import/export structure via JSON
-Dark/light mode
-Drag & drop base folder
-Auto-create README or .gitignore

-----------------------------------------------------------------------------

📄 License

This project is provided for personal and educational use.
Feel free to modify and extend it for your own workflow. :D
