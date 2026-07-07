import requests


def fetch_api(url, timeout, logger):
    """
    请求API接口，返回JSON数据
    """

    logger.info(f"开始请求API：{url}")

    response = requests.get(url, timeout=timeout)

    logger.info(f"接口返回状态码：{response.status_code}")

    response.raise_for_status()

    data = response.json()

    logger.info("JSON数据解析成功")

    return data