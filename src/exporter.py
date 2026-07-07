from pathlib import Path


def export_to_excel(df, output_folder, filename, logger):
    """
    将DataFrame导出为Excel文件
    """

    Path(output_folder).mkdir(exist_ok=True)

    output_path = Path(output_folder) / filename

    df.to_excel(output_path, index=False)

    logger.info(f"Excel导出成功：{output_path}")

    return output_path