import winreg

def get_windows_theme_mode():
    try:
        Registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        reg_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
        key = winreg.OpenKey(Registry, reg_path)
        value = winreg.QueryValueEx(key, 'AppsUseLightTheme')[0]
        if value == 1:
            return "light"
        return "dark"
    except Exception as e:
        print(f"获取Windows主题模式出错: {e}")
        return None

if __name__ == "__main__":
    print(get_windows_theme_mode())
