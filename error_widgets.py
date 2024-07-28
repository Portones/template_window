import flet as ft

def version_error_widget():
    widget = ft.Container(
        height=100,
        border_radius=20,
        padding=15,
        alignment=ft.alignment.center,
        content=ft.Text(
            "ERROR",
            weight=ft.FontWeight.BOLD,
            size=40
            ),
        bgcolor=ft.colors.RED_300
    )
    return widget