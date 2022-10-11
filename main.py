from kivy.config import Config

Config.set("graphics", "resizable", False)
from time import strftime
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window

Window.size = (400, 400)


class MyApp(App):
    stopwatch_started = False
    stopwatch_seconds = 0
    countdown_started = False
    countdown_seconds = 0
    countdown_hora = 0
    countdown_sec = 0
    countdown_minutes = 0
    countdown_paused = False
    hrs24 = [str(i) for i in range(0, 24)]
    minut60 = [str(i) for i in range(0, 61)]
    sec60 = [str(i) for i in range(0, 61)]

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self, tick):
        # Main Clock
        self.root.ids.clocktime.text = strftime("%H:%M:%S")
        self.root.ids.clockday.text = strftime("%m/%d/%Y")
        #-------------Countdown Setup--------------#
        # START: Started (True) + Paused (False)
        # PAUSE: Started (True) + Paused (True)
        # RESET: Started (False) + Paused (False)
        if self.countdown_started:
            self.countdown_paused = False
            self.root.ids.countdown_minutos.values = []
            self.root.ids.countdown_segundos.values = []
            self.root.ids.countdown_horas.values = []
            self.root.ids.countdown_minutos.font_size = 0
            self.root.ids.countdown_segundos.font_size = 0
            self.root.ids.countdown_horas.font_size = 0
            if self.countdown_seconds > 0:
                self.countdown_seconds -= tick
            if self.countdown_seconds <= 0:
                self.countdown_started = False
                self.root.ids.countdown_start_stop.text = "Start"
        
        if not self.countdown_started:
            if not self.countdown_paused:
                self.root.ids.countdown_minutos.font_size = 20
                self.root.ids.countdown_segundos.font_size = 20
                self.root.ids.countdown_horas.font_size = 20
                self.root.ids.countdown_minutos.values = self.minut60
                self.root.ids.countdown_segundos.values = self.sec60
                self.root.ids.countdown_horas.values = self.hrs24
                
        if self.stopwatch_started:
            self.stopwatch_seconds += tick

        a, b = divmod(self.stopwatch_seconds, 60)
        m, s = divmod(self.countdown_seconds, 60)

        self.root.ids.stopwatch_counter.text = ("%02d:%02d:%02d" % (int(a), int(b), int(b * 100 % 100)))
        self.root.ids.countdown_counter.text = ("%02d:%02d:%02d" % (int(m / 60), int(m % 60), int(s)))

    def stopwatch_stop_start(self):
        self.root.ids.stopwatch_start_stop.text = "Start" if self.stopwatch_started else 'Stop'
        self.stopwatch_started = not self.stopwatch_started

    def stopwatch_reset(self):
        self.root.ids.stopwatch_start_stop.text = 'Start'
        self.stopwatch_started = False
        self.stopwatch_seconds = 0

    def countdown_minutos_clicked(self, value):
        if self.countdown_started:
            self.countdown_started = False
            self.countdown_paused = True
        self.countdown_minutes = int(value)
        self.root.ids.countdown_start_stop.text = "Start"

    def countdown_segundos_clicked(self, value):
        if self.countdown_started:
            self.countdown_started = False
            self.countdown_paused = True
        self.countdown_sec = int(value)
        self.root.ids.countdown_start_stop.text = "Start"

    def countdown_horas_clicked(self, value):
        if self.countdown_started:
            self.countdown_started = False
            self.countdown_paused = True
        self.countdown_hora = int(value)
        self.root.ids.countdown_start_stop.text = "Start"

    def countdown_stop_start(self):
        if not self.countdown_started and not self.countdown_paused:
            self.countdown_seconds = self.countdown_minutes * 60 + self.countdown_sec + self.countdown_hora * 3600
        self.root.ids.countdown_start_stop.text = "Start" if self.countdown_started else 'Stop'
        self.countdown_started = not self.countdown_started
        self.countdown_paused = True

    def countdown_reset(self):
        self.root.ids.countdown_start_stop.text = 'Start'
        self.countdown_started = False
        self.countdown_paused = False
        self.root.ids.countdown_minutos.text = "0"
        self.root.ids.countdown_segundos.text = "0"
        self.root.ids.countdown_horas.text = "0"
        self.countdown_sec = 0
        self.countdown_hora = 0
        self.countdown_minutes = 0
        self.countdown_seconds = 0


if __name__ == "__main__":
    MyApp().run()
            
