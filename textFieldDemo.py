"""
Program: textFieldDemo.py
Chapter 8 (Page 263)
1/22/2024

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

Example of a GUI-based app that has labels, text fields for both input and output and a command button.
"""

from breezypythongui import EasyFrame
# Other imports go here

# Class header (class name will change project to project)
class TextFieldDemo(EasyFrame):

	# Definition of our classes' constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Text Field Demo", width = 280, height = 160, background = "skyblue")

		# Label and entry field for the input
		self.addLabel(text = "Input", row = 0, column = 0, background = "skyblue")
		self.inputField = self.addTextField(text = "", row = 0, column = 1)
		self.inputField["background"] = "khaki"

		# Label and entry field for the output
		self.addLabel(text = "Output", row = 1, column = 0, background = "skyblue")
		self.outputField = self.addTextField(text = "", row = 1, column = 1, state = "readonly")

		# The command button which triggers the convert() function
		self.addButton(text = "Convert", row = 2, column = 0, columnspan = 2, command = self.convert)

	# Definition of the convert() function
	def convert(self):
		""" Collects the input string, converts it to uppercase and outputs the result."""
		text = self.inputField.getText()
		result = text.upper()
		self.outputField.setText(result)

# Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	TextFieldDemo().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()