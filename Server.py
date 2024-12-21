import subprocess
import time


def start_appium_server(port=4723):
    command = f'start cmd /k appium --use-plugins=relaxed-caps -p {port}'
    subprocess.Popen(command, shell=True)
    time.sleep(5)


if __name__ == "__main__":
    start_appium_server()
    try:
        print("Appium server started in a new command window. Running tests...")
        time.sleep(10)
    finally:
        print("You can manually stop the Appium server from the command window.")