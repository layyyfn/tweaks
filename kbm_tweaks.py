import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import winreg
import json

# Constants for registry paths and default values
KEYBOARD_REG_PATH = r"Control Panel\Keyboard"
MOUSE_REG_PATH = r"Control Panel\Mouse"
DEFAULT_SETTINGS = {
    "KeyboardDelay": "1",
    "KeyboardSpeed": "31",
    "MouseSpeed": "1",
    "MouseThreshold1": "6",
    "MouseThreshold2": "10",
    "MouseSensitivity": "10",
}

# Global log for changes
log = []
undo_stack = []
redo_stack = []

def get_current_settings():
    """Retrieve the current keyboard and mouse settings from the registry."""
    try:
        # Read keyboard settings
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEYBOARD_REG_PATH, 0, winreg.KEY_READ)
        keyboard_delay = winreg.QueryValueEx(key, "KeyboardDelay")[0]
        keyboard_speed = winreg.QueryValueEx(key, "KeyboardSpeed")[0]
        winreg.CloseKey(key)

        # Read mouse settings
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, MOUSE_REG_PATH, 0, winreg.KEY_READ)
        mouse_speed = winreg.QueryValueEx(key, "MouseSpeed")[0]
        mouse_threshold1 = winreg.QueryValueEx(key, "MouseThreshold1")[0]
        mouse_threshold2 = winreg.QueryValueEx(key, "MouseThreshold2")[0]
        mouse_sensitivity = winreg.QueryValueEx(key, "MouseSensitivity")[0]
        winreg.CloseKey(key)

        return {
            "KeyboardDelay": keyboard_delay,
            "KeyboardSpeed": keyboard_speed,
            "MouseSpeed": mouse_speed,
            "MouseThreshold1": mouse_threshold1,
            "MouseThreshold2": mouse_threshold2,
            "MouseSensitivity": mouse_sensitivity,
        }
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read settings: {e}")
        return None

def apply_optimization():
    def run_optimization():
        # Get settings before optimization
        before_settings = get_current_settings()
        if before_settings is None:
            return  # Exit if settings could not be read

        selected_type = optimization_type.get()
        advanced = advanced_var.get()
        level = int(slider.get())

        # Display initial optimization details
        log.append(f"Starting optimization...")
        log.append(f"Optimization Type: {selected_type}")
        log.append(f"Advanced Optimization: {'Enabled' if advanced else 'Disabled'}")
        log.append(f"Optimization Level: {level}")

        # Simulate optimization progress
        progress_bar["value"] = 0
        progress_bar["maximum"] = 100
        try:
            for i in range(1, 101):  # Simulate progress in percentages
                root.after(5)  # Simulate work being done
                progress_bar["value"] = i
                root.update_idletasks()  # Keep the UI responsive

            # Apply optimizations based on the selected type
            if selected_type in ["Keyboard", "Both"]:
                optimize_keyboard(level, advanced)
            if selected_type in ["Mouse", "Both"]:
                optimize_mouse(level, advanced)

            # Get settings after optimization
            after_settings = get_current_settings()

            # Save to undo stack
            undo_stack.append(before_settings)
            redo_stack.clear()

            # Display before and after settings
            if after_settings:
                settings_message = (
                    f"Before Optimization:\n"
                    f"  Keyboard Delay: {before_settings['KeyboardDelay']}\n"
                    f"  Keyboard Speed: {before_settings['KeyboardSpeed']}\n"
                    f"  Mouse Speed: {before_settings['MouseSpeed']}\n"
                    f"  Mouse Threshold1: {before_settings['MouseThreshold1']}\n"
                    f"  Mouse Threshold2: {before_settings['MouseThreshold2']}\n"
                    f"  Mouse Sensitivity: {before_settings['MouseSensitivity']}\n\n"
                    f"After Optimization:\n"
                    f"  Keyboard Delay: {after_settings['KeyboardDelay']}\n"
                    f"  Keyboard Speed: {after_settings['KeyboardSpeed']}\n"
                    f"  Mouse Speed: {after_settings['MouseSpeed']}\n"
                    f"  Mouse Threshold1: {after_settings['MouseThreshold1']}\n"
                    f"  Mouse Threshold2: {after_settings['MouseThreshold2']}\n"
                    f"  Mouse Sensitivity: {after_settings['MouseSensitivity']}"
                )
                messagebox.showinfo("Optimization Results", settings_message)
                log.append(settings_message)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            log.append(f"Error: {e}")
        finally:
            progress_bar.stop()

    # Run the optimization logic in a separate thread
    threading.Thread(target=run_optimization, daemon=True).start()

