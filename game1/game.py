import math
import random
import tkinter as tk
import winsound
from os import walk

class Game(tk.Tk):
    bubbles_count = 6
    pop_radius = 100

    width = 0
    height = 0

    def __init__(self):
        super().__init__()
        self.bg = tk.PhotoImage(file='images\\background.png')
        self.width = Game.width = self.winfo_screenwidth() - 10
        self.height = Game.height = self.winfo_screenheight() - 70
        self.ca = tk.Canvas(width=self.width, height=self.height)
        self.ca.pack()
        self.ca.update()

        self.beep_duration = 90
        self.ca.create_image(self.width / 2, self.height / 2, image=self.bg)
        self.bubbles = []
        self.plane = {}
        self.stats = {}
        self.stat_text_ids = {}
        self.story_visible = False
        self.story_ids = []
        self.bomb = {}
        self.launched_bombs = 0
        self.popped_bubbles = 0
        self.sprites = self.load_sprites()

        for i in range(Game.bubbles_count + 1):
            self.stats[i] = 0
            self.stat_text_ids[i] = self.ca.create_text(40, Game.height - i * 30 - 50, text=f"{i} : 0", font="arial 20", fill="navy")

        SpriteBase(self.ca, Game.width / 2, Game.height - 50, self.sprites["pane"], 0, 0, 0, 0, None)
        self.score_id = self.ca.create_text(Game.width / 2, Game.height - 40, text="0.0%", font="arial 30")
        self.story()

        self.add_plane()
        self.ca.bind("<1>", self.mouse_press)
        self.ca.after(500, self.game_loop)

    def game_loop(self):
        if len(self.bubbles) < Game.bubbles_count:
            self.add_bubble()
        if not self.plane:
            self.add_plane()
        self.ca.after(1000, self.game_loop)

    def mouse_press(self, event):
        if self.story_visible:
            self.hide_story()
        if self.plane and self.plane.is_live:
            if self.plane.has_bomb:
                self.launch_plane_bomb()
                winsound.Beep(100, self.beep_duration)
            elif self.bomb and self.bomb.is_live:
                self.bomb.is_live = False
                DetonationSprite(self.ca, self.bomb.x, self.bomb.y, self.sprites["expl"], 90, 0, 0, 0,
                                 self.sprite_event)

                # ocekovat, ci nevybuchli bubliny
                todel = []
                any_pop = False
                for bub in self.bubbles:
                    dist = math.sqrt((bub.x - self.bomb.x) ** 2 + (bub.y - self.bomb.y) ** 2)
                    if dist <= Game.pop_radius:
                        bub.pop()
                        self.popped_bubbles += 1
                        todel.append(bub)
                        any_pop = True
                cnt = len(todel)
                self.stats[cnt] += 1
                self.update_stat()
                if cnt > 0:
                    for bub in todel:
                        self.bubbles.remove(bub)
                if any_pop:
                    winsound.Beep(1000, self.beep_duration)
                    self.update_score()
                else:
                    winsound.Beep(50, self.beep_duration)

    def update_stat(self):
        for i in range(Game.bubbles_count + 1):
            self.ca.itemconfig(self.stat_text_ids[i], text=f"{i} : {self.stats[i]}")


    def update_score(self):
        sco = self.popped_bubbles / self.launched_bombs * 100.0
        self.ca.itemconfig(self.score_id, text=f"{sco:.1f}%")

    def launch_plane_bomb(self):
        self.plane.has_bomb = False
        self.launched_bombs += 1
        self.bomb = BombSprite(self.ca, self.plane.x, self.plane.y, self.sprites["miss"], 50, self.plane.dx, 20, 0,
                               self.sprite_event)
        self.update_score()

    def init_bubles(self):
        self.add_bubble()
        self.add_bubble()
        self.add_bubble()

    def add_plane(self):
        y = random.randrange(40, int(Game.height * 0.4))

        if random.randint(0, 1):
            spr = self.sprites["plaL"]
            plane = random.randrange(spr.count)
            x = Game.width
            self.plane = PlaneSprite(self.ca, x, y, self.sprites["plaL"], 25, -20, 0, plane, self.sprite_event, 'L')
        else:
            spr = self.sprites["plaR"]
            plane = random.randrange(spr.count)
            x = 0
            self.plane = PlaneSprite(self.ca, x, y, self.sprites["plaR"], 25, 20, 0, plane, self.sprite_event, 'R')

    def add_bubble(self):
        sprite = random.choice([self.sprites["bub0"], self.sprites["bub1"], self.sprites["bub2"]])
        self.bubbles.append(BubbleSprite(self.ca, 0, 0, sprite, 100, 0, 0, 0, self.sprite_event))

    def sprite_event(self, type, name, obj):
        if type == 'out' and name == 'plane':
            self.plane = None
            # self.add_plane()

    def load_sprites(self):
        return {"bub0": SpriteLoader("bubble_pop_one", 5),
                "bub1": SpriteLoader("bubble_pop_two", 5),
                "bub2": SpriteLoader("bubble_pop_underwater", 5),
                "expl": SpriteLoader("explosion", 5),
                "plaL": SpriteLoader("planes_left", 6),
                "plaR": SpriteLoader("planes_right", 6),
                "miss": SpriteLoader("missile", 2),
                "pane": SpriteLoader("panel", 2)
                }

    def story(self):
        self.story_visible = True
        file = open("story.txt", 'r', encoding="utf-8")
        lines = file.readlines()
        file.close()
        y = 150
        for line in lines:
            id = self.ca.create_text(Game.width / 2, y, text=line, font="arial 30", fill="navy")
            y += 40
            self.story_ids.append(id)

    def hide_story(self):
        self.story_visible = False
        for id in self.story_ids:
            self.ca.delete(id)


