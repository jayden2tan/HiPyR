import flet as ft
from core.playback import AudioController
from ui.components.playback_controls import playback_ui
from ui.views.settings.settings import settings_view


def main(page: ft.Page):

    async def open_settings(e):
        await page.push_route("/settings")

    controller_ui = playback_ui(AudioController(page))

    def change_route():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.SafeArea(
                        content=ft.Column(
                            controls=[
                                ft.AppBar(
                                    actions=[ft.IconButton(
                                        ft.Icons.SETTINGS,
                                        mouse_cursor=ft.MouseCursor.CLICK,
                                        hover_color=ft.Colors.TRANSPARENT,
                                        highlight_color=ft.Colors.TRANSPARENT,
                                        on_click=open_settings
                                        )
                                    ]
                                ),
                            ]
                        )
                    ),
                    ft.BottomAppBar(
                        height=100,
                        content=ft.Container(
                            content=controller_ui,
                            alignment=ft.Alignment.CENTER
                        )
                    )
                ],
            )
        )

        if page.route == "/settings":
            page.views.append(settings_view(page))

        page.update()

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    page.on_route_change = change_route
    page.on_view_pop = view_pop

    change_route()

    page.title = "HiPyR"
    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(
            android=ft.PageTransitionTheme.NONE,
            ios=ft.PageTransitionTheme.NONE,
            linux=ft.PageTransitionTheme.NONE,
            macos=ft.PageTransitionTheme.NONE,
            windows=ft.PageTransitionTheme.NONE,
        )
    )


if __name__ == "__main__":
    ft.run(main)