def optimize_keyboard(level, advanced):
    try:
        # Open the registry key for keyboard settings
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEYBOARD_REG_PATH, 0, winreg.KEY_SET_VALUE)

        # Map the optimization level (0–100) to `KeyboardDelay` and `KeyboardSpeed`
        # `KeyboardDelay`: 3 (worst) at level 0, 0 (best) at level 100
        # `KeyboardSpeed`: 10 (slowest) at level 0, 31 (fastest) at level 100
        if level == 100:
            repeat_delay = 0  # Closest to 0 delay at max optimization
        else:
            repeat_delay = max(0, 3 - (level // 34))  # Maps 0–100 to 3–0

        repeat_speed = min(31, 10 + (level // 3))  # Maps 0–100 to 10–31

        # Apply the calculated settings to the registry
        winreg.SetValueEx(key, "KeyboardDelay", 0, winreg.REG_SZ, str(repeat_delay))
        winreg.SetValueEx(key, "KeyboardSpeed", 0, winreg.REG_SZ, str(repeat_speed))
        winreg.CloseKey(key)

        # Log the applied settings
        log.append(f"Keyboard optimized: Delay={repeat_delay}, Speed={repeat_speed}")
    except Exception as e:
        log.append(f"Failed to optimize keyboard: {e}")



def optimize_mouse(level, advanced):
    try:
        # Open the registry key for mouse settings
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, MOUSE_REG_PATH, 0, winreg.KEY_SET_VALUE)

        # Disable mouse acceleration if advanced is enabled
        acceleration = "0" if advanced else "1"  # Disable acceleration if advanced is enabled

        # Adjust mouse speed to simulate reduced delay (polling rate cannot be directly set via registry)
        # Higher levels reduce delay by setting MouseSpeed to a consistent value
        winreg.SetValueEx(key, "MouseSpeed", 0, winreg.REG_SZ, acceleration)
        winreg.SetValueEx(key, "MouseThreshold1", 0, winreg.REG_SZ, "0")
        winreg.SetValueEx(key, "MouseThreshold2", 0, winreg.REG_SZ, "0")

        # Do not modify MouseSensitivity
        log.append(f"Mouse optimized: Acceleration={'Disabled' if advanced else 'Enabled'}")
        winreg.CloseKey(key)
    except Exception as e:
        log.append(f"Failed to optimize mouse: {e}")

def reset_to_default():
    """Reset all settings to their default values."""
    try:
        # Reset keyboard settings
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEYBOARD_REG_PATH, 0, winreg.KEY_SET_VALUE)
        for setting, value in DEFAULT_SETTINGS.items():
            if "Keyboard" in setting:
                winreg.SetValueEx(key, setting, 0, winreg.REG_SZ, value)
        winreg.CloseKey(key)

        # Reset mouse settings
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, MOUSE_REG_PATH, 0, winreg.KEY_SET_VALUE)
        for setting, value in DEFAULT_SETTINGS.items():
            if "Mouse" in setting:
                winreg.SetValueEx(key, setting, 0, winreg.REG_SZ, value)
        winreg.CloseKey(key)

        messagebox.showinfo("Reset Complete", "All settings have been reset to their default values.")
        log.append("Settings reset to default.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to reset settings: {e}")
        log.append(f"Failed to reset settings: {e}")

def undo_changes():
    """Undo the last optimization."""
    if undo_stack:
        last_settings = undo_stack.pop()
        redo_stack.append(get_current_settings())
        apply_settings(last_settings)
        messagebox.showinfo("Undo", "Last optimization has been undone.")
        log.append("Undo performed.")
    else:
        messagebox.showinfo("Undo", "No changes to undo.")

def redo_changes():
    """Redo the last undone optimization."""
    if redo_stack:
        last_settings = redo_stack.pop()
        undo_stack.append(get_current_settings())
        apply_settings(last_settings)
        messagebox.showinfo("Redo", "Last undone optimization has been redone.")
        log.append("Redo performed.")
    else:
        messagebox.showinfo("Redo", "No changes to redo.")

def apply_settings(settings):
    """Apply the given settings to the registry."""
    try:
        # Apply keyboard settings
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, KEYBOARD_REG_PATH, 0, winreg.KEY_SET_VALUE)
        for setting, value in settings.items():
            if "Keyboard" in setting:
                winreg.SetValueEx(key, setting, 0, winreg.REG_SZ, value)
        winreg.CloseKey(key)

        # Apply mouse settings
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, MOUSE_REG_PATH, 0, winreg.KEY_SET_VALUE)
        for setting, value in settings.items():
            if "Mouse" in setting:
                winreg.SetValueEx(key, setting, 0, winreg.REG_SZ, value)
        winreg.CloseKey(key)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to apply settings: {e}")
        log.append(f"Failed to apply settings: {e}")

