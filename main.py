import configparser
from pathlib import Path

from src.logger import setup_logger
from src.api_client import fetch_api
from src.processor import process_json
from src.exporter import export_to_excel


def load_config():
    config = configparser.ConfigParser()
    config.read(Path("config") / "config.ini", encoding="utf-8")
    return config


def main():
    logger = setup_logger()

    logger.info("Enterprise API Sync 启动")

    config = load_config()

    url = config["API"]["url"]
    timeout = int(config["API"]["timeout"])
    output_folder = config["API"]["output"]

    data = fetch_api(url, timeout, logger)

    df = process_json(data, logger)

    output_path = export_to_excel(
        df=df,
        output_folder=output_folder,
        filename="api_users.xlsx",
        logger=logger
    )

    logger.info(f"同步完成：{output_path}")


if __name__ == "__main__":
    main()