import pygame as pg
from settings import *
from classes import *


def main():
    # Game constants

    do_game = True

    pg.init()
    screen = pg.display.set_mode(WIN_SIZE)
    pg.display.set_caption(PROJECT_NAME)
    clock = pg.time.Clock()

    # Objects

    star = Stars(screen, 50, 50)

    rocket = Rocket(screen, WIN_WIDTH // 2 - 21, WIN_HEIGHT // 2 + WIN_HEIGHT // 4 - 37)

    # Cursor position variables

    old_mouse_x = None

    while do_game:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                do_game = False

        # Controls

        if pg.mouse.get_focused():
            rocket.x = pg.mouse.get_pos()[0]

            if old_mouse_x is None:
                old_mouse_x = pg.mouse.get_pos()[0]
            if old_mouse_x < pg.mouse.get_pos()[0]:
                rocket.state = "ToRight"
                old_mouse_x = pg.mouse.get_pos()[0]
            elif old_mouse_x > pg.mouse.get_pos()[0]:
                rocket.state = "ToLeft"
                old_mouse_x = pg.mouse.get_pos()[0]
            elif old_mouse_x == pg.mouse.get_pos()[0]:
                rocket.state = "Idle"

        if rocket.x > WIN_WIDTH - rocket.w * 2:
            rocket.x = WIN_WIDTH - rocket.w * 2

        # Drawing objects

        screen.fill(SPACE_COLOR)

        star.draw()
        star.update()
        rocket.update()
        rocket.animation()

        pg.display.flip()

        clock.tick(FPS)

    pg.quit()


if __name__ == "__main__":
    main()
