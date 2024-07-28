import yaml

from ddbb_operations import execute_query
from consts import config_file_name

def read_config():
    with open(config_file_name, 'r') as file:
        return yaml.safe_load(file)


def compare_versions(current_version, new_version):
    c_version, c_subversion, c_subsubversion = current_version.split(".")
    n_version, n_subversion, n_subsubversion = new_version.split(".")

    if c_version != n_version:
        mss = f"Current Version: {c_version}\nCloud Version: {n_version}\nCan't continue, need to upgrade your app"
        return False, mss
    if c_subversion != n_subversion:
        mss = f"Current Subversion: {c_subversion}\nCloud Subversion: {n_subversion}\nChanges in cloud, consider to upgrade your app"
        return True, mss
    if c_subsubversion != n_subsubversion:
        mss = f"Current Subsubversion: {c_subsubversion}\nCloud Subsubversion: {n_subsubversion}\nMinor changes in cloud"
        return True, mss
    return True, mss


def check_version():
    config = read_config()
    if config is None:
        return False

    project_name = config["project"]["name"]
    current_version = config["project"]["version"]
    obtain_version_query = f"select version from projects where project = '{project_name}'"
    new_version = execute_query(obtain_version_query)[0][0]

    return compare_versions(current_version, new_version)


def obtain_version():
    return read_config()["project"]["version"]
