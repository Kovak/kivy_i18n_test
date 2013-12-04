__version__ = '1.0'
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from flufl.i18n import initialize
import os
from flufl.i18n import registry, SimpleStrategy
strategy = SimpleStrategy('test')
strategy._messages_dir = os.path.dirname(__file__) + '/messages'
application = registry.register(strategy)
_ = application._
_.push('fr')
print _.code, 'current language'
print strategy._messages_dir
with _.using('fr'):
    print _('English')


class RootWidget(FloatLayout):
    pass


class Testi18nApp(App):

    def build(self):
        pass


if __name__ == '__main__':
    Testi18nApp().run()