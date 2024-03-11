import pyautogui
import tkinter as tk

def get_mouse_position():
    # Get the current mouse position
    x, y = pyautogui.position()
    # Update the label text with mouse position
    position_label.config(text=f"Mouse Position: X={x}, Y={y}")
    # Schedule the function to run again after 100 milliseconds
    root.after(100, get_mouse_position)

# Create a tkinter window
root = tk.Tk()
root.title("Mouse Position Tracker")

# Create a label to display mouse position
position_label = tk.Label(root, text="Mouse Position: X=, Y=")
position_label.pack(pady=10)

# Start tracking mouse position
get_mouse_position()

# Run the tkinter event loop
root.mainloop()
