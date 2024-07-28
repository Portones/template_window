import flet as ft
from config_operations import check_version, obtain_version
from error_widgets import version_error_widget
from header_widgets import header_widget
from main_widgets import main_widget
from footer_widgets import footer_widget

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.min_width = 450
    version_check, version_mss = check_version()
    if version_check:
        page.add(header_widget())
        main_widget_princ = main_widget(version_mss)
        page.add(main_widget_princ)
        page.add(footer_widget(obtain_version()))
    else:
        page.add(version_error_widget())

ft.app(target=main, assets_dir="assets")
