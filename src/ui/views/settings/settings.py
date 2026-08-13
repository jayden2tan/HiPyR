import flet as ft
from ui.views.settings.general import general_settings
from ui.views.settings.library import library_settings


def settings_view(page: ft.Page):

    async def go_back():
        await page.push_route("/")

    sidebar = ft.Container(
        width=250,
        height=490, # stop container from reaching top and bottom of window, looks nicer
        padding=10,
        content=ft.Column(
            [
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.SETTINGS_OUTLINED),
                    title=ft.Text("General"),
                    on_click=lambda _:change_tab(general_settings),
                ),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.LIBRARY_BOOKS),
                    title=ft.Text("Library"),
                    on_click=lambda _: change_tab(library_settings()),
                )
            ],
        ),
    )

    content_area = ft.Container(
        content=general_settings(page),
        expand=True,
        padding=20
    )

    def change_tab(content):
        content_area.content = content(page)
        content_area.update()

    return ft.View(
        route="/settings",
        controls=[
            ft.AppBar(
                title=ft.Text("Settings"),
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    tooltip="Back",
                    mouse_cursor=ft.MouseCursor.CLICK,
                    hover_color=ft.Colors.TRANSPARENT,
                    highlight_color=ft.Colors.TRANSPARENT,
                    on_click=go_back
                ),
            ),
            ft.Row(
                [
                    sidebar,
                    content_area
                ],
                expand=True
            )
        ]
    )