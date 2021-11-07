import pyglet

vidPath = 'Need_for_Speed.mp4'
window = pyglet.window.Window(1280, 720)
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)

player.queue(MediaLoad)
player.play()


@window.event
def on_draw():
    window.clear()
    if player.source and player.source.video_format:
        player.get_texture().blit(0, 0)


pyglet.app.run()

# speed_car_highway = 225
# speed_car_rural = 175
#
# time_highway = 150 / speed_car_highway
# time_rural = 100 / speed_car_rural

try:
    bet = int(input('Сделайте ставку, выберите маршрут 1 или 2: '))
except (ValueError, EOFError):
    print('Ошибка! Выберите маршрут 1 или 2')
else:
    try:
        with open('result.txt', encoding='utf-8') as file:
            contain = file.readlines()
    except:
        print('File error')

    else:
        if bet == 1:
            for i in range(1, 18):
                print(contain[i].rstrip('\n'))
        elif bet == 2:
            for i in range(19, 30):
                print(contain[i].rstrip('\n'))
        else:
            print('Ошибка! Выберите маршрут 1 или 2')
