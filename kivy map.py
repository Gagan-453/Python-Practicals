from kivy_garden.mapview import MapView
from kivy.app import App

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=15, lat=13.6109084, lon= 79.4175269)
        return mapview

MapViewApp().run()