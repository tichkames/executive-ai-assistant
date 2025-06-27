import yaml
import asyncio
from pathlib import Path

_ROOT = Path(__file__).absolute().parent


async def get_config(config: dict):
    # This loads things either ALL from configurable, or
    # all from the config.yaml
    # This is done intentionally to enforce an "all or nothing" configuration
    if "email" in config["configurable"]:
        return config["configurable"]
    else:
        return await asyncio.to_thread(_load_yaml_from_file)


def _load_yaml_from_file():
    config_path = _ROOT.joinpath("config.yaml")
    with open(config_path, "r") as stream:
        return yaml.safe_load(stream)
