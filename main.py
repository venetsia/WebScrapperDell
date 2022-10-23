# This is a sample Python script.
import requests
from win10toast_click import ToastNotifier
import webbrowser
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_time():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    return current_time

def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    response = requests.get("https://www.dell.com/en-uk/search/nawm17r5a08sc")
    outcome = response.text.find('<div class="ps-stock-level-wrapper blk-border ">Temporarily out of stock</div>')
    current_time = get_time()
    if outcome == -1:
        toast = ToastNotifier()
        toast.show_toast("Laptop is available", "Click to open link to product", callback_on_click=your_callback_function)
        print(f"Laptop is available: {current_time}")
    else:
        toast = ToastNotifier()
        toast.show_toast("Laptop is still unavailable", "Check just in case maybe?",
                         callback_on_click=your_callback_function)
        print(f"Laptop is unavailable: {current_time}")


def your_callback_function():
    webbrowser.open('https://www.dell.com/en-uk/search/nawm17r5a08sc')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
    scheduler = BlockingScheduler()
    scheduler.add_job(print_hi, 'interval', hours=1, name="Track DELL Alienware laptop")
    scheduler.start()

