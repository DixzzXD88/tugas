#!/usr/bin/env python3

import os
import re
from pathlib import Path

README_PATH = "README.md"
ROOT = Path(".")
START_TREE = "<!-- START_TREE -->"
END_TREE = "<!-- END_TREE -->"
START_LIST = "<!-- START_LIST -->"
END_LIST = "<!-- END_LIST -->"

IGNORE = {
    ".git", ".github", "node_modules", "__pycache__",
    ".vscode", ".idea", "venv", ".venv", "dist", "build",
    ".DS_Store", "Thumbs.db", ".env", "scripts"
}

ICONS = {
    ".py": "🐍", ".js": "🟨", ".ts": "🔷", ".jsx": "⚛️", ".tsx": "⚛️",
    ".html": "🌐", ".css": "🎨", ".scss": "🎨", ".sass": "🎨",
    ".java": "☕", ".c": "🔵", ".cpp": "🔵", ".cs": "🟣",
    ".go": "🐹", ".rs": "🦀", ".php": "🐘", ".rb": "💎",
    ".sql": "🗄️", ".json": "📦", ".yml": "⚙️", ".yaml": "⚙️",
    ".md": "📝", ".txt": "📄", ".sh": "🐚", ".bat": "🪟",
    ".png": "🖼️", ".jpg": "🖼️", ".jpeg": "🖼️", ".gif": "🖼️",
    ".svg": "🖼️", ".pdf": "📕", ".docx": "📘", ".xlsx": "📗",
    ".pptx": "📙", ".zip": "🗜️",
}


def should_ignore(name):
    return name in IGNORE or name.startswith(".")


def build_tree(path, prefix=""):
    lines = []
    try:
        items = sorted(
            [p for p in path.iterdir() if not should_ignore(p.name)],
            key=lambda p: (p.is_file(), p.name.lower())
        )
    except PermissionError:
        return lines

    for i, item in enumerate(items):
        last = (i == len(items) - 1)
        connector = "┗━━ " if last else "┣━━ "
        icon = "📁" if item.is_dir() else ICONS.get(item.suffix.lower(), "📄")
        lines.append(f"{prefix}{connector}{icon} {item.name}")

        if item.is_dir():
            ext = "    " if last else "┃   "
            lines.extend(build_tree(item, prefix + ext))

    return lines


def build_file_table(path, base=None):
    if base is None:
        base = path
    rows = []
    try:
        items = sorted(
            [p for p in path.iterdir() if not should_ignore(p.name)],
            key=lambda p: (p.is_file(), p.name.lower())
        )
    except PermissionError:
        return rows

    for item in items:
        rel = item.relative_to(base).as_posix()
        if item.is_dir():
            rows.extend(build_file_table(item, base))
        else:
            icon = ICONS.get(item.suffix.lower(), "📄")
            size = item.stat().st_size
            size_str = f"{size / 1024:.1f} KB" if size >= 1024 else f"{size} B"
            rows.append(f"| {icon} | [{item.name}]({rel}) | `{rel}` | {size_str} |")

    return rows


def count_stats(path=None):
    if path is None:
        path = ROOT
    files, folders, total_size = 0, 0, 0
    try:
        for item in path.rglob("*"):
            parts = item.relative_to(ROOT).parts
            if any(p in IGNORE or p.startswith(".") for p in parts):
                continue
            if item.is_file():
                files += 1
                total_size += item.stat().st_size
            elif item.is_dir():
                folders += 1
    except PermissionError:
        pass
    return {"files": files, "folders": folders, "size": total_size}


def generate():
    tree_lines = build_tree(ROOT)
    tree = "```bash\n📦 tugas/\n" + "\n".join(tree_lines) + "\n```"

    table_rows = build_file_table(ROOT)
    stats = count_stats()

    if table_rows:
        table = (
            f"**📊 Total: {stats['files']} file · {stats['folders']} folder · "
            f"{stats['size'] / 1024:.1f} KB**\n\n"
            "| 🎯 | Nama File | Path | Ukuran |\n"
            "|----|-----------|------|--------|\n"
            + "\n".join(table_rows)
        )
    else:
        table = "_Belum ada file._"

    readme = Path(README_PATH)
    if not readme.exists():
        print(f"❌ {README_PATH} tidak ditemukan!")
        return

    content = readme.read_text(encoding="utf-8")

    content = re.sub(
        f"{re.escape(START_TREE)}.*?{re.escape(END_TREE)}",
        f"{START_TREE}\n\n## 📂 Struktur Folder\n\n{tree}\n\n{END_TREE}",
        content, flags=re.DOTALL
    )

    content = re.sub(
        f"{re.escape(START_LIST)}.*?{re.escape(END_LIST)}",
        f"{START_LIST}\n\n## 📋 Daftar File & Folder\n\n{table}\n\n{END_LIST}",
        content, flags=re.DOTALL
    )

    readme.write_text(content, encoding="utf-8")
    print(f"✅ README.md berhasil di-update! ({stats['files']} file, {stats['folders']} folder)")


if __name__ == "__main__":
    generate()
