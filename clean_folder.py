import os
import sys
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path

STRUCTURE = {
    "00 Proj": {},
    "01 Video": {
        "K 1": {},
        "K 2": {},
        "K 3": {},
        "Audio": {}
    },
    "02 Additional": {},
    "03 Music": {},
    "04 SFX": {},
    "05 Export": {}
}

def create_folder_structure(base_dir: Path, tree: dict) -> None:

    for name, subtree in tree.items():
        folder_path = base_dir / name
        folder_path.mkdir(parents=True, exist_ok=True)

        if isinstance(subtree, dict) and subtree:
            create_folder_structure(folder_path, subtree)\

def main():
    base = Path.cwd() / "Clean Folder"

    base.mkdir(parents=True, exist_ok=True)
    create_folder_structure(base, STRUCTURE)

    print(f"Struktura foldera kreirana u: {base}")


def open_in_file_manager(path: Path) -> None:
    try:
        if sys.platform.startswith("win"):
            os.startfile(str(path))  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.run(["open", str(path)], check=False)
        else:
            subprocess.run(["xdg-open", str(path)], check=False)
    except Exception:
        # Ne rušimo app ako korisnik nema xdg-open ili slično
        pass

class CleanFolderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clean folder Generator")
        self.geometry("640x240")
        self.minsize(640, 420)

        self.base_dir = tk.StringVar(value=str(Path.home()))
        self.project_name = tk.StringVar(value="Clean Folder")

        self._build_ui()

    def _build_ui(self):
        pad = {"padx": 12, "pady": 8}

        # Header 
        header = ttk.Label(self, text="Create project folder structure", font=("Segoe UI", 14, "bold"))
        header.pack(anchor="w", **pad)

        # Base folder row
        frm_base = ttk.Frame(self)
        frm_base.pack(fill="x", **pad)

        ttk.Label(frm_base, text="Base folder:").pack(side="left")
        ent_base = ttk.Entry(frm_base, textvariable=self.base_dir)
        ent_base.pack(side="left", fill="x", expand=True, padx=8)

        ttk.Button(frm_base, text="Browse...", command=self.on_browse).pack(side="left")

        # Project name row
        frm_name = ttk.Frame(self)
        frm_name.pack(fill="x", **pad)

        ttk.Label (frm_name, text="Project name:").pack(side="left")
        ent_name = ttk.Entry(frm_name, textvariable=self.project_name)
        ent_name.pack(side="left", fill="x", expand=True, padx=8)

        # Buttons row
        frm_buttons = ttk.Frame(self)
        frm_buttons.pack(fill="x", **pad)

        ttk.Button(frm_buttons, text="Create Folder Structure", command=self.on_create).pack(side="left")
        ttk.Button(frm_buttons, text="Open Folder", command=self.on_open_folder).pack(side="left", padx=(8, 0))
        ttk.Button(frm_buttons, text="Clear log", command=self.on_clear).pack(side="left", padx=(8, 0))

        # Preview box 
        frm_prev = ttk.Frame(self)
        frm_prev.pack(fill="both", expand=True, **pad)

        ttk.Label(frm_prev, text="Log Preview:").pack(anchor="w")

        self.txt_preview = tk.Text(frm_prev, wrap="word", height=10)
        self.txt_preview.pack(fill="both", expand=True)
        self.txt_preview.config(state="disabled")

        ttk.Label(frm_prev, text="Log:").pack(anchor="w", pady=(10, 0))
        self.log = tk.Text(frm_prev, height=10, wrap="word")
        self.log.pack(fill="both", expand=True, pady=(6, 0))
        self.log.configure(state="disabled")

        self._render_preview()

    def _render_preview(self):
        lines = []
        def walk(prefix: str, tree: dict):
            for i, (name, subtree) in enumerate(tree.items()):
                is_last = (i == len(tree) - 1)
                branch = "└── " if is_last else "├── "
                lines.append(prefix + branch + name)
                if isinstance(subtree, dict) and subtree:
                    walk(prefix + ("    " if is_last else "│   "), subtree)

        walk("", STRUCTURE)

        self.txt_preview.configure(state="normal")
        self.txt_preview.delete("1.0", "end")
        self.txt_preview.insert("1.0", "\n".join(lines))
        self.txt_preview.configure(state="disabled")
    def _append_log(self, msg: str):
        self.log.configure(state="normal")
        self.log.insert("end", msg + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")
    
    def on_browse(self):
        chosen = filedialog.askdirectory(title="Select base folder")
        if chosen:
            self.base_dir.set(chosen)

    def on_clear(self):
        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")
    
    def on_create(self):
        base = Path(self.base_dir.get()).expanduser()
        name = self.project_name.get().strip()

        if not name:
            messagebox.showerror("Error", "Project name cannot be empty.")
            return

        # Validacija imena projekta
        invalid_chars = set(r'\/:*?"<>|')
        if any((char in invalid_chars) for char in name):
            messagebox.showerror("Error", f"Project name contains invalid characters: {''.join(invalid_chars)}")
            return

        project_path = base / name

        try:
            project_path.mkdir(parents=True, exist_ok=True)
            create_folder_structure(project_path, STRUCTURE)
            self._append_log(f"Folder structure created at: {project_path}")    
            self._append_log("Done.")

            messagebox.showinfo("Success", f"Folder structure created at:\n{project_path}")
        except PermissionError:
            messagebox.showerror("Error", "Permission denied. Cannot create folder structure.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def on_open_folder(self):
        base = Path(self.base_dir.get()).expanduser()
        name = self.project_name.get().strip() or "Clean Folder"
        project_path = base / name
        open_in_file_manager(project_path)

if __name__ == "__main__":
    app = CleanFolderApp()
    app.mainloop()