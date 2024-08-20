import flet as ft
from config_operations import check_version, obtain_version
from header_widgets import header_widget
from main_widgets import main_widget
from footer_widgets import footer_widget

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.min_width = 450
    version_check, version_mss, version_status = check_version()
    page.add(header_widget())
    page.add(main_widget(version_mss, version_check))
    page.add(footer_widget(obtain_version(), version_status))

ft.app(target=main, assets_dir="assets")
