import flet as ft
import subprocess
from consts import app_list

def execute_program(program_path, output_field):
    def run_program(e):
        output_field.value = ""
        process = subprocess.Popen(
            ["python", program_path], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )

        for line in process.stdout:
            output_field.value += line
            output_field.update()

        for line in process.stderr:
            output_field.value += line
            output_field.update()

    return run_program

def main_widget(version_mss, version_check):
    output_field = ft.TextField(
        label="App Result",
        disabled=True,
        value=version_mss,
        multiline=True,
        expand=True
    )

    all_app_widget = ft.Row(
        wrap=True,
        spacing=20,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[]
    )
    
    for app_name, app_path in app_list.items():
        all_app_widget.controls.append(
            ft.Row(
                wrap=True,
                width=225,
                controls=[
                    ft.Text(app_name, size=40),
                    ft.IconButton(
                        icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,
                        icon_size=30,
                        on_click=execute_program(app_path, output_field),
                        disabled=not version_check
                    )
                ],
            )
        )

    widget = ft.Container(
        content=ft.Column(
            [all_app_widget, output_field],
            expand=True
        ),
        expand=True
    )
    return widget
