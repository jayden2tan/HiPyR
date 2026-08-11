import flet as ft
from core.playback import AudioController


def control_gui(controller: AudioController):
    return ft.Row(
        [
            ft.Button("Play", on_click=controller.play),
            ft.Button("Pause", on_click=controller.pause),
            ft.Button("Resume", on_click=controller.resume)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )