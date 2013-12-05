__version__ = '1.0'
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from flufl.i18n import initialize
import os
from flufl.i18n import registry, PackageStrategy
import translations.messages
strategy = PackageStrategy('test', translations.messages) 
application = registry.register(strategy)
_ = application._
_.push('fr')
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class RootWidget(FloatLayout):
    app = ObjectProperty(None)
    layout = ObjectProperty(None, allownone=True)

    def set_english(self):
    	_.pop()
    	self.reload_layout()

    def reload_layout(self):
    	self.remove_widget(self.layout)
    	self.layout = None
    	self.layout = Buttons()
    	self.add_widget(self.layout)

    def set_french(self):
    	_.push('fr')
    	self.reload_layout()


class Buttons(BoxLayout):
	pass

class Testi18nApp(App):

    def build(self):
        pass


if __name__ == '__main__':
    Testi18nApp().run()