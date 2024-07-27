import subprocess

def get_current_activity():
    try:
        result = subprocess.run(['adb', 'shell', 'dumpsys', 'window', 'windows'], capture_output=True, text=True)
        output = result.stdout
        for line in output.splitlines():
            if 'mCurrentFocus' in line or 'mFocusedApp' in line:
                print(line)
    except Exception as e:
        print(f"Error: {e}")

get_current_activity()
