from infi.systray import SysTrayIcon
import keyboard


def activate(systray):
    for i in range(150):
        keyboard.block_key(i)


def desactivate(systray):
    keyboard.unhook_all()

menu_options = (("Cleaning Keyboard: True", "circle-check-solid.ico", activate), ("Cleaning Keyboard: False", "circle-check-regular.ico", desactivate),)
systray = SysTrayIcon("keyboard-solid.ico", "Keyboard Cleaner", menu_options)
systray.start()


#  IT'S WORKING!!!