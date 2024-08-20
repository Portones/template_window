import os

from dotenv import load_dotenv

load_dotenv()

config_file_name = "config.yaml"
db_params = {
    "dbname": "neondb",
    "user": os.getenv("DDBB_USERNAME"),
    "password": os.getenv("DDBB_PASSWORD"),
    "host": "ep-tiny-shadow-a2ozabxt.eu-central-1.aws.neon.tech",
    "port": "5432"
}
app_name = "PRUEBA"
app_list = {
    "nombre1": "main_nombre1.py",
    "nombre2": "main_nombre2.py",
    "nombre3": "fichero"
}
version_statuses = {
    0: "🔴",
    1: "🟠",
    2: "🔵",
    3: "🟢",
}