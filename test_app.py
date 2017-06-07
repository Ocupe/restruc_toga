import toga


def callback(btn):
    print('in callback')


if __name__ == '__main__':
    # btn = toga.Button('My Button')
    # print(btn.label)
    # for sc in Factory.__subclasses__():
    #     print(sc.__name__)
    # f = Factory
    # print(f)
    # btn = f.create_button('My Button')
    # print(btn)
    # print(btn.label)
    # btn.label = 'Test'
    # print(btn.label)
    btn = toga.Button('My Button')
    print(btn)
    print(btn.label)
    print(btn.enabled)
    btn.enabled = False
    print(btn.enabled)

    btn2 = toga.Button('Button 2')
    print(btn2)
    print(btn2.label)
    btn2.label = 'Nice'
    btn2.on_press = callback
    print(btn2.label)
    print(btn2.on_press.__name__)
