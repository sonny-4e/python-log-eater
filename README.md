# Python Log Eater 🐍📜

> 🚧 **Status: Work in Progress (Active Development)** 🚧
> This project is currently under construction. New features and Docker containerization are being actively added.

## About The Project
Python Log Eater is a lightweight script designed to parse and analyze web server logs (like Nginx or Apache). It extracts critical information such as IP addresses and HTTP status codes from raw log files.

This project serves as a practical exercise in scripting for DevOps, focusing on log analysis, regular expressions, and containerization.

## 🛠️ Built With
* **Python 3.x**
* **Regex (`re` module)**
* **Docker** *(Planned)*

## 🚀 Current Features
* Reads raw `access.log` files.
* Uses Regular Expressions (Regex) to extract client IP addresses and HTTP response codes.

## 📅 Planned Roadmap
- [x] Add `collections.Counter` to generate a summary report of HTTP status codes.
- [x] Containerize the application using Docker (`Dockerfile`).
- [x] Implement Docker Volumes to read log files from the host machine securely.

## 💻 How to run locally (Current version)

1. Clone the repository:
```bash
git clone [https://github.com/TwojaNazwaUzytkownika/python-log-eater.git](https://github.com/TwojaNazwaUzytkownika/python-log-eater.git)
