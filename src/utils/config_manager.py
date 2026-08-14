import os
import json
import flet as ft

CONFIG_DIR = os.getenv("FLET_APP_STORAGE_DATA", os.getcwd())
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

DEFAULT_SETTINGS = {
    "general": {"dark_mode": True},
    "library": {"folders": []}
}

def load_settings():
    if not os.path.exists(CONFIG_FILE):
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        show_alert("Failed to load config", "Config file not found. Loading defaults.")
        return DEFAULT_SETTINGS
    except PermissionError:
        show_alert("Failed to load config", "Permission denied. Loading defaults.")
        return DEFAULT_SETTINGS
    except json.JSONDecodeError:
        show_alert("Failed to load config", "Corrupted or invalid config. Loading defaults.")
        return DEFAULT_SETTINGS


def save_settings(settings):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(settings, f, indent=4)


def show_alert(title: str, message: str, page: ft.Page):
    def close_alert():
        alert.open = False
        page.update()


    alert = ft.AlertDialog(
        title=ft.Text(title),
        content=ft.Text(message),
        actions=[ft.TextButton("Dismiss", on_click=close_alert)],
    )

    page.show_dialog(alert)
    alert.open = True
    page.update()