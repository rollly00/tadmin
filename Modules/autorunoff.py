import winreg
def remove_from_startup():
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
	winreg.DeleteValue(key, "RMS")
	winreg.CloseKey(key)