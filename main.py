__version__ = '1.0'
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from flufl.i18n import registry, PackageStrategy, initialize
import translations.messages
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class RootWidget(FloatLayout):
    pass


class Buttons(BoxLayout):
    pass


class Testi18nApp(App):
    _ = ObjectProperty(None, allownone=True)

    def build(self):
        strategy = PackageStrategy('test', translations.messages) 
        application = registry.register(strategy)
        self._ = application._
        self.set_language('fr')

    def set_language(self, language_code):
        self._.push(language_code)
        _ = self._
        self._ = None
        self._ = _


if __name__ == '__main__':
    Testi18nApp().run()