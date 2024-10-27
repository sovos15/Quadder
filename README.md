🖱️ Quadder Mouse Replacement System ⌨️
a keyboard-driven mouse replacement system, ideal for users who prefer or need to navigate their computer without a traditional mouse. The program uses a numpad to divide the screen into regions for precise cursor placement by "adressing", supports left, right, and middle* clicks, WIP drag-and-drop, scrolling, etc

Planned Features ✨
Precise Mouse Control: Navigate the screen with recursive grid divisions using numpad keys.
Primary, Secondary, and Middle Clicks: Click with keys 0, ., and *.
Drag-and-Drop: Supports click-and-hold operations for drag-and-drop functionality.
Smooth Scrolling: Use + and - on the numpad for scrolling up and down.
Visual Feedback: Transparent, fullscreen grid overlay with numbered regions.
Accessible Design: Works across various operating systems (Windows, Linux, macOS) with minimal dependencies.*

git pull
pip install pyautogui opencv-python keyboard numpy pillow pywin32 pynput
python quadder.py

Numpad Layout 🎛
The numpad keys are mapped to divide the screen into a 3x3 grid, allowing recursive zooming for precise cursor control at intuitive adresses
0: Primary Click
.: Secondary Click
*: Middle Click
+: Scroll Up
-: Scroll Down

Usage 📋
When you open the Program A transparent grid overlay will appear.
Select a region by pressing a numpad key (1-9) to zoom into that section of the screen.
Select a sub region the same way
when you click the grid should reset so you can click something else.

Troubleshooting 🐛
Using esc to close the program isn't working so just close the terminal to close the program.
Otherwise FIY

Contributing 🤝
Feel free to fork this repository, submit pull requests, or open issues if you encounter any bugs or have feature suggestions!

Acknowledgements 🙌
Special thanks to the OpenCV, Pillow, and PyAutoGUI teams for providing the tools to make this project possible.

Plans:
drag and drop should work by allowing you to hold a click and enter another adress before releasing.
double click is fairly intuitive.


Author 👨‍💻
Designed by sovos
Coded by ChatGPT 4o
Reach out to ChatGPT for help.

Share and Enjoy! 🖱️🚀
