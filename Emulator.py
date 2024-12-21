import subprocess
import time
import os


def start_emulator(emulator_name, sdk_path):
    command = f'start cmd /k "{sdk_path}\\emulator\\emulator.exe" -avd {emulator_name} -no-snapshot-load -gpu host'
    subprocess.Popen(command, shell=True)
    time.sleep(30)


def wait_for_emulator_to_load():
    print("Waiting for the emulator to boot...")
    while True:
        result = subprocess.run(['adb', 'shell', 'getprop', 'sys.boot_completed'], capture_output=True, text=True)
        if result.stdout.strip() == '1':
            print("Boot completed. Checking for home screen...")
            break
        time.sleep(5)

    while True:
        # Check if the launcher is running
        result = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], capture_output=True, text=True)
        if 'com.google.android.apps.nexuslauncher' in result.stdout:
            print("Home screen is displayed.")
            break
        time.sleep(5)  # Check every 5 seconds


if __name__ == "__main__":
    emulator_name = "Mobile_33"
    sdk_path = "D:\\Android"
    print(f"Starting emulator: {emulator_name}")
    start_emulator(emulator_name, sdk_path)
    wait_for_emulator_to_load()
    try:
        # Your test code goes here
        print("Emulator started in a new command window. Running tests...")
        time.sleep(10)  # Simulate running tests for 10 seconds
    finally:
        print("You can manually stop the emulator from the command window.")