from pathlib import Path
import shutil

def organise_file_recursively(base_path):
    archive_path = base_path / "Archives"
    archive_path.mkdir(parents=True, exist_ok=True)

    for item in base_path.rglob("*"):
        # Skip directories, process only files
        if item.is_dir():
            continue

        # Determine file extension
        file_extension = item.suffix.lstrip(".").lower()
        if not file_extension:
            continue

        if file_extension in ('zip', 'tar', 'gztar'):
            extract_dir = archive_path / item.stem
            extract_dir.mkdir(parent=True, exist_ok=True)

            