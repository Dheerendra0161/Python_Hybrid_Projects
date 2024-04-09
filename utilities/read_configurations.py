import configparser


def read_config(section, key):
    config = configparser.ConfigParser()
    config_file_path = "../configurations/config.ini"  # .. refers to the parent directory of the current directory.
    config.read(config_file_path)
    value = None
    if config.has_section(section):
        if config.has_option(section, key):
            value = config.get(section, key)
    return value

# def read_config(section, key):
#     config = configparser.ConfigParser()
#     config.read('configurations.ini')
#     value = None
#     if config.has_section(section):
#         if config.has_option(section, key):
#             value = config.get(section, key)
#     return value
