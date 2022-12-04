"""entry of the bot"""
import yaml
from bot import soul


def main():
    """entry"""
    with open("docs/config.yml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    if config.get("token") is None or config.get("token") == "TOKEN":
        raise ValueError("bot token is not set")
    soul.run(config)

if __name__ == "__main__":
    main()
