import win32gui
import pyautogui
import tkinter as tk

def get_mouse_position():
    # Get the current mouse position
    x, y = pyautogui.position()
    # Update the label text with mouse position
    position_label.config(text=f"    Mouse Position: X={x}, Y={y}    ")
    # Schedule the function to run again after 100 milliseconds
    root.after(100, get_mouse_position)

def get_window_info():
    window = win32gui.GetForegroundWindow()
    l, t, r, b = win32gui.GetWindowRect(window)
    window_label.config(text=f"    Window Rect: L: {l}, T: {t}, R: {r}, B: {b}, W: {r-l}, H: {b-t}    ")
    # print(f"Window LEFT: {l}, TOP: {t}, RIGHT: {r}, BOTTOM: {b}, Window WIDTH: {r-l}, Window HEIGHT: {b-t}")
    root.after(100, get_window_info)


# Create a tkinter window
root = tk.Tk()
root.title("Info Tracker")

# Create a label to display mouse position
position_label = tk.Label(root, text="Mouse Position: X:, Y:")
position_label.pack(pady=10)

# Create a label to display mouse position
window_label = tk.Label(root, text="Window Rect: L:, T:, R:, B:, W:, H:")
window_label.pack(pady=10)


# Start tracking mouse position
get_mouse_position()

# Start window tracker
get_window_info()

# Run the tkinter event loop
root.mainloop()
