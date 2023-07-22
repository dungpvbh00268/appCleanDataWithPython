

# =====================///
# import tkinter as tk
# from tkinter import filedialog
# import pandas as pd
# import tkinter.messagebox as messagebox
# from tkinter import ttk
# from io import StringIO
# import tkinter as tk

# class DataCleaningApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Data Cleaning App (By DungPham2209)")
        
        
#         # Set the window size and put the app in fullscreen mode
#         window_width = self.root.winfo_screenwidth() * 0.9
#         window_height = self.root.winfo_screenheight() * 0.9
#         self.root.geometry("%dx%d+0+0" % (window_width, window_height))
        
#         # Add the title label with formatted text
#         title_label = tk.Label(root, text="Data Cleaning App ", font=("Helvetica", 18, "bold"), background="#F0F0F0", foreground="#2B579A")
#         title_label.pack(pady=5)
        
#         # Add the (By DungPham2209) label with smaller font size
#         author_label = tk.Label(root, text="(By DungPham2209)", font=("Helvetica", 10), fg="gray")
#         author_label.pack(pady=5)

#         data_frame = tk.Frame(root, borderwidth=2, relief="groove")
#         data_frame.pack(padx=10, pady=5, fill="both", expand=True)

#         # Create a container (frame) to hold the Treeview widget and vertical scrollbar
#         data_container = ttk.Frame(data_frame)
#         data_container.pack(side="left", fill="both", expand=True)

#         # Create a Treeview widget to display data
#         self.data_tree = ttk.Treeview(data_container, show="headings")  # Hide the default first column
#         self.data_tree.pack(side="left", padx=5, pady=5, fill="both", expand=True)

#         v_scrollbar = ttk.Scrollbar(data_frame, orient="vertical", command=self.data_tree.yview)
#         v_scrollbar.pack(side="right", fill="y")
#         self.data_tree.configure(yscrollcommand=v_scrollbar.set)

#         # Create a horizontal scrollbar for the Treeview
#         h_scrollbar = ttk.Scrollbar(root, orient="horizontal", command=self.data_tree.xview)
#         h_scrollbar.pack(side="bottom", fill="x")
#         self.data_tree.configure(xscrollcommand=h_scrollbar.set)

#         button_frame = tk.Frame(root)
#         button_frame.pack(side="top", padx=5, pady=5, anchor="w")

#         file_menu = tk.Menu(root, tearoff=0)
#         file_menu.add_command(label="Open", command=self.open_csv)
#         file_menu.add_command(label="Save", command=self.save_csv)  # Gọi đến phương thức save_csv
#         file_menu.add_command(label="Save As", command=self.save_as_csv)  # Gọi đến phương thức save_as_csv

#         edit_menu = tk.Menu(root, tearoff=0)

#         about_menu = tk.Menu(root, tearoff=0)
#         about_menu.add_command(label="By DungPham2209")

#         main_menu = tk.Menu(root)
#         main_menu.add_cascade(label="File", menu=file_menu)
#         main_menu.add_cascade(label="Edit", menu=edit_menu)
#         main_menu.add_cascade(label="About", menu=about_menu)
#         root.config(menu=main_menu)

    
        
#         # load_button = tk.Button(button_frame, text="Load CSV", command=self.open_csv)
#         load_button = tk.Button(button_frame, text="Reload Data", command=self.reload_data)
#         load_button.pack(side="left", padx=5)

#         clean_button = tk.Button(button_frame, text="Clean Data", command=self.clean_data)
#         clean_button.pack(side="left", padx=5)

#     def reload_data(self):
#         if hasattr(self, "current_file_path"):
#             df = pd.read_csv(self.current_file_path)
#             self.display_data(df)
#         else:
#             messagebox.showwarning("No Data", "Please load a CSV file first.")
    
#     def open_csv(self):
#         file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
#         if file_path:
#             df = pd.read_csv(file_path)
#             self.display_data(df)
#             self.current_file_path = file_path

#     def display_data(self, df):
#         """Display DataFrame in Treeview widget"""
#         self.data_tree.delete(*self.data_tree.get_children())
#         # Set up columns
#         self.data_tree["columns"] = list(df.columns)
#         for col in self.data_tree["columns"]:
#             col_width = max(len(str(df[col].max())), len(col))
#             self.data_tree.heading(col, text=col)
#             self.data_tree.column(col, width=col_width * 10, anchor="center")  # Adjust the multiplier for desired width and anchor to center
#         # Insert data
#         for i, row in df.iterrows():
#             values = [str(val) for val in row.tolist()]
#             self.data_tree.insert("", "end", values=values)

