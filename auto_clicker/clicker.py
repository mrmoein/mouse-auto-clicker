import random
import threading
import time

from pynput.mouse import Button, Controller


class Clicker:
    def __init__(self):
        self.data = {}
        self.event = threading.Event()
        self.mouse = Controller()
        self.status = 'stop'

    def start(self, data):
        if self.status == 'stop':
            self.status = 'start'
            threading.Thread(target=self.thread, args=(data,)).start()

    def thread(self, data):
        time_sleep = 0
        time_sleep += data['interval_hours'] * 60 * 60
        time_sleep += data['interval_minutes'] * 60
        time_sleep += data['interval_seconds']
        time_sleep += data['interval_milliseconds'] / 1000
        regression = data['regression_milliseconds']

        if time_sleep > 0:
            while not self.event.is_set():
                random_r = 0 if not regression else random.randint(regression * -1, regression) / 1000
                self.click(data)
                self.event.wait(time_sleep + random_r)
        self.status = 'stop'
        self.event.clear()

    def click(self, data):
        if data['option_mouse_button'] == 0:
            button = Button.left
        else:
            button = Button.right
        click_count = data['option_mouse_action'] + 1
        self.mouse.click(button, click_count)

    def stop(self):
        self.event.set()

    def create_event(self):
        self.event = threading.Event()