class SpriteBase:
    def __init__(self, canvas, x, y, sprites, ticks, dx, dy, init_frame, event):
        self.ca = canvas
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.event = event
        self.ticks = ticks
        self.sprites = sprites
        self.frame_idx = init_frame
        self.is_live = True
        self.id = self.ca.create_image(x, y, image=self.sprites.images[self.frame_idx])

        self.update_dx_dy()
        self.on_tick()

    def next_frame_idx(self):
        pass

    def on_tick(self):
        fi = self.frame_idx
        self.next_frame_idx()
        if fi != self.frame_idx:
            self.ca.itemconfig(self.id, image=self.sprites.images[self.frame_idx])
        if self.ticks:
            if self.dx or self.dy:
                self.x += self.dx
                self.y += self.dy
                self.ca.move(self.id, self.dx, self.dy)

            self.check_out()

            if self.is_live:
                self.update_dx_dy()
                self.ca.after(self.ticks, self.on_tick)
            else:
                self.ca.delete(self.id)

    def update_dx_dy(self):
        pass

    def check_out(self):
        pass


class DetonationSprite(SpriteBase):
    def __init__(self, canvas, x, y, sprites, ticks, dx, dy, init_frame, event):
        super().__init__(canvas, x, y, sprites, ticks, dx, dy, init_frame, event)

    def next_frame_idx(self):
        self.frame_idx += 1

    def check_out(self):
        if self.frame_idx == self.sprites.count - 1:
            self.is_live = False


class BombSprite(SpriteBase):
    def __init__(self, canvas, x, y, sprites, ticks, dx, dy, init_frame, event):
        self.fdx = float(dx)
        super().__init__(canvas, x, y, sprites, ticks, dx, dy, init_frame, event)

    def check_out(self):
        if self.y >= Game.height:
            self.is_live = False;
        else:
            self.fdx *= 0.95
            self.dx = round(self.fdx)


class PlaneSprite(SpriteBase):
    def __init__(self, canvas, x, y, sprites, ticks, dx, dy, init_frame, event, pdir):
        self.dir = pdir
        self.has_bomb = True
        super().__init__(canvas, x, y, sprites, ticks, dx, dy, init_frame, event)

    def check_out(self):
        if self.dir == 'L':  # leti dolava, cize zprava dolava a out je ked ma x = -size
            if self.x < -self.sprites.width:
                if self.event:
                    self.is_live = False
                    self.event('out', 'plane', self)
        else:
            if self.x > Game.width:
                if self.event:
                    self.is_live = False
                    self.event('out', 'plane', self)


class BubbleSprite(SpriteBase):
    def __init__(self, canvas, x, y, sprites, ticks, dx, dy, init_frame, event):
        self.dx = random.randrange(10)
        self.border_limit = 100
        self.dy = random.randrange(10)
        self.duration = random.randrange(20, 40)
        self.pop_state = False
        x = random.randint(self.border_limit, Game.width - self.border_limit)
        y = random.randint(self.border_limit, Game.height - self.border_limit)
        super().__init__(canvas, x, y, sprites, ticks, self.dx, self.dy, init_frame, event)

    def update_dx_dy(self):
        if self.duration <= 0:
            self.dx = self.dy = 0
            while self.dx == 0 and self.dy == 0:
                self.dx = random.randrange(-10, 11)
                self.dy = random.randrange(-10, 11)
            self.duration = random.randrange(10, 20)
        else:
            self.duration -= 1

        x, y = self.ca.coords(self.id)
        if x < self.border_limit:
            self.dx = abs(self.dx)
        if y < self.border_limit:
            self.dy = abs(self.dy)
        if x + self.sprites.width > Game.width - self.border_limit:
            self.dx = -abs(self.dx)
        if y + self.sprites.height > Game.height - self.border_limit:
            self.dy = -abs(self.dy)

    def next_frame_idx(self):
        if self.pop_state:
            self.frame_idx += 1

    def check_out(self):
        if self.pop_state and self.frame_idx == self.sprites.count - 1:
            self.is_live = False

    def pop(self):
        self.pop_state = True;


class SpriteLoader:
    def __init__(self, path, unzoom=1):
        self.images = []
        _, _, filenames = next(walk(f"images\\{path}"))
        filenames.sort()
        for fn in filenames:
            self.im = tk.PhotoImage(file=f'images\\{path}\\{fn}')
            if unzoom > 1:
                self.im = self.im.subsample(unzoom, unzoom)
            self.images.append(self.im)
        self.width = self.im.width()
        self.height = self.im.height()
        self.count = len(self.images)
        del self.im

    def __str__(self):
        return f"{len(self.images)} images"


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        self.master.geometry(self._geom)
        self._geom = geom


game = Game()
app = FullScreenApp(game)
game.update()
game.focus_force()
game.mainloop()
