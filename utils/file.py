# utils/file.py
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.absolute()


def abs_path_from_project(relative_path: str) -> str:
    """Получить абсолютный путь из относительного пути проекта"""
    if relative_path.startswith('/') or relative_path.startswith('http'):
        return relative_path
    return str(PROJECT_ROOT / relative_path)


# Или более простая версия:
def abs_path_from_project_simple(relative_path: str) -> str:
    """Простая версия без проверок"""
    return os.path.join(PROJECT_ROOT, relative_path)