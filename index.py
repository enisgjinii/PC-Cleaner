import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import customtkinter as ctk
import os
import shutil
import psutil
import threading
import logging
from PIL import Image, ImageTk
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PCCleanerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI-Powered PC Cleaner 2024")
        self.geometry("1000x600")
        
        self.resizable(False, False)
        # self.attributes('-toolwindow', True)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.setup_ui()
        self.setup_logging()
        self.setup_ai_model()

    def setup_ui(self):
        # Sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="PC Cleaner", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text="Cleaning", command=self.show_cleaning_frame)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text="System Info", command=self.show_system_info_frame)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, text="Disk Analyzer", command=self.show_disk_analyzer_frame)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        # Main frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Cleaning frame
        self.cleaning_frame = ctk.CTkFrame(self.main_frame)
        self.quick_clean_btn = ctk.CTkButton(self.cleaning_frame, text="Quick Clean", command=self.quick_clean)
        self.quick_clean_btn.pack(pady=10)
        self.deep_clean_btn = ctk.CTkButton(self.cleaning_frame, text="Deep Clean", command=self.deep_clean)
        self.deep_clean_btn.pack(pady=10)

        # System info frame
        self.system_info_frame = ctk.CTkFrame(self.main_frame)
        self.cpu_label = ctk.CTkLabel(self.system_info_frame, text="CPU Usage: ")
        self.cpu_label.pack(pady=5)
        self.memory_label = ctk.CTkLabel(self.system_info_frame, text="Memory Usage: ")
        self.memory_label.pack(pady=5)
        self.disk_label = ctk.CTkLabel(self.system_info_frame, text="Disk Usage: ")
        self.disk_label.pack(pady=5)

        # Disk analyzer frame
        self.disk_analyzer_frame = ctk.CTkFrame(self.main_frame)
        self.analyze_btn = ctk.CTkButton(self.disk_analyzer_frame, text="Analyze Disk", command=self.analyze_disk)
        self.analyze_btn.pack(pady=10)
        self.disk_tree = ttk.Treeview(self.disk_analyzer_frame, columns=('size', 'type'), show='tree headings')
        self.disk_tree.heading('size', text='Size')
        self.disk_tree.heading('type', text='Type')
        self.disk_tree.pack(expand=True, fill='both')

        # Log frame
        self.log_frame = ctk.CTkFrame(self.main_frame)
        self.log_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.log_frame.grid_columnconfigure(0, weight=1)
        self.log_frame.grid_rowconfigure(0, weight=1)

        self.log_text = ctk.CTkTextbox(self.log_frame, height=10)
        self.log_text.grid(row=0, column=0, sticky="nsew")

        self.show_cleaning_frame()
        # Add AI Recommendations button
        self.ai_recommend_btn = ctk.CTkButton(self.cleaning_frame, text="AI Recommendations", command=self.get_ai_recommendations)
        self.ai_recommend_btn.pack(pady=10)

        # Add System Health Prediction
        self.health_predict_btn = ctk.CTkButton(self.system_info_frame, text="Predict System Health", command=self.predict_system_health)
        self.health_predict_btn.pack(pady=10)

        # Add Intelligent File Categorization
        self.categorize_btn = ctk.CTkButton(self.disk_analyzer_frame, text="Intelligent Categorization", command=self.intelligent_categorization)
        self.categorize_btn.pack(pady=10)

    def setup_ai_model(self):
        # In a real scenario, you'd load a pre-trained model
        # For this example, we'll create a simple model
        self.model = RandomForestClassifier(n_estimators=10)
        
        # Dummy training data
        X = np.random.rand(100, 3)  # 3 features: CPU, Memory, Disk usage
        y = np.random.choice(['Clean', 'Optimize', 'No Action'], 100)
        
        self.model.fit(X, y)

    def get_ai_recommendations(self):
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        
        features = np.array([[cpu, memory, disk]])
        recommendation = self.model.predict(features)[0]
        
        self.log_message(f"AI Recommendation: {recommendation}")
        messagebox.showinfo("AI Recommendation", f"Based on current system state, the AI recommends: {recommendation}")

    def predict_system_health(self):
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        
        health_score = 100 - (cpu + memory + disk) / 3
        
        self.log_message(f"Predicted System Health: {health_score:.2f}%")
        messagebox.showinfo("System Health Prediction", f"Your system health score is: {health_score:.2f}%")

    def intelligent_categorization(self):
        folder = filedialog.askdirectory()
        if folder:
            self.log_message("Starting intelligent file categorization...")
            threading.Thread(target=self._categorize_files, args=(folder,), daemon=True).start()

    def _categorize_files(self, folder):
        categories = {
            'Documents': ['.txt', '.doc', '.docx', '.pdf'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif'],
            'Videos': ['.mp4', '.avi', '.mov'],
            'Audio': ['.mp3', '.wav', '.flac'],
            'Archives': ['.zip', '.rar', '.7z']
        }

        categorized_files = {cat: [] for cat in categories}
        
        for root, _, files in os.walk(folder):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                for category, extensions in categories.items():
                    if ext in extensions:
                        categorized_files[category].append(os.path.join(root, file))
                        break

        for category, files in categorized_files.items():
            self.log_message(f"{category}: {len(files)} files")

        messagebox.showinfo("Categorization Complete", "File categorization completed. Check the log for details.")

    def setup_logging(self):
        self.logger = logging.getLogger('PCCleaner')
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def log_message(self, message):
        self.logger.info(message)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def show_cleaning_frame(self):
        self.cleaning_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.system_info_frame.grid_forget()
        self.disk_analyzer_frame.grid_forget()

    def show_system_info_frame(self):
        self.system_info_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.cleaning_frame.grid_forget()
        self.disk_analyzer_frame.grid_forget()
        self.update_system_info()

    def show_disk_analyzer_frame(self):
        self.disk_analyzer_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.cleaning_frame.grid_forget()
        self.system_info_frame.grid_forget()

    def quick_clean(self):
        self.log_message("Starting quick clean...")
        threading.Thread(target=self._quick_clean, daemon=True).start()

    def _quick_clean(self):
        try:
            self.clear_temp_files()
            self.clear_recycle_bin()
            self.log_message("Quick clean completed.")
        except Exception as e:
            self.log_message(f"Error during quick clean: {str(e)}")

    def deep_clean(self):
        self.log_message("Starting deep clean...")
        threading.Thread(target=self._deep_clean, daemon=True).start()

    def _deep_clean(self):
        try:
            self._quick_clean()
            self.clear_windows_update_cache()
            self.clear_browser_cache()
            self.log_message("Deep clean completed.")
        except Exception as e:
            self.log_message(f"Error during deep clean: {str(e)}")

    def clear_temp_files(self):
        temp_folders = [os.environ.get('TEMP'), os.environ.get('TMP')]
        for folder in temp_folders:
            if folder and os.path.exists(folder):
                for root, dirs, files in os.walk(folder, topdown=False):
                    for name in files:
                        try:
                            file_path = os.path.join(root, name)
                            os.unlink(file_path)
                        except Exception as e:
                            self.log_message(f"Error deleting {file_path}: {str(e)}")
                    for name in dirs:
                        try:
                            dir_path = os.path.join(root, name)
                            os.rmdir(dir_path)
                        except Exception as e:
                            self.log_message(f"Error deleting directory {dir_path}: {str(e)}")

    def clear_recycle_bin(self):
        try:
            import winshell
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
            self.log_message("Recycle Bin cleared.")
        except ImportError:
            self.log_message("winshell module not found. Unable to clear Recycle Bin.")
        except Exception as e:
            self.log_message(f"Error clearing Recycle Bin: {str(e)}")

    def clear_windows_update_cache(self):
        windows_update_cache = r"C:\Windows\SoftwareDistribution\Download"
        try:
            if os.path.exists(windows_update_cache):
                shutil.rmtree(windows_update_cache)
                os.mkdir(windows_update_cache)
            self.log_message("Windows Update cache cleared.")
        except Exception as e:
            self.log_message(f"Error clearing Windows Update cache: {str(e)}")

    def clear_browser_cache(self):
        chrome_cache = os.path.join(os.environ['LOCALAPPDATA'], r"Google\Chrome\User Data\Default\Cache")
        try:
            if os.path.exists(chrome_cache):
                shutil.rmtree(chrome_cache)
            self.log_message("Browser cache cleared.")
        except Exception as e:
            self.log_message(f"Error clearing browser cache: {str(e)}")

    def update_system_info(self):
        cpu_usage = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        self.cpu_label.configure(text=f"CPU Usage: {cpu_usage}%")
        self.memory_label.configure(text=f"Memory Usage: {memory.percent}%")
        self.disk_label.configure(text=f"Disk Usage: {disk.percent}%")

        self.after(1000, self.update_system_info)

    def analyze_disk(self):
        folder = filedialog.askdirectory()
        if folder:
            self.disk_tree.delete(*self.disk_tree.get_children())
            threading.Thread(target=self._analyze_folder, args=(folder, ""), daemon=True).start()

    def _analyze_folder(self, folder, parent):
        total_size = 0
        try:
            for item in os.listdir(folder):
                path = os.path.join(folder, item)
                try:
                    size = os.path.getsize(path)
                    total_size += size
                    if os.path.isdir(path):
                        folder_id = self.disk_tree.insert(parent, 'end', text=item, values=(f"{size/1024/1024:.2f} MB", "Folder"))
                        subfolder_size = self._analyze_folder(path, folder_id)
                        total_size += subfolder_size
                        self.disk_tree.item(folder_id, values=(f"{(size+subfolder_size)/1024/1024:.2f} MB", "Folder"))
                    else:
                        self.disk_tree.insert(parent, 'end', text=item, values=(f"{size/1024/1024:.2f} MB", "File"))
                except Exception as e:
                    self.log_message(f"Error accessing {path}: {str(e)}")
        except Exception as e:
            self.log_message(f"Error analyzing folder {folder}: {str(e)}")
        return total_size

if __name__ == "__main__":
    app = PCCleanerApp()
    app.mainloop()