#     def clean_data(self):
#         data = ""
#         for item in self.data_tree.get_children():
#             values = self.data_tree.item(item)["values"]
#             row_data = ",".join(str(val) for val in values) + "\n"
#             data += row_data
#         # Convert the data string to a Pandas DataFrame
#         df = pd.read_csv(pd.compat.StringIO(data))
#         # Clean the data by dropping duplicate rows
#         df.drop_duplicates(inplace=True)
#         # Display the cleaned DataFrame in the Treeview widget
#         self.display_data(df)

#     def save_as_csv(self):
#         data = ""
#         for item in self.data_tree.get_children():
#             values = self.data_tree.item(item)["values"]
#             row_data = ",".join(str(val) for val in values) + "\n"
#             data += row_data
#         if not data:
#             messagebox.showerror("Error", "Nothing to save. The data is empty!")
#             return
#         df = pd.read_csv(StringIO(data))
#         if df.isnull().values.any():
#             messagebox.showerror("Error", "Cannot save data with null values!")
#         else:
#             file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
#             if file_path:
#                 # Add the column names to the beginning of the data string
#                 column_names = ",".join(str(col) for col in self.data_tree["columns"]) + "\n"
#                 data = column_names + data
#                 with open(file_path, "w") as f:
#                     f.write(data)
#                 messagebox.showinfo("Success", "Data has been saved successfully!")

#     def save_csv(self):
#         data = ""
#         for item in self.data_tree.get_children():
#             values = self.data_tree.item(item)["values"]
#             row_data = ",".join(str(val) for val in values) + "\n"
#             data += row_data
#         if not data:
#             messagebox.showerror("Error", "Nothing to save. The data is empty!")
#             return
#         if hasattr(self, "current_file_path"):
#             df = pd.read_csv(StringIO(data))
#             if df.isnull().values.any():
#                 messagebox.showerror("Error", "Cannot save data with null values!")
#             else:
#                 # Add the column names to the beginning of the data string
#                 column_names = ",".join(str(col) for col in self.data_tree["columns"]) + "\n"
#                 data = column_names + data
#                 with open(self.current_file_path, "w") as f:
#                     f.write(data)
#                 messagebox.showinfo("Success", "Data has been saved successfully!")
#         else:
#             messagebox.showerror("Error", "No file has been opened. Please use 'Save As' to save the data to a new file.")

#         column_names = ",".join(str(col) for col in self.data_tree["columns"]) + "\n"
#         data = column_names + data

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DataCleaningApp(root)
#     root.mainloop()



import tkinter as tk
from tkinter import filedialog
import pandas as pd
from tkinter import ttk
from ttkthemes import ThemedStyle
import tkinter.messagebox as messagebox
from io import StringIO
import webbrowser



class DataCleaningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Cleaning App (By DungPham2209)")

        # Set the window size and put the app in fullscreen mode
        window_width = self.root.winfo_screenwidth() * 0.9
        window_height = self.root.winfo_screenheight() * 0.9
        self.root.geometry("%dx%d+0+0" % (window_width, window_height))

        # Use ThemedStyle to customize the appearance
        style = ThemedStyle(root)
        style.set_theme("arc")  # You can choose a different theme here

        # Add the title label with formatted text
        title_label = ttk.Label(root, text="Data Cleaning App", font=("Helvetica", 18, "bold"), background="#F0F0F0", foreground="#2B579A")
        title_label.pack(pady=10)


        # Add the (By DungPham2209) label with smaller font size
        author_label = ttk.Label(root, text="(By DungPham2209)", font=("Helvetica", 10), foreground="#333")
        author_label.pack()


        data_frame = ttk.Frame(root, borderwidth=2, relief="groove")
        data_frame.pack(padx=10, pady=5, fill="both", expand=True)

        # Create a container (frame) to hold the Treeview widget and vertical scrollbar
        data_container = ttk.Frame(data_frame)
        data_container.pack(side="left", fill="both", expand=True)

        # Create a Treeview widget to display data
        self.data_tree = ttk.Treeview(data_container, show="headings")  # Hide the default first column
        self.data_tree.pack(side="left", padx=5, pady=5, fill="both", expand=True)

        v_scrollbar = ttk.Scrollbar(data_frame, orient="vertical", command=self.data_tree.yview)
        v_scrollbar.pack(side="right", fill="y")
        self.data_tree.configure(yscrollcommand=v_scrollbar.set)

        # Create a horizontal scrollbar for the Treeview
        h_scrollbar = ttk.Scrollbar(root, orient="horizontal", command=self.data_tree.xview)
        h_scrollbar.pack(side="bottom", fill="x")
        self.data_tree.configure(xscrollcommand=h_scrollbar.set)

        button_frame = ttk.Frame(root)
        button_frame.pack(side="top", padx=5, pady=5, anchor="w")

        file_menu = tk.Menu(root, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_csv)
        file_menu.add_command(label="Save", command=self.save_csv)
        file_menu.add_command(label="Save As", command=self.save_as_csv)

        edit_menu = tk.Menu(root, tearoff=0)
        about_menu = tk.Menu(root, tearoff=0)
        about_menu.add_command(label="By DungPham2209", command=lambda: webbrowser.open("https://www.facebook.com/100010290584323"))

        main_menu = tk.Menu(root)
        main_menu.add_cascade(label="File", menu=file_menu)
        main_menu.add_cascade(label="Edit", menu=edit_menu)
        main_menu.add_cascade(label="About", menu=about_menu)
        root.config(menu=main_menu)

        load_button = ttk.Button(button_frame, text="Reload Data", command=self.reload_data)
        load_button.pack(side="left", padx=5)

        clean_button = ttk.Button(button_frame, text="Clean Data", command=self.clean_data)
        clean_button.pack(side="left", padx=5)


    def reload_data(self):
        if hasattr(self, "current_file_path"):
            df = pd.read_csv(self.current_file_path)
            self.display_data(df)
        else:
            messagebox.showwarning("No Data", "Please load a CSV file first.")

    def open_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            df = pd.read_csv(file_path)
            self.display_data(df)
            self.current_file_path = file_path

    def display_data(self, df):
        """Display DataFrame in Treeview widget"""
        self.data_tree.delete(*self.data_tree.get_children())
        # Set up columns
        self.data_tree["columns"] = list(df.columns)
        for col in self.data_tree["columns"]:
            col_width = max(len(str(df[col].max())), len(col))
            self.data_tree.heading(col, text=col)
            self.data_tree.column(col, width=col_width * 10, anchor="center")  # Adjust the multiplier for desired width and anchor to center
        # Insert data
        for i, row in df.iterrows():
            values = [str(val) for val in row.tolist()]
            self.data_tree.insert("", "end", values=values)

    def clean_data(self):
        data = ""
        for item in self.data_tree.get_children():
            values = self.data_tree.item(item)["values"]
            row_data = ",".join(str(val) for val in values) + "\n"
            data += row_data
        # Convert the data string to a Pandas DataFrame
        df = pd.read_csv(StringIO(data))
        # Clean the data by dropping duplicate rows
        df.drop_duplicates(inplace=True)
        # Display the cleaned DataFrame in the Treeview widget
        self.display_data(df)

    def save_as_csv(self):
        data = ""
        for item in self.data_tree.get_children():
            values = self.data_tree.item(item)["values"]
            row_data = ",".join(str(val) for val in values) + "\n"
            data += row_data
        if not data:
            messagebox.showerror("Error", "Nothing to save. The data is empty!")
            return
        df = pd.read_csv(StringIO(data))
        if df.isnull().values.any():
            messagebox.showerror("Error", "Cannot save data with null values!")
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if file_path:
                # Add the column names to the beginning of the data string
                column_names = ",".join(str(col) for col in self.data_tree["columns"]) + "\n"
                data = column_names + data
                with open(file_path, "w") as f:
                    f.write(data)
                messagebox.showinfo("Success", "Data has been saved successfully!")

    def save_csv(self):
        data = ""
        for item in self.data_tree.get_children():
            values = self.data_tree.item(item)["values"]
            row_data = ",".join(str(val) for val in values) + "\n"
            data += row_data
        if not data:
            messagebox.showerror("Error", "Nothing to save. The data is empty!")
            return
        if hasattr(self, "current_file_path"):
            df = pd.read_csv(StringIO(data))
            if df.isnull().values.any():
                messagebox.showerror("Error", "Cannot save data with null values!")
            else:
                # Add the column names to the beginning of the data string
                column_names = ",".join(str(col) for col in self.data_tree["columns"]) + "\n"
                data = column_names + data
                with open(self.current_file_path, "w") as f:
                    f.write(data)
                messagebox.showinfo("Success", "Data has been saved successfully!")
        else:
            messagebox.showerror("Error", "No file has been opened. Please use 'Save As' to save the data to a new file.")

        column_names = ",".join(str(col) for col in self.data_tree["columns"]) + "\n"
        data = column_names + data

if __name__ == "__main__":
    root = tk.Tk()
    app = DataCleaningApp(root)
    root.mainloop()