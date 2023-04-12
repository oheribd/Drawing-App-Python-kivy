from typing import NewType
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse, Rectangle
from kivy.config import Config
from kivy.core.window import Window

class DrawingWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        # parent = Widget()
        # with parent.canvas:
            # pass

        with self.canvas:
            Color(1, 0.3, 0.7)
            self.player = Ellipse(pos=(0, 0), size=(50, 50))


    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_keyboard_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):

        currentx = self.player.pos[0]
        currenty = self.player.pos[1]

        if text == 'w'or keycode[1] == 'up':
            print("UP")
            currenty += 1

        elif text == 'd'or keycode[1] == 'right':
            print("RIGHT")
            currentx += 1

        elif text == 'a'or keycode[1] == 'left':
            print("LEFT")
            currentx -= 1

        elif text == 's'or keycode[1] == 'down':
            print("DOWN")
            currenty -= 1

        else:
            print("not respond")

        self.player.pos = (currentx,currenty)

    

       


class DrawingApp(App):
    def build(self):

        self.title=" **** AMAZING DRAWING APP **** "

        return DrawingWidget()

# drawing

if __name__ == '__main__':
    # set the window size
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '800')
    DrawingApp().run()
            
