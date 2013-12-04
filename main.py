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


class RootWidget(FloatLayout):
    pass


class Testi18nApp(App):

    def build(self):
        pass


if __name__ == '__main__':
    Testi18nApp().run()