import random
import threading
import time
from pynput.mouse import Button, Controller


class Clicker:
    def __init__(self):
        self.data = {}
        self.mouse = Controller()
        self.event = threading.Event()
        self.status = 'stop'
        self.main_thread = threading.Thread()

    def start(self, data):
        if self.status == 'stop' and not self.main_thread.is_alive():
            self.status = 'start'
            self.main_thread = threading.Thread(target=self.thread, args=[data])
            self.main_thread.start()

    @staticmethod
    def get_random_number(regression):
        return random.randint(regression * -1, regression) / 1000

    def thread(self, data):
        time_sleep = 0
        time_sleep += data['interval_hours'] * 60 * 60
        time_sleep += data['interval_minutes'] * 60
        time_sleep += data['interval_seconds']
        time_sleep += data['interval_milliseconds'] / 1000
        regression = data['regression_milliseconds']
        random_number_latest = None

        if time_sleep > 0:
            while self.status == 'start' and self.status != 'need_end':
                if regression == 0:
                    random_number = 0
                else:
                    random_number = self.get_random_number(regression)
                    while random_number == random_number_latest:
                        random_number = self.get_random_number(regression)
                    random_number_latest = random_number
                threading.Thread(target=self.click, args=[data]).start()
                # time.sleep(time_sleep + random_number)
                self.event.wait(time_sleep + random_number)

    def click(self, data):
        if data['option_mouse_button'] == 0:
            button = Button.left
        else:
            button = Button.right
        click_count = data['option_mouse_action'] + 1
        self.mouse.click(button, click_count)

    def stop(self):
        self.status = 'need_end'
        self.event.set()
        self.status = 'stop'
        self.event.clear()
