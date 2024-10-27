# 🖱️ Quadder Mouse Replacement System ⌨️ 
A keyboard-driven mouse replacement system ideal for users who prefer or need to navigate their computer without a traditional mouse.
  - The program uses a numpad to divide the screen into regions for precise cursor placement by "adressing", supports left, right, and middle* clicks, WIP drag-and-drop, scrolling, etc

### ✨ Precise Mouse Control:
- Navigate the screen with recursive grid divisions using numpad keys.
- Primary, Secondary, and Middle Clicks
- Drag-and-Drop (broken)
- Use + and - on the numpad for scrolling up and down. (untested)
- semitransparent, fullscreen grid overlay with numbered regions.
- Should work across various operating systems (Windows, Linux, macOS) with minimal dependencies.

Install:

	git pull 
	pip install pyautogui opencv-python keyboard numpy pillow pywin32 pynput 
	python quadder.py

Numpad Layout 🎛 The numpad keys are mapped to divide the screen into a 3x3 grid, allowing recursive zooming for precise cursor control at intuitive adresses:
-	0: Primary Click 
-	.: Secondary Click
-	*: Middle Click
-	+: Scroll Up
-	-: Scroll Down

Usage 📋 
-	When you open the program a transparent grid overlay should appear.
-	Select a region by pressing the asociated numpad key select that box of the grid.
-	Select sub regions the same way.
-	I find 1-3 digits will adress most things. 
-	When you use a click the grid should reset so you can click something else.
-	If you held the click (not implemented) it should allow you to select another adress to release it at.
-	Double click is also not yet implemented.

Troubleshooting 🐛 
-	Using esc to close the program isn't working so just close the terminal to close the program.
-	Otherwise FIY

Contributing 🤝
-	Feel free to fork this repository, submit pull requests, or open issues if you encounter any bugs or have feature suggestions!

Acknowledgements🙌 
-	Special thanks to the OpenCV, Pillow, and PyAutoGUI teams for providing the tools to make this project possible.

Plans 🎛
-	drag and drop 
-	double click

Author 👨‍💻 
-	Designed by sovos 
-	Coded by ChatGPT 4o 
-	Reach out to ChatGPT or your local LLM for any help.

Share and Enjoy! 🖱️🚀
