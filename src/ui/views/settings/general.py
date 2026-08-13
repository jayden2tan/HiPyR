import flet as ft


def general_settings(page: ft.Page):
    return ft.Column(
        [
            ft.Text("Appearance", size=18, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Switch(
                label="Dark Mode",
                padding=15,
                value=True,
                on_change=lambda _: (
                    setattr(page, 'theme_mode', ft.ThemeMode.DARK if _.control.value else ft.ThemeMode.LIGHT),
                    page.update()
                )
            )
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

