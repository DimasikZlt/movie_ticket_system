import yaml


def load_yaml(file_name: str):
    with open(file_name, 'r') as file:
        try:
            movie_hall_schema = yaml.safe_load(file)
        except yaml.YAMLError:
            print('YAML format error')
            exit(1)
        except FileNotFoundError:
            print('File not found')
            exit(1)
    return movie_hall_schema
