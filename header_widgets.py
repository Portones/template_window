import flet as ft

from consts import app_name

def header_widget():
    exit_widget = ft.IconButton(icon=ft.icons.EXIT_TO_APP, icon_color="red", icon_size=50)
    app_name_widget = ft.Text(value=app_name, size=50, weight=ft.FontWeight.BOLD)
    settings_widget = ft.IconButton(icon=ft.icons.SETTINGS, icon_color="grey", icon_size=50)
    widget = ft.Row(
        controls=[exit_widget, app_name_widget, settings_widget],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    return widget