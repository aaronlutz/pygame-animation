import sys
import pygame
from label import ReadOut


def check_events(character):
    """Respond to keypresses and mouse events."""
    # Check new events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_keydown(event, character)
        elif event.type == pygame.KEYUP:

            # if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            on_keyup(event, character)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            event_pos = event.pos
            print('mousedown')
            #slider.check_if_clicked(event_pos)

        elif event.type == pygame.MOUSEBUTTONUP:
            #slider.clicked = False
            print('deletethis')
        elif event.type == pygame.MOUSEMOTION:
            #if slider.clicked:
            #    event_pos = event.pos
            #    slider.update_slider(event_pos)
            print('deletethis')
			
    # Check keys being held down
    check_keys_held_down(character)


def check_keys_held_down(character):
    '''Loop through key booleans to check for keys currently down.'''
    keys = pygame.key.get_pressed()
    if keys[275] == 1:  # Right
        print('right held')
        character.direction = 'right'
        character.set_action('walking')
    if keys[276] == 1:  # Left
        print('left held')
        character.direction = 'left'
        character.set_action('walking')
    if keys[273] == 1 and keys[99] == 1:  # up and c
        character.set_action('climbing')
        character.vertical_coef = 1
    if keys[274] == 1 and keys[99] == 1:  # down and c
        character.set_action('climbing')
        character.vertical_coef = -1

    for k in range(0, len(keys)):
        if keys[k] == 1:
            print(k)


def on_keyup(event, character):
    keys = pygame.key.get_pressed()
    print(str(event.key) + ' up')

    if character.action == 'climbing':
        if keys[273] == 0 and keys[274] == 0:
            print('stop climbing test past')
            character.set_action('standing')
    if keys[275] == 0:
        character.set_action('standing')

    if keys[275] == 0 and keys[276] == 0:
        character.set_action('standing')
        character.delta_x = 0


def on_keydown(event, character):
    keys = pygame.key.get_pressed()
    if event.key == pygame.K_UP:
        if keys[99] == 1:
            character.set_action('climbing')
        elif keys[99] == 0:
            character.set_action('jumping')
    elif event.key == pygame.K_b:
        print('b pressed')
        character.set_action('backflipping')
    # elif event.key == pygame.K_c:
    #	character.set_action('climbing')
    elif event.key == pygame.K_DOWN:
        print('down pressed')
        character.set_action('kneeling')
    elif event.key == pygame.K_LEFT:
        print('left pressed')
        character.set_action('walking')
        character.direction = 'left'
    elif event.key == pygame.K_RIGHT:
        print('right pressed')
        character.set_action('walking')
        character.direction = 'right'


def update_screen(screen, settings, character, scene, readouts):
    '''Draw the new Screen.'''
    # Background
    screen.fill((240, 249, 255))
    scene.draw_scene(screen, settings)
    # Character
    character.do(scene)
    character.increment_frame()
    character.blitme(screen)
    character.frame_total += 1
    # Slider
    #slider.draw_me(screen)
    # Readouts
    #readouts['delay'].update_val(slider.value)
    #readouts['delay'].blitme()
    readouts['frame'].update_val(character.frame)
    readouts['frame'].blitme()
    readouts['char_xy'].update_val(str((character.x, character.y)))
    readouts['char_xy'].blitme()
    readouts['delta_xy'].update_val(str((character.delta_x, character.delta_y)))
    readouts['delta_xy'].blitme()
    readouts['action'].update_val(character.action)
    readouts['action'].blitme()
    readouts['direction'].update_val(character.direction)
    readouts['direction'].blitme()
    readouts['delta_y_since_start'].update_val(character.y - settings.char_start_y)
    readouts['delta_y_since_start'].blitme()
    # Display New Screen
    pygame.display.flip()


def create_read_outs(screen, settings, character):
    readouts = {}
#    readouts['delay'] = ReadOut(screen, settings.dd_pos,
#                                settings.slider_start_value,
#                               txt_color=(0, 0, 0), font_size=30,
#                                pre_text='Milliseconds between frames: ',
#                                post_text=' ms')
    readouts['frame'] = ReadOut(screen, (settings.fd_pos),
                                character.frame,
                                txt_color=(0, 0, 0), font_size=30,
                                pre_text='Current Frame: ')
    readouts['char_xy'] = ReadOut(screen, (settings.xy_pos),
                                  str((character.x, character.y)),
                                  txt_color=(0, 0, 0), font_size=30)
    readouts['delta_xy'] = ReadOut(screen, (settings.delta_xy_pos),
                                   str((0, 0)),
                                   txt_color=(0, 0, 0), font_size=30)
    readouts['delta_y_since_start'] = ReadOut(screen, (settings.delta_y_pos),
                                              str(0), txt_color=(0, 0, 0), font_size=30)
    readouts['action'] = ReadOut(screen, (settings.action_pos),
                                 'standing', txt_color=(0, 0, 0), font_size=30)
    readouts['direction'] = ReadOut(screen, (settings.direction_pos),
                                    'right', txt_color=(0, 0, 0), font_size=30)

    return readouts
