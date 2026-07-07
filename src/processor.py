import pandas as pd


def process_json(data, logger):
    """
    将 API 返回的 JSON 数据转换成表格数据
    """

    if not data:
        logger.warning("API返回数据为空")
        return pd.DataFrame()

    df = pd.json_normalize(data)

    logger.info(f"JSON转换完成，共 {len(df)} 条数据")
    logger.info(f"字段数量：{len(df.columns)}")

    return df