import tkinter as tk
from tkinter import filedialog, ttk, messagebox

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Track changes for enabling/disabling "Apply" button
        self.changes_made = False

        # Track if configuration has been applied
        self.configuration_applied = False

        # Set the title of the window
        self.title("Test GUI")

        # Center the window on the screen
        self.center_window(500, 400)

        # Start with the main menu
        self.main_menu()

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def main_menu(self):
        # Reset window size to default when showing the main menu
        #self.geometry("400x500")
        self.center_window(300, 400)
        
        # Restore the default close behavior
        self.protocol("WM_DELETE_WINDOW", self.quit)

        # Disable buttons if configuration not applied
        state = tk.NORMAL if self.configuration_applied else tk.DISABLED

        configure_button = tk.Button(self, text="Configure")
        calibrate_button = tk.Button(self, text="Cameras Calibration")
        # Define the button with different labels
        annotate_2d_button = tk.Button(self, text="2D Annotation")
        annotate_3d_button = tk.Button(self, text="3D Kinematics")

        label_2d_button = tk.Button(self, text="2D Video Labelling")
        label_3d_button = tk.Button(self, text="3D Video Labelling")

        exit_button = tk.Button(self, text="Exit", command=self.quit)

        button_ypadding = 10
        configure_button.pack(pady=button_ypadding)
        annotate_2d_button.pack(pady=button_ypadding)
        label_2d_button.pack(pady=button_ypadding)
        calibrate_button.pack(pady=button_ypadding)
        annotate_3d_button.pack(pady=button_ypadding)
        label_3d_button.pack(pady=button_ypadding)
        exit_button.pack(pady=button_ypadding)


# Run the application
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()