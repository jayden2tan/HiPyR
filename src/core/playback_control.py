import flet as ft
from core.playback import AudioController


def control_gui(controller: AudioController):
    playback_state = {"is_playing": False}

    button = ft.IconButton(icon=ft.Icons.PLAY_ARROW)

    async def button_clicked(e):
        if playback_state["is_playing"]:
            await controller.pause()
            button.icon = ft.Icons.PLAY_ARROW
            playback_state["is_playing"] = False
        else:
            await controller.resume()
            button.icon = ft.Icons.PAUSE
            playback_state["is_playing"] = True

        button.update()


    button.on_click = button_clicked

    return ft.Row(
        [button],
        alignment=ft.MainAxisAlignment.CENTER
    )