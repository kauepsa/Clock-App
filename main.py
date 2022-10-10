from kivy.config import Config

Config.set("graphics", "resizable", True)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from datetime import datetime
import csv

Window.size = (800, 538)
Window.minimum_width, Window.minimum_height = (800, 360)

Builder.load_file('main.kv')

# Variables Setup 
widgets = [] # list of actual widgets
widget_id = 0 # id generator for widgets , unique and don't repeat after delete
actual_widget = [] # list of the actual widget values
widgets_id = [] # list of the widgets ids
widgets_count = 0 # count of the ammount of widgets

# Load from csv file when open.
def load_widgets():
    with open('savedtasks.csv') as file:
        arquive = csv.DictReader(file)
        for i in arquive:
            widgets.append(i)
            
# Save to csv file when closed.
def save_widgets():
    with open('savedtasks.csv', 'w', newline='') as file:
        arquive = csv.writer(file)
        arquive.writerow(['ID', 'NAME', 'DAYS', 'HOUR', 'MINUTE', 'STATE'])
        for i in widgets:
            arquive.writerow(i.values())
