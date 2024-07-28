import os
import flet as ft

from consts import app_list

def execute_program(program_path):
    os.system(f"python {os.path.join(os.getcwd(), program_path)}")

def main_widget(version_mss):

    result_text_wiget = ft.TextField(
                            label="App Result",
                            disabled=True,
                            value=version_mss,
                            multiline=True
                        )
    all_app_widget = ft.Row(
        controls=[],
        wrap=True
    )
    
    for app in app_list:
        all_app_widget.controls.append(
            ft.Row(
                controls=[
                    ft.Text(app, size=40),
                    ft.IconButton(
                        icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,
                        icon_size=30,
                        on_click=execute_program(app_list[app])
                    )
                ]
            )
        )

    widget = ft.Container(
        content=ft.Column(
            [all_app_widget, result_text_wiget]
        ),
        
        height=300
    )
    return widget