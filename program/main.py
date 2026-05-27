import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import sys
from datetime import datetime

def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(os.path.dirname(__file__), relative)

class ReactorMonitorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Система учёта параметров реакторных установок")
        self.geometry("900x600")
        self.resizable(True, True)
        self.configure(bg="#f0f4f8")
        self._build_ui()

    def _build_ui(self):
        # Шапка
        header = tk.Frame(self, bg="#1a3a5c", height=60)
        header.pack(fill="x")
        tk.Label(header, text="Система учёта параметров реакторных установок",
                 bg="#1a3a5c", fg="white", font=("Arial", 13, "bold")).pack(side="left", padx=16, pady=14)
        tk.Label(header, text="v1.0.0",
                 bg="#1a3a5c", fg="#aac4e0", font=("Arial", 10)).pack(side="right", padx=16)

        # Панель статуса
        status_frame = tk.Frame(self, bg="#e8f0fb", relief="flat", bd=0)
        status_frame.pack(fill="x", padx=0, pady=0)
        tk.Label(status_frame, text="● Система работает в штатном режиме",
                 bg="#e8f0fb", fg="#2e6da4", font=("Arial", 10)).pack(side="left", padx=12, pady=6)
        self.time_label = tk.Label(status_frame, text="", bg="#e8f0fb", fg="#555", font=("Arial", 10))
        self.time_label.pack(side="right", padx=12)
        self._update_time()

        # Основная область
        main = tk.Frame(self, bg="#f0f4f8")
        main.pack(fill="both", expand=True, padx=20, pady=16)

        # Левая колонка — меню разделов
        left = tk.Frame(main, bg="#ffffff", relief="solid", bd=1, width=200)
        left.pack(side="left", fill="y", padx=(0, 14))
        left.pack_propagate(False)

        tk.Label(left, text="Разделы", bg="#dce8f5", fg="#1a3a5c",
                 font=("Arial", 11, "bold"), anchor="w").pack(fill="x", padx=8, pady=6)

        sections = [
            "Журнал измерений",
            "Тревожная сигнализация",
            "Расчёт выгорания",
            "Учёт доз облучения",
            "Электронная подпись",
            "Отчёты",
            "Настройки",
        ]
        for s in sections:
            btn = tk.Button(left, text=s, anchor="w", relief="flat",
                            bg="#ffffff", fg="#1a3a5c", font=("Arial", 10),
                            command=lambda n=s: self._show_stub(n))
            btn.pack(fill="x", padx=6, pady=2)

        # Правая область — приветствие
        right = tk.Frame(main, bg="#ffffff", relief="solid", bd=1)
        right.pack(side="left", fill="both", expand=True)

        tk.Label(right, text="Добро пожаловать",
                 bg="#ffffff", fg="#1a3a5c", font=("Arial", 16, "bold")).pack(pady=(40, 8))
        tk.Label(right,
                 text="Система учёта параметров реакторных установок\n"
                      "предназначена для ведения электронного журнала\n"
                      "измерений, контроля параметров и формирования отчётов.",
                 bg="#ffffff", fg="#444", font=("Arial", 11), justify="center").pack(pady=8)

        tk.Label(right, text="Выберите раздел в меню слева для начала работы.",
                 bg="#ffffff", fg="#888", font=("Arial", 10, "italic")).pack(pady=4)

        # Кнопки внизу
        btn_frame = tk.Frame(right, bg="#ffffff")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Открыть справку (F1)", width=22,
                  bg="#2e6da4", fg="white", font=("Arial", 10),
                  relief="flat", command=self._open_help).pack(side="left", padx=6)

        tk.Button(btn_frame, text="Выход", width=12,
                  bg="#e8e8e8", fg="#333", font=("Arial", 10),
                  relief="flat", command=self.destroy).pack(side="left", padx=6)

        self.bind("<F1>", lambda e: self._open_help())

    def _update_time(self):
        self.time_label.config(text=datetime.now().strftime("%d.%m.%Y  %H:%M:%S"))
        self.after(1000, self._update_time)

    def _show_stub(self, name):
        messagebox.showinfo("Раздел", f"Раздел «{name}»\nФункциональность в разработке.")

    def _open_help(self):
        help_path = resource_path(os.path.join("help", "index.html"))
        if os.path.exists(help_path):
            os.startfile(help_path)
        else:
            messagebox.showwarning("Справка", "Файл справки не найден.\nУбедитесь, что папка help находится рядом с программой.")

if __name__ == "__main__":
    app = ReactorMonitorApp()
    app.mainloop()
