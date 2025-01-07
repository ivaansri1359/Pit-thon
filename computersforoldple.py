import tkinter as tk
import webbrowser

# Create the main window
root = tk.Tk()
root.title("Easy Control Panel")
root.geometry("800x600")

# Create a label
label = tk.Label(root, text="Hello World!", font=("Monospace", 24))
label.pack(pady=10)



# Function to create the web control panel
def on_button_click_Web():
    # Create a new window using Toplevel
    web_root = tk.Toplevel(root)
    web_root.title("Easy Control Panel - Web")
    web_root.geometry("800x600")

    # Button to open Google
    def on_button_click_google():
        webbrowser.open("https://www.google.com")

    google_button = tk.Button(web_root, text="Google", command=on_button_click_google)
    google_button.pack(pady=10)

    # Button to open Google Classroom
    def on_button_click_classroom():
        webbrowser.open("https://www.classroom.google.com")

    classroom_button = tk.Button(web_root, text="Classroom", command=on_button_click_classroom)
    classroom_button.pack(pady=10)

    # Button to open Gmail
    def on_button_click_email():
        webbrowser.open("https://www.gmail.com")

    email_button = tk.Button(web_root, text="E-mail", command=on_button_click_email)
    email_button.pack(pady=10)

# Main button to open the web control panel
web_button = tk.Button(root, text="Web", command=on_button_click_Web)
web_button.pack(pady=10)





# Function to create the web control panel
def on_button_click_Apps():
    # Create a new window using Toplevel
    web_root = tk.Toplevel(root)
    web_root.title("Easy Control Panel - Apps")
    web_root.geometry("800x600")

    # Button to open Notepad
    def on_button_click_notepad():
        webbrowser.open("notepad.exe")
    
    notepad_button = tk.Button(web_root, text="Notepad", command=on_button_click_notepad)
    notepad_button.pack(pady=10)

    # Button to open Calculator
    def on_button_click_calculator():
        webbrowser.open("calc.exe")

    calculator_button = tk.Button(web_root, text="Calculator", command=on_button_click_calculator)
    calculator_button.pack(pady=10)

    # Button to open Paint
    def on_button_click_paint():
        webbrowser.open("mspaint.exe")

    paint_button = tk.Button(web_root, text="Paint", command=on_button_click_paint)
    paint_button.pack(pady=10)

    # Button to open Command Prompt
    def on_button_click_cmd():
        webbrowser.open("cmd.exe")

    cmd_button = tk.Button(web_root, text="Command Prompt", command=on_button_click_cmd)
    cmd_button.pack(pady=10)

    # Button to open File Explorer
    def on_button_click_explorer():
        webbrowser.open("explorer.exe")

    explorer_button = tk.Button(web_root, text="File Explorer", command=on_button_click_explorer)
    explorer_button.pack(pady=10)

    # Button to open Task Manager
    def on_button_click_taskmgr():
        webbrowser.open("taskmgr.exe")

    taskmgr_button = tk.Button(web_root, text="Task Manager", command=on_button_click_taskmgr)
    taskmgr_button.pack(pady=10)

    # Button to open Control Panel
    def on_button_click_control_panel():
        webbrowser.open("control.exe")

    control_panel_button = tk.Button(web_root, text="Control Panel", command=on_button_click_control_panel)
    control_panel_button.pack(pady=10)

    # Button to open System Information
    def on_button_click_sysinfo():
        webbrowser.open("msinfo32.exe")

    sysinfo_button = tk.Button(web_root, text="System Information", command=on_button_click_sysinfo)
    sysinfo_button.pack(pady=10)

    # Button to open Device Manager
    def on_button_click_devicemgr():
        webbrowser.open("devmgmt.msc")

    devicemgr_button = tk.Button(web_root, text="Device Manager", command=on_button_click_devicemgr)
    devicemgr_button.pack(pady=10)

    # Button to open Disk Management
    def on_button_click_diskmgmt():
        webbrowser.open("diskmgmt.msc")

    diskmgmt_button = tk.Button(web_root, text="Disk Management", command=on_button_click_diskmgmt)
    diskmgmt_button.pack(pady=10)

    # Button to open Event Viewer
    def on_button_click_eventvwr():
        webbrowser.open("eventvwr.msc")

    eventvwr_button = tk.Button(web_root, text="Event Viewer", command=on_button_click_eventvwr)
    eventvwr_button.pack(pady=10)

    # Button to open Services
    def on_button_click_services():
        webbrowser.open("services.msc")

    services_button = tk.Button(web_root, text="Services", command=on_button_click_services)
    services_button.pack(pady=10)

    # Button to open More Apps
    def on_button_click_more_apps():
        more_apps_root = tk.Toplevel(root)
        more_apps_root.title("Easy Control Panel - More Apps")
        more_apps_root.geometry("800x600")
        
        # Button to open Registry Editor
        def on_button_click_regedit():
            webbrowser.open("regedit.exe")

        regedit_button = tk.Button(web_root, text="Registry Editor", command=on_button_click_regedit)
        regedit_button.pack(pady=10)

        # Button to open Snipping Tool
        def on_button_click_snipping_tool():
            webbrowser.open("snippingtool.exe")

        snipping_tool_button = tk.Button(more_apps_root, text="Snipping Tool", command=on_button_click_snipping_tool)
        snipping_tool_button.pack(pady=10)

        # Button to open Sticky Notes
        def on_button_click_sticky_notes():
            webbrowser.open("stikynot.exe")

        sticky_notes_button = tk.Button(more_apps_root, text="Sticky Notes", command=on_button_click_sticky_notes)
        sticky_notes_button.pack(pady=10)

        # Button to open Windows Media Player
        def on_button_click_media_player():
            webbrowser.open("wmplayer.exe")

        media_player_button = tk.Button(more_apps_root, text="Windows Media Player", command=on_button_click_media_player)
        media_player_button.pack(pady=10)

    

        # Button to open PowerShell
        def on_button_click_powershell():
            webbrowser.open("powershell.exe")

        powershell_button = tk.Button(web_root, text="PowerShell", command=on_button_click_powershell)
        powershell_button.pack(pady=10)

        # Button to open Windows Update
        def on_button_click_windows_update():
            webbrowser.open("ms-settings:windowsupdate")

        windows_update_button = tk.Button(web_root, text="Windows Update", command=on_button_click_windows_update)
        windows_update_button.pack(pady=10)

        # Button to open Network Connections
        def on_button_click_network_connections():
            webbrowser.open("ncpa.cpl")

        network_connections_button = tk.Button(web_root, text="Network Connections", command=on_button_click_network_connections)
        network_connections_button.pack(pady=10)

        # Button to open Bluetooth Settings
        def on_button_click_bluetooth():
            webbrowser.open("ms-settings:bluetooth")

        bluetooth_button = tk.Button(web_root, text="Bluetooth Settings", command=on_button_click_bluetooth)
        bluetooth_button.pack(pady=10)

    more_apps_button = tk.Button(web_root, text="More Apps", command=on_button_click_more_apps)
    more_apps_button.pack(pady=10)

    # Function to create the web control panel
def on_button_click_Web():
    # Create a new window using Toplevel
    web_root = tk.Toplevel(root)
    web_root.title("Easy Control Panel - Web")
    web_root.geometry("800x600")

    # Button to open Google
    def on_button_click_google():
        webbrowser.open("https://www.google.com")

    google_button = tk.Button(web_root, text="Google", command=on_button_click_google)
    google_button.pack(pady=10)

    # Button to open Google Classroom
    def on_button_click_classroom():
        webbrowser.open("https://www.classroom.google.com")

    classroom_button = tk.Button(web_root, text="Classroom", command=on_button_click_classroom)
    classroom_button.pack(pady=10)

    # Button to open Gmail
    def on_button_click_email():
        webbrowser.open("https://www.gmail.com")

    email_button = tk.Button(web_root, text="E-mail", command=on_button_click_email)
    email_button.pack(pady=10)









# Main button to open the web control panel
web_button = tk.Button(root, text="Apps", command=on_button_click_Apps)
web_button.pack(pady=10)

# Run the application
root.mainloop()
