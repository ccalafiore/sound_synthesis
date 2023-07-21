import keyboard
import pygame as pg
import audiomixer


color = 'white'
# color = 'pink'
# color = 'blue'
# color = 'brown'
# color = 'violet'
# 'white', 'pink','blue', 'brown', 'violet'


duration_sec = 2  # [s]

samples_per_sec = 44100  # default value for the pygame mixer
bits_per_sample = -16
n_channels = 2
buffer = 512

volume = 1.0
fadein_ms = 3000
fadeout_ms = 3000

pg.init()
pg.mixer.init(frequency=samples_per_sec, size=bits_per_sample, channels=n_channels, buffer=buffer, devicename=None)

sounds_2d_arr = audiomixer.synth.noises.synth_noise_2d(
    color=color, duration_sec=10, mirror=True, samples_per_sec=samples_per_sec,
    dtype='i', n_channels=n_channels, volume=volume)

sounds_2d_pg = pg.sndarray.make_sound(sounds_2d_arr.copy())

sounds_2d_pg.play(loops=-1, maxtime=0, fade_ms=fadein_ms)

print('playing ...')

keyboard.wait('esc')

print('fading out ...')

sounds_2d_pg.fadeout(fadeout_ms)
pg.time.wait(fadeout_ms)

pg.mixer.quit()
pg.quit()

print('finished!!')
