import logging
from pathlib import Path


def setup_logger(log_dir="logs"):
    """
    创建日志对象
    """

    Path(log_dir).mkdir(exist_ok=True)

    logger = logging.getLogger("EnterpriseAPI")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler(
        Path(log_dir) / "run.log",
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger