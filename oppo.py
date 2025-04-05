import os
import tkinter as tk
from tkinter import messagebox

# Function to check ADB connection
def check_adb():
    devices = os.popen("adb devices").read()
    if "device" in devices:
        messagebox.showinfo("Status", "Phone Connected ✅")
    else:
        messagebox.showerror("Status", "No Device Found ❌")

# Function to control volume
def volume_up():
    os.system("adb shell input keyevent 24")

def volume_down():
    os.system("adb shell input keyevent 25")

def mute():
    os.system("adb shell input keyevent 164")

# Function to check battery percentage
def check_battery():
    battery = os.popen("adb shell dumpsys battery | findstr level").read()
    messagebox.showinfo("Battery Status", f"🔋 {battery.strip()}%")

# Function to toggle WiFi
def wifi_on():
    os.system("adb shell svc wifi enable")

def wifi_off():
    os.system("adb shell svc wifi disable")

# Function to toggle Bluetooth
def bluetooth_on():
    os.system("adb shell svc bluetooth enable")

def bluetooth_off():
    os.system("adb shell svc bluetooth disable")

# Function to take a screenshot
def take_screenshot():
    os.system("adb shell screencap -p /sdcard/screenshot.png")
    os.system("adb pull /sdcard/screenshot.png .")
    messagebox.showinfo("Screenshot", "📸 Screenshot Saved!")

# Function to make a call
def make_call():
    number = number_entry.get()
    if number:
        os.system(f"adb shell am start -a android.intent.action.CALL -d tel:{number}")
        messagebox.showinfo("Calling", f"📞 Calling {number}...")
    else:
        messagebox.showwarning("Error", "Please enter a phone number!")

# GUI Setup
root = tk.Tk()
root.title("📱 Phone Controller from PC")
root.geometry("300x500")

# Buttons
tk.Button(root, text="🔍 Check ADB Connection", command=check_adb).pack(pady=5)
tk.Button(root, text="🔊 Volume Up", command=volume_up).pack(pady=5)
tk.Button(root, text="🔉 Volume Down", command=volume_down).pack(pady=5)
tk.Button(root, text="🔇 Mute", command=mute).pack(pady=5)
tk.Button(root, text="🔋 Check Battery", command=check_battery).pack(pady=5)
tk.Button(root, text="📶 WiFi ON", command=wifi_on).pack(pady=5)
tk.Button(root, text="📴 WiFi OFF", command=wifi_off).pack(pady=5)
tk.Button(root, text="📡 Bluetooth ON", command=bluetooth_on).pack(pady=5)
tk.Button(root, text="❌ Bluetooth OFF", command=bluetooth_off).pack(pady=5)
tk.Button(root, text="📸 Take Screenshot", command=take_screenshot).pack(pady=5)


# Call Feature
tk.Label(root, text="📞 Enter Number:").pack(pady=5)
number_entry = tk.Entry(root)
number_entry.pack(pady=5)
tk.Button(root, text="📲 Make Call", command=make_call).pack(pady=5)

root.mainloop()
