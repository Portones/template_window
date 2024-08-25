import yaml
import os

from ddbb_operations import execute_query
from consts import config_file_name, programs_path

def read_config(subprogram_path: str = ""):
    
    config_file = subprogram_path if subprogram_path else config_file_name
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

def compare_versions(current_version, new_version):
    try:
        c_version, c_subversion, c_subsubversion = current_version.split(".")
        n_version, n_subversion, n_subsubversion = new_version.split(".")

    except ValueError:
        return False, f"El formato de la versión es erróneo"

    if c_version != n_version:
        mss = f"Current Version: {c_version}\nCloud Version: {n_version}\nCan't continue, need to upgrade your app"
        return False, mss, 0
    if c_subversion != n_subversion:
        mss = f"Current Subversion: {c_subversion}\nCloud Subversion: {n_subversion}\nChanges in cloud, consider to upgrade your app"
        return True, mss, 1
    if c_subsubversion != n_subsubversion:
        mss = f"Current Subsubversion: {c_subsubversion}\nCloud Subsubversion: {n_subsubversion}\nMinor changes in cloud"
        return True, mss, 2
    return True, "Correct Version", 3


def check_version(subprogram_name: str = "", subprogram_version: str = ""):
    if not subprogram_version and not subprogram_name:
        config = read_config()

        if config is None:
            return False

        project_name = config["project"]["name"]
        current_version = config["project"]["version"]
    else:
        if subprogram_name == "No" and subprogram_version == "No":
            return compare_versions("1.1.1", "1.1.1")
        project_name = subprogram_name
        current_version = subprogram_version
    obtain_version_query = f"select version from projects where project = '{project_name}'"
    try:
        new_version = execute_query(obtain_version_query)[0][0]
        
    except IndexError:
        return False, f"El proyecto {project_name} no existe", 0
    except ValueError:
        return False, f"El proyecto {project_name} no existe", 0
    except Exception as e:
        return False, f"Excepción: {e}", 0
    return compare_versions(current_version, new_version)


def obtain_version(subprogram_path: str = ""):
    return read_config(subprogram_path)["project"]["version"]


def obtain_name(subprogram_path: str = ""):
    return read_config(subprogram_path)["project"]["name"]


def obtain_subprograms_version_and_name(program_path):
    base_dir = os.path.dirname(program_path)
    if base_dir == programs_path:
        return "No", "No"
    
    config_file = os.path.join(base_dir, "config.yaml")
    return obtain_name(config_file), obtain_version(config_file)

    
   