import os

from dotenv import load_dotenv

load_dotenv()

app_name = "PRUEBA"
config_file_name = "config.yaml"
programs_path = "Programs"

db_params = {
    "dbname": "neondb",
    "user": os.getenv("DDBB_USERNAME"),
    "password": os.getenv("DDBB_PASSWORD"),
    "host": "ep-tiny-shadow-a2ozabxt.eu-central-1.aws.neon.tech",
    "port": "5432"
}

app_list = {
    "nombre1": {
        "path": os.path.join(programs_path, "main_nombre1.py")
    },
    "nombre2": {
        "path": os.path.join(programs_path, "main_nombre2.py"),
    },
    "ugg_excel_converter": {
        "path": os.path.join(programs_path, "IN_UEC_20240624", "main.py"),
    }
}
version_statuses = {
    0: "🔴",
    1: "🟠",
    2: "🔵",
    3: "🟢",
}