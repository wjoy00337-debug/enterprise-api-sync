import configparser
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, scrolledtext

from src.logger import setup_logger
from src.api_client import fetch_api
from src.processor import process_json
from src.exporter import export_to_excel


def load_config():
    config = configparser.ConfigParser()
    config.read(Path("config") / "config.ini", encoding="utf-8")
    return config


class ApiSyncApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enterprise API Sync Tool v1.0")
        self.root.geometry("760x520")

        config = load_config()

        self.api_url = tk.StringVar(value=config["API"]["url"])
        self.timeout = tk.StringVar(value=config["API"]["timeout"])
        self.output_folder = tk.StringVar(value=str(Path(config["API"]["output"]).resolve()))
        self.output_file = tk.StringVar(value="api_users.xlsx")

        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self.root,
            text="Enterprise API Sync Tool",
            font=("Microsoft YaHei UI", 18, "bold")
        )
        title.pack(pady=15)

        subtitle = tk.Label(
            self.root,
            text="企业 API 数据同步工具：接口请求、JSON解析、Excel导出、日志记录",
            font=("Microsoft YaHei UI", 10)
        )
        subtitle.pack(pady=5)

        form = tk.Frame(self.root)
        form.pack(fill="x", padx=30, pady=10)

        tk.Label(form, text="API地址：", width=12, anchor="w").grid(row=0, column=0, pady=8)
        tk.Entry(form, textvariable=self.api_url, width=75).grid(row=0, column=1, padx=5, columnspan=2)

        tk.Label(form, text="超时时间：", width=12, anchor="w").grid(row=1, column=0, pady=8)
        tk.Entry(form, textvariable=self.timeout, width=75).grid(row=1, column=1, padx=5, columnspan=2)

        tk.Label(form, text="输出目录：", width=12, anchor="w").grid(row=2, column=0, pady=8)
        tk.Entry(form, textvariable=self.output_folder, width=65).grid(row=2, column=1, padx=5)
        tk.Button(form, text="浏览", command=self.choose_output).grid(row=2, column=2)

        tk.Label(form, text="输出文件名：", width=12, anchor="w").grid(row=3, column=0, pady=8)
        tk.Entry(form, textvariable=self.output_file, width=75).grid(row=3, column=1, padx=5, columnspan=2)

        self.start_button = tk.Button(
            self.root,
            text="开始同步",
            font=("Microsoft YaHei UI", 12, "bold"),
            width=18,
            height=2,
            command=self.start_sync
        )
        self.start_button.pack(pady=10)

        tk.Label(self.root, text="运行日志：", anchor="w").pack(fill="x", padx=30)

        self.log_box = scrolledtext.ScrolledText(self.root, height=14)
        self.log_box.pack(fill="both", expand=True, padx=30, pady=10)

    def choose_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder.set(folder)

    def write_log(self, message):
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)
        self.root.update_idletasks()

    def start_sync(self):
        self.start_button.config(state="disabled")
        self.log_box.delete("1.0", tk.END)

        thread = threading.Thread(target=self.run_sync)
        thread.daemon = True
        thread.start()

    def run_sync(self):
        try:
            url = self.api_url.get().strip()
            timeout = int(self.timeout.get().strip())
            output_folder = self.output_folder.get().strip()
            output_file = self.output_file.get().strip()

            if not output_file.endswith(".xlsx"):
                output_file += ".xlsx"

            self.write_log("程序启动...")
            self.write_log(f"API地址：{url}")
            self.write_log(f"输出目录：{output_folder}")

            logger = setup_logger()

            data = fetch_api(url, timeout, logger)
            self.write_log("API请求成功")

            df = process_json(data, logger)
            self.write_log(f"JSON解析完成，共 {len(df)} 条数据")

            output_path = export_to_excel(
                df=df,
                output_folder=output_folder,
                filename=output_file,
                logger=logger
            )

            self.write_log(f"Excel导出成功：{output_path}")
            self.write_log("同步完成！")

            messagebox.showinfo(
                "同步完成",
                f"同步完成！\n\n输出文件：\n{output_path}"
            )

        except Exception as e:
            self.write_log(f"同步失败：{e}")
            messagebox.showerror("同步失败", str(e))

        finally:
            self.start_button.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = ApiSyncApp(root)
    root.mainloop()