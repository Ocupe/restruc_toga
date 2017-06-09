import toga
from colosseum import CSS

# Todo implement toga.box in a correct way
def callback(btn):
    print('in callback')

def build(app):
    box = toga.Box(style=CSS(flex=1, margin=20))
    btn = toga.Button('My Button', on_press=callback)
    return btn

if __name__ == '__main__':
    # window = toga.Window()
    app = toga.App('My App', 'ocupe.org.app', startup=build)
    app.main_loop()


    # btn = toga.Button('My Button')
    # print(btn)
    # print(btn.label)
    # print(btn.enabled)
    # btn.enabled = False
    # print(btn.enabled)
    #
    # btn2 = toga.Button('Button 2')
    # print(btn2)
    # print(btn2.label)
    # btn2.label = 'Nice'
    # btn2.on_press = callback
    # print(btn2.label)
    # print(btn2.on_press.__name__)
