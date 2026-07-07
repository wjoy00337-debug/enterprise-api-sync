# 🌐 Enterprise API Sync Tool

> 基于 Python 开发的企业 API 数据同步工具。

一个模拟企业后台 API 数据同步场景的自动化工具，支持 HTTP API 请求、JSON 数据解析、Excel 数据导出、运行日志记录以及 GUI 图形界面操作，适用于企业接口开发、数据同步及自动化办公场景。

---

# ✨ Project Features

✅ HTTP API 数据获取

✅ JSON 自动解析

✅ Excel 数据导出

✅ GUI 图形界面

✅ 接口请求日志

✅ 输出目录自由选择

✅ 超时参数配置

✅ 模块化设计

✅ 企业级项目结构

---

# 📷 Software Preview

## 图形界面

![](docs/gui.png)

---

## 同步完成

![](docs/result.png)

---

## 导出的 Excel

![](docs/api_users.png)

---

# 📁 Workflow

```
HTTP API
     │
     ▼
Request Data
     │
     ▼
JSON Parsing
     │
     ▼
Data Processing
     │
     ▼
Export Excel
     │
     ▼
Generate Log
```

---

# 📂 Project Structure

```
enterprise-api-sync/

├── config/
│
├── docs/
│   ├── gui.png
│   ├── result.png
│   └── api_users.png
│
├── logs/
│
├── output/
│
├── src/
│   ├── api_client.py
│   ├── processor.py
│   ├── exporter.py
│   ├── logger.py
│   └── __init__.py
│
├── gui.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔧 Technology Stack

| 技术 | 说明 |
|------|------|
| Python | 开发语言 |
| Requests | HTTP 请求 |
| JSON | 数据解析 |
| Pandas | 数据处理 |
| OpenPyXL | Excel 导出 |
| Tkinter | GUI 图形界面 |
| Logging | 日志记录 |

---

# 🚀 Quick Start

## 1. 安装依赖

```bash
pip install -r requirements.txt
```

---

## 2. 启动 GUI

```bash
python gui.py
```

---

## 3. 命令行运行

```bash
python main.py
```

---

# 🌍 Default API

项目默认接口：

```text
https://jsonplaceholder.typicode.com/users
```

返回 JSON 用户数据，并自动导出 Excel。

---

# 💼 Business Scenario

本项目模拟企业系统之间的数据同步流程。

适用于：

- ERP 数据同步
- CRM 用户同步
- OA 系统接口
- 第三方开放平台
- 企业数据接口
- 自动化数据采集
- API 数据导出

典型流程：

```
HTTP API
      │
      ▼
获取数据
      │
      ▼
JSON解析
      │
      ▼
数据整理
      │
      ▼
导出Excel
      │
      ▼
生成运行日志
```

---

# ⭐ Project Highlights

- 模块化项目架构
- GUI 桌面工具
- REST API 调用
- JSON 数据解析
- Requests 网络请求
- Excel 自动导出
- 自动生成日志
- 企业级目录结构
- Python 自动化开发

---

# 📈 Project Result

✔ 成功请求 REST API

✔ 自动解析 JSON 数据

✔ 自动导出 Excel

✔ GUI 图形界面操作

✔ 输出运行日志

✔ 模块化代码设计

✔ 企业接口数据同步

✔ 企业自动化办公场景

---

# 👨‍💻 Author

Joy Wang

GitHub：

https://github.com/wjoy00337-debug
