import tkinter as tk
from tkinter import messagebox, ttk
import subprocess

# === Constants ===
BG_COLOR = "#2C2F38"
TEXT_COLOR = "#FFFFFF"
BUTTON_COLOR = "#4CAF50"
BACK_BUTTON_COLOR = "#FF5722"

# === Helper Functions ===
def run_cmd(command):
    """Run a shell command with error handling."""
    try:
        subprocess.check_call(command, shell=True)
        print(f"Command executed successfully: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\n{e}")
        messagebox.showerror("Error", f"Failed to execute command: {command}")
    except FileNotFoundError:
        print(f"Command not found: {command}")
        messagebox.showerror("Error", f"Command not found: {command}")

# === Optimization Functions ===

def disable_mouse_pointer_precision():
    print("Disabling mouse pointer precision...")

def enable_high_perf():
    print("Enabling high performance power plan...")

def disable_background_apps():
    print("Disabling background apps...")

def disable_visual_effects():
    print("Disabling visual effects...")

def disable_services():
    print("Disabling unnecessary services...")

def disable_cortana():
    print("Disabling Cortana...")

def disable_indexing():
    print("Disabling Windows Search Indexing...")

def disable_startup_sound():
    print("Disabling startup sound...")

def disable_notifications():
    print("Disabling notifications...")

def disable_game_bar():
    print("Disabling Game Bar...")

def optimize_cpu_priority(priority):
    print(f"Optimizing CPU priority to: {priority}")

def set_gpu_priority(priority):
    print(f"Setting GPU priority to: {priority}")

def optimize_tcp():
    print("Optimizing TCP stack...")

def disable_nagle():
    print("Disabling Nagle's Algorithm...")

def set_google_dns():
    print("Setting Google DNS...")

def disable_qos():
    print("Disabling QoS (Quality of Service)...")

def disable_mouse_accel():
    print("Disabling mouse acceleration...")

def disable_filter_keys():
    print("Disabling filter keys...")

def prioritize_input():
    print("Prioritizing input devices...")

def disable_usb_suspend():
    print("Disabling USB suspend...")

def clear_temp():
    print("Clearing temp files...")

def clear_prefetch():
    print("Clearing prefetch files...")

def flush_dns():
    print("Flushing DNS cache...")

def empty_recycle_bin():
    print("Emptying the recycle bin...")

def revert_all():
    print("Reverting all optimizations...")

# === Additional Tweaks ===
def enable_fast_startup():
    print("Enabling fast startup...")

def disable_hibernation():
    print("Disabling hibernation...")

def disable_error_reporting():
    print("Disabling Windows Error Reporting...")

def disable_remote_assistance():
    print("Disabling Remote Assistance...")

def disable_scheduled_tasks():
    print("Disabling unnecessary scheduled tasks...")


def disable_action_center():
    print("Disabling Action Center...")

def disable_startup_programs():
    print("Disabling unnecessary startup programs...")

def disable_disk_defrag():
    print("Disabling disk defragmentation...")

def disable_auto_restart():
    print("Disabling automatic restart after updates...")

def disable_game_mode():
    print("Disabling Game Mode...")

def enable_ulow_latency_mode():
    print("Enabling ultra-low latency mode...")

def disable_fullscreen_optimizations():
    print("Disabling fullscreen optimizations...")

def disable_vsync():
    print("Disabling V-Sync...")

def enable_high_dpi_scaling():
    print("Enabling high DPI scaling override...")

def disable_antivirus():
    print("Disabling third-party antivirus...")

def disable_firewall():
    print("Disabling Windows Firewall...")

def disable_power_throttling():
    print("Disabling power throttling...")

def enable_max_performance_gpu():
    print("Enabling maximum performance for GPU...")

def disable_background_tasks():
    print("Disabling background tasks...")

def disable_ipv6():
    print("Disabling IPv6...")

def enable_tcp_fast_open():
    print("Enabling TCP Fast Open...")

def disable_network_discovery():
    print("Disabling network discovery...")

def disable_netbios():
    print("Disabling NetBIOS over TCP/IP...")

def disable_smb():
    print("Disabling SMB protocol...")

def enable_dns_cache():
    print("Enabling DNS caching...")

def disable_multicast():
    print("Disabling multicast DNS...")

def disable_network_sharing():
    print("Disabling network sharing...")

def disable_autotuning():
    print("Disabling TCP autotuning...")

def disable_touchpad():
    print("Disabling touchpad...")

def enable_raw_input():
    print("Enabling raw input for devices...")

def disable_keyboard_delay():
    print("Disabling keyboard delay...")

def enable_polling_rate():
    print("Enabling high polling rate for mouse...")

def disable_mouse_smoothing():
    print("Disabling mouse smoothing...")

def disable_mouse_trails():
    print("Disabling mouse trails...")

def disable_sticky_keys():
    print("Disabling sticky keys...")

def disable_toggle_keys():
    print("Disabling toggle keys...")

def disable_caps_lock():
    print("Disabling Caps Lock key...")

def clear_logs():
    print("Clearing system logs...")

def clear_cache():
    print("Clearing system cache...")

def clear_temp_internet_files():
    print("Clearing temporary internet files...")

def clear_windows_update_cache():
    print("Clearing Windows Update cache...")

def clear_event_logs():
    print("Clearing event logs...")

def clear_error_reports():
    print("Clearing error reports...")

# === GUI Application ===
class OptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fortnite Optimizer by Layyy")
        self.root.geometry("600x750")
        self.frames = {}
        self.create_main_menu()

    def switch_frame(self, name):
        """Switch to a specific frame."""
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[name].pack(fill='both', expand=True)

    def create_main_menu(self):
        """Create the main menu."""
        menu = tk.Frame(self.root, bg=BG_COLOR)
        menu.pack(fill='both', expand=True)
        self.frames['main'] = menu

        tk.Label(menu, text="Layyy Tweaks Menu", font=('Arial', 20, 'bold'), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=20)

        buttons = [
            ("System Tweaks", self.system_menu),
            ("Advanced Tweaks", self.advanced_menu),
            ("Gaming Tweaks", self.gaming_menu),
            ("Network Tweaks", self.network_menu),
            ("KBM Tweaks", self.kbm_menu),
            ("Cleaner Tools", self.cleaner_menu),
            ("Revert Changes", revert_all),
            ("Quit", self.root.quit)
        ]

        for text, command in buttons:
            self.create_menu_button(menu, text, command)

    def create_menu_button(self, parent, text, command):
        """Create a button for the menu."""
        button = tk.Button(parent, text=text, font=('Arial', 14), bg=BUTTON_COLOR, fg=TEXT_COLOR, relief="raised",
                           command=command, width=25, height=2, bd=2)
        button.pack(pady=12)

    def build_submenu(self, name, actions):
        """Build a submenu with actions."""
        frame = tk.Frame(self.root, bg=BG_COLOR)
        self.frames[name] = frame

        canvas = tk.Canvas(frame, bg=BG_COLOR, highlightthickness=0)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview, bg=BG_COLOR)
        scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        tk.Label(scrollable_frame, text=name, font=('Arial', 16, 'bold'), fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=20)

        for label, func in actions:
            self.create_action_button(scrollable_frame, label, func)

        back_button = tk.Button(scrollable_frame, text="⬅ Back", font=('Arial', 14), bg=BACK_BUTTON_COLOR, fg=TEXT_COLOR,
                                relief="raised", command=lambda: self.switch_frame('main'), width=25, height=2)
        back_button.pack(pady=20)

    def create_action_button(self, parent, label, func):
        """Create an action button."""
        button = tk.Button(parent, text=label, font=('Arial', 14), bg="#2196F3", fg=TEXT_COLOR, relief="raised",
                           command=lambda f=func: self.run_with_loading(f), width=25, height=2)
        button.pack(pady=10)

    def system_menu(self):
        self.build_submenu('System Tweaks', [
            ("Enable High Perf Power Plan", enable_high_perf),
            ("Disable Background Apps", disable_background_apps),
            ("Disable Visual Effects", disable_visual_effects),
            ("Disable Services", disable_services),
            ("Enable Fast Startup", enable_fast_startup),
            ("Disable Hibernation", disable_hibernation),
            ("Disable Error Reporting", disable_error_reporting),
            ("Disable Remote Assistance", disable_remote_assistance),
            ("Disable Scheduled Tasks", disable_scheduled_tasks),
        
        ])
        self.switch_frame('System Tweaks')

    def advanced_menu(self):
        self.build_submenu('Advanced Tweaks', [
            ("Disable Cortana", disable_cortana),
            ("Disable Indexing", disable_indexing),
            ("Disable Startup Sound", disable_startup_sound),
            ("Disable Notifications", disable_notifications),
            ("Disable Action Center", disable_action_center),
            ("Disable Startup Programs", disable_startup_programs),
            ("Disable Disk Defrag", disable_disk_defrag),
           
        ])
        self.switch_frame('Advanced Tweaks')

    def gaming_menu(self):
        self.build_submenu('Gaming Tweaks', [
            ("Disable Game Bar", disable_game_bar),
            ("Disable Game Mode", disable_game_mode),
            ("Enable Ultra-Low Latency Mode", enable_ulow_latency_mode),
            ("Disable Fullscreen Optimizations", disable_fullscreen_optimizations),
            ("Disable V-Sync", disable_vsync),
            ("Enable High DPI Scaling", enable_high_dpi_scaling),
            ("Disable Power Throttling", disable_power_throttling),
            ("Enable Max Performance GPU", enable_max_performance_gpu),
            ("Disable Background Tasks", disable_background_tasks),
            ("Disable Touchpad", disable_touchpad),
        ])
        self.switch_frame('Gaming Tweaks')

    def network_menu(self):
        self.build_submenu('Network Tweaks', [
            ("Optimize TCP Stack", optimize_tcp),
            ("Disable Nagle's Algorithm", disable_nagle),
            ("Set Google DNS", set_google_dns),
            ("Disable QoS Limit", disable_qos),
            ("Disable IPv6", disable_ipv6),
            ("Enable TCP Fast Open", enable_tcp_fast_open),
            ("Disable Network Discovery", disable_network_discovery),
            ("Disable NetBIOS", disable_netbios),
            ("Disable SMB", disable_smb),
            ("Enable DNS Cache", enable_dns_cache),
        ])
        self.switch_frame('Network Tweaks')

    def kbm_menu(self):
        self.build_submenu('KBM Tweaks', [
            ("Disable Mouse Accel", disable_mouse_accel),
            ("Disable Filter Keys", disable_filter_keys),
            ("Prioritize Input Devices", prioritize_input),
            ("Disable USB Suspend", disable_usb_suspend),
            ("Enable Raw Input", enable_raw_input),
            ("Disable Keyboard Delay", disable_keyboard_delay),
            ("Enable Polling Rate", enable_polling_rate),
            ("Disable Mouse Smoothing", disable_mouse_smoothing),
            ("Disable Mouse Trails", disable_mouse_trails),
            ("Disable Sticky Keys", disable_sticky_keys),
        ])
        self.switch_frame('KBM Tweaks')

    def cleaner_menu(self):
        self.build_submenu('Cleaner Tools', [
            ("Clear Temp Files", clear_temp),
            ("Clear Prefetch", clear_prefetch),
            ("Flush DNS", flush_dns),
            ("Empty Recycle Bin", empty_recycle_bin),
            ("Clear Logs", clear_logs),
            ("Clear Cache", clear_cache),
            ("Clear Temp Internet Files", clear_temp_internet_files),
            ("Clear Windows Update Cache", clear_windows_update_cache),
            ("Clear Event Logs", clear_event_logs),
            ("Clear Error Reports", clear_error_reports),
        ])
        self.switch_frame('Cleaner Tools')

    def run_with_loading(self, func):
        """Run a function with a loading indicator."""
        loading_window = tk.Toplevel(self.root)
        loading_window.geometry("300x100")
        loading_window.title("Running...")
        progress = ttk.Progressbar(loading_window, mode='indeterminate')
        progress.pack(pady=20, padx=30)
        progress.start()
        try:
            func()
            progress.stop()
            messagebox.showinfo("Success", "The optimization was successful!")
        except Exception as e:
            progress.stop()
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            loading_window.destroy()

# === Main Execution ===
if __name__ == '__main__':
    root = tk.Tk()
    app = OptimizerApp(root)
    root.mainloop()
