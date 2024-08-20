import flet as ft

from consts import version_statuses

def footer_widget(current_version, version_status):
    version_text = f"Version: {current_version} {version_statuses[version_status]}"
    version_widget = ft.Text(version_text, size=30, weight=ft.FontWeight.BOLD)
    logo_widget = ft.Image(src=f"logoPortPyTech.png", width=90)
    widget = ft.Container(
        content=ft.Row(
            [logo_widget, version_widget],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )
    return widget