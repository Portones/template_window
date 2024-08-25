import flet as ft
import subprocess
import os

from consts import app_list, version_statuses
from config_operations import check_version, obtain_subprograms_version_and_name

def execute_program(program_path, output_field):
    def run_program(e):
        output_field.value = "Running..."
        output_field.update()

        try:
            base_dir = os.path.dirname(program_path)
            python_executable = os.path.join(base_dir, 'venv', 'Scripts', 'python.exe') if os.name == 'nt' else os.path.join(base_dir, 'venv', 'bin', 'python')

            if not os.path.isfile(python_executable):
                output_field.value = "Error: no se encontró el intérprete de Python en el venv."
                output_field.update()
                return

            process = subprocess.Popen(
                [python_executable, program_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            stdout, stderr = process.communicate()
            output_field.value = stdout + stderr
            output_field.update()

        except Exception as ex:
            output_field.value = f"Error al ejecutar el programa: {str(ex)}"
            output_field.update()

    return run_program

def main_widget(version_mss):
    output_field = ft.TextField(
        label="App Result",
        read_only=True,
        value=version_mss,
        multiline=True,
        expand=True,
        text_size=25
    )

    all_app_widget = ft.Row(
        spacing=20,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[],
        wrap=True,
    )
    
    for app_name, app_details in app_list.items():
        subapp_name, subapp_version = obtain_subprograms_version_and_name(app_details["path"])
        sub_version_check, _, version_status = check_version(subapp_name, subapp_version)
        all_app_widget.controls.append(
            ft.Row(
                wrap=True,
                width=400,
                controls=[
                    ft.Text(version_statuses[version_status], size=30),
                    ft.Text(app_name, size=30),
                    ft.IconButton(
                        icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,
                        icon_size=30,
                        on_click=execute_program(app_details["path"], output_field),
                        disabled=not sub_version_check
                    ),
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
