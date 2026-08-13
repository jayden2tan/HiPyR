import flet as ft
from core.playback import AudioController
from ui.components.playback_control import control_gui


def main(page: ft.Page):
    controller = AudioController(page)
    controller_ui = control_gui(controller)

    page.title = "HiPyR"
    page.add(
        controller_ui
    )


if __name__ == "__main__":
    ft.run(main)
