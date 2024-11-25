from os import path
from ruamel.yaml import YAML
from loguru import logger

yaml = YAML()


def test_read_config():
    folder_path = path.dirname(path.dirname(__file__))
    logger.debug(folder_path)

    # Open and read the YAML file properly
    with open(
        path.join(folder_path, "assets", "tests", "annual_rate.yaml"), "r"
    ) as file:
        c = yaml.load(file)

    logger.debug(c)
    assert c.get("annual_rate") == 5
