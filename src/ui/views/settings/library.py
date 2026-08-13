import flet as ft


def library_settings(page: ft.Page):
    return ft.Column(
        [
            ft.Text("Folders", size=12, weight=ft.FontWeight.BOLD),
            ft.Divider(),
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

