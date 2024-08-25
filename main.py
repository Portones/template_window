import flet as ft
from config_operations import check_version, obtain_version
from header_widgets import header_widget
from main_widgets import main_widget
from footer_widgets import footer_widget

def main(page: ft.Page):
    try:
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        page.window.min_width = 450
        _, version_mss, version_status = check_version()

        page.add(header_widget(page))
        page.add(main_widget(version_mss))
        page.add(footer_widget(obtain_version(), version_status))
    except Exception as e:
        page.add(ft.Text(f"Error during initialization: {str(e)}", color="red", size= 30))

ft.app(target=main, assets_dir="assets")
