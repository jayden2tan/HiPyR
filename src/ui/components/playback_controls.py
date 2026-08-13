import flet as ft
from core.playback import AudioController


def playback_ui(controller: AudioController):
    playback_state = {"is_playing": False}

    button = ft.IconButton(
        icon=ft.Icons.PLAY_ARROW,
        scale=1.2,
        mouse_cursor=ft.MouseCursor.CLICK,
        hover_color=ft.Colors.TRANSPARENT,
        highlight_color=ft.Colors.TRANSPARENT,
        tooltip="Play"
    )

    async def button_clicked(e):
        if playback_state["is_playing"]:
            await controller.pause()
            button.icon = ft.Icons.PLAY_ARROW
            button.tooltip = "Play"
            playback_state["is_playing"] = False
        else:
            await controller.resume()
            button.icon = ft.Icons.PAUSE
            button.tooltip = "Pause"
            playback_state["is_playing"] = True

        button.update()


    button.on_click = button_clicked

    return ft.Row(
            [button],
            alignment=ft.MainAxisAlignment.CENTER
    )

