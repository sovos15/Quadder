import pyautogui
import keyboard
import time
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
import win32gui
import win32con
import win32api  # Importing for transparency handling

# Configurations
DELAY = 0.1  # Delay to prevent accidental fast presses
DOUBLE_CLICK_WINDOW = 0.3  # Max time between two clicks to register as double-click
GRID_COLOR = (0, 255, 0)  # Green color for grid and numbers (BGR format)

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Initialize the region (start with the whole screen)
current_region = [0, 0, screen_width, screen_height]  # [x1, y1, x2, y2]
last_click_time = 0  # Track time of the last click for double-click detection
holding = False  # Track if a click-and-hold operation is ongoing

def divide_region(region, num):
    """Divide the region into a 3x3 grid according to the numpad layout."""
    x1, y1, x2, y2 = region
    width = (x2 - x1) / 3
    height = (y2 - y1) / 3

    # Adjust row and column based on numpad layout (789 -> 123 from top to bottom)
    row = 2 - (num - 1) // 3  # Reversing row order
    col = (num - 1) % 3

    new_x1 = int(x1 + col * width)
    new_y1 = int(y1 + row * height)
    new_x2 = int(new_x1 + width)
    new_y2 = int(new_y1 + height)

    return [new_x1, new_y1, new_x2, new_y2]

def move_cursor_to_center(region):
    """Move the cursor to the center of the given region."""
    x1, y1, x2, y2 = region
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    pyautogui.moveTo(center_x, center_y)

def handle_click(button='left'):
    """Simulate a mouse click and reset the grid."""
    global last_click_time, holding, current_region

    current_time = time.time()
    if current_time - last_click_time <= DOUBLE_CLICK_WINDOW:
        pyautogui.doubleClick(button=button)
    else:
        pyautogui.click(button=button)
    last_click_time = current_time

    reset_region()  # Reset to the full screen region

def release_click(button='left'):
    """Release the mouse button (for drag-and-drop)."""
    global holding
    pyautogui.mouseUp(button=button)
    holding = False

def handle_scroll(direction):
    """Scroll up or down."""
    pyautogui.scroll(1 if direction == 'up' else -1)

def reset_region():
    """Reset the region to the full screen."""
    global current_region
    current_region = [0, 0, screen_width, screen_height]

def draw_overlay(region):
    """Draw the 3x3 grid as a transparent overlay."""
    x1, y1, x2, y2 = region
    width = (x2 - x1) // 3
    height = (y2 - y1) // 3

    # Create a transparent image
    overlay = Image.new('RGBA', (screen_width, screen_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Draw the grid lines
    for i in range(1, 3):
        draw.line([(x1 + i * width, y1), (x1 + i * width, y2)], fill=GRID_COLOR, width=2)
        draw.line([(x1, y1 + i * height), (x2, y1 + i * height)], fill=GRID_COLOR, width=2)

    # Draw numbers (1-9) according to the numpad layout
    font = ImageFont.truetype("arial.ttf", 32)
    layout = [7, 8, 9, 4, 5, 6, 1, 2, 3]  # Numpad layout order

    for i in range(3):
        for j in range(3):
            num = layout[i * 3 + j]
            text_x = x1 + j * width + width // 2 - 10
            text_y = y1 + i * height + height // 2 - 20
            draw.text((text_x, text_y), str(num), font=font, fill=GRID_COLOR)

    # Convert to OpenCV format and display the overlay
    overlay = np.array(overlay)
    overlay = cv2.cvtColor(overlay, cv2.COLOR_RGBA2BGRA)
    
    # Ensure the window starts in fullscreen and has no borders
    cv2.namedWindow("Overlay", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Overlay", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    # Move the window to (0, 0) to make sure it is not anchored to the center
    hwnd = win32gui.FindWindow(None, "Overlay")
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, screen_width, screen_height, 0)
    
    cv2.imshow("Overlay", overlay)
    cv2.waitKey(1)  # Refresh the window

def make_window_transparent(hwnd):
    """Make the OpenCV window transparent."""
    extended_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, extended_style | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 0, win32con.LWA_COLORKEY)

def run():
    """Main loop to listen for numpad key presses and perform actions."""
    global current_region, holding

    print("Numpad mouse program running. Press 'Esc' to quit.")
    
    while True:
        hwnd = win32gui.FindWindow(None, "Overlay")
        if hwnd:
            make_window_transparent(hwnd)

        draw_overlay(current_region)  # Draw the current grid

        for num in range(1, 10):
            if keyboard.is_pressed(str(num)):
                current_region = divide_region(current_region, num)
                move_cursor_to_center(current_region)
                time.sleep(DELAY)

        if keyboard.is_pressed('0'):
            handle_click('left')
            time.sleep(DELAY)

        if keyboard.is_pressed('.'):
            handle_click('right')
            time.sleep(DELAY)

        if keyboard.is_pressed('*'):
            handle_click('middle')
            time.sleep(DELAY)

        if keyboard.is_pressed('+'):
            handle_scroll('up')
            time.sleep(DELAY)

        if keyboard.is_pressed('-'):
            handle_scroll('down')
            time.sleep(DELAY)

        if keyboard.is_pressed('esc'):
            print("Exiting.")
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