def save_profile():
    """Save the current settings to a file."""
    settings = get_current_settings()
    if settings:
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, "w") as file:
                json.dump(settings, file)
            messagebox.showinfo("Profile Saved", "Settings have been saved successfully.")
            log.append(f"Profile saved to {file_path}.")

def load_profile():
    """Load settings from a file and apply them."""
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                settings = json.load(file)
            apply_settings(settings)
            messagebox.showinfo("Profile Loaded", "Settings have been loaded successfully.")
            log.append(f"Profile loaded from {file_path}.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load profile: {e}")
            log.append(f"Failed to load profile: {e}")

def export_log():
    """Export the log to a text file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write("\n".join(log))
        messagebox.showinfo("Log Exported", "Log has been exported successfully.")
        log.append(f"Log exported to {file_path}.")

# Create the main application window
root = tk.Tk()
root.title("Layyys KBM Optimizer")

# Set the application icon
try:
    root.iconbitmap("../../../Downloads/black-l10.ico")  # Use the .ico file for the icon
except Exception as e:
    print("Icon not found or invalid. Please ensure 'black-l10.ico' is in the specified directory.")

# Add a label
label = tk.Label(root, text="Layyys Keyboard & Mouse Optimizer", font=("Arial", 16))
label.pack(pady=10)

# Add a dropdown for optimization type
optimization_type_label = tk.Label(root, text="Select Optimization Type:")
optimization_type_label.pack()

optimization_type = ttk.Combobox(root, values=["Keyboard", "Mouse", "Both"], state="readonly")
optimization_type.set("Both")  # Default value
optimization_type.pack(pady=5)

# Add a slider (scale)
slider_label = tk.Label(root, text="Optimization Level (100 - 0):")
slider_label.pack()

slider = ttk.Scale(root, from_=100, to=0, orient="horizontal")
slider.pack(pady=10)

# Add a checkbox for advanced optimization
advanced_var = tk.BooleanVar()
advanced_checkbox = tk.Checkbutton(root, text="Enable Advanced Optimization", variable=advanced_var)
advanced_checkbox.pack(pady=5)

# Add a progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)

# Add buttons for additional features
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

apply_button = tk.Button(button_frame, text="Apply Optimization", command=apply_optimization)
apply_button.grid(row=0, column=0, padx=5)

reset_button = tk.Button(button_frame, text="Reset to Default", command=reset_to_default)
reset_button.grid(row=0, column=1, padx=5)

save_button = tk.Button(button_frame, text="Save Profile", command=save_profile)
save_button.grid(row=0, column=2, padx=5)

load_button = tk.Button(button_frame, text="Load Profile", command=load_profile)
load_button.grid(row=0, column=3, padx=5)

export_log_button = tk.Button(button_frame, text="Export Log", command=export_log)
export_log_button.grid(row=0, column=4, padx=5)

undo_button = tk.Button(button_frame, text="Undo", command=undo_changes)
undo_button.grid(row=1, column=0, padx=5)

redo_button = tk.Button(button_frame, text="Redo", command=redo_changes)
redo_button.grid(row=1, column=1, padx=5)

# Run the application
root.mainloop()
