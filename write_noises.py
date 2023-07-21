import math

import numpy as np
import soundfile as sf
import audiomixer


# color = 'white'
# color = 'pink'
# color = 'blue'
# color = 'brown'
color = 'violet'
# 'white', 'pink','blue', 'brown', 'violet'

# Duration
# duration_sec = 10
# duration_str = '10_sec'

duration_sec = 1 * 60 * 60
duration_str = '1_hour'
secs_one_repetition = duration_sec

# 44100 is default value for the pygame mixer
samples_per_sec = 44100

# samples_per_sec = math.floor(samples_per_sec / 2)  # for brown
samples_per_sec = math.floor(samples_per_sec / 10)  # for other colors
n_channels = 2

volume = 1000.0
fadein_ms = 1000
fadeout_ms = 1000

sounds_2d_arr = audiomixer.synth.noises.synth_noise_2d(
    color=color, duration_sec=secs_one_repetition, mirror=True, samples_per_sec=samples_per_sec,
    dtype='i', n_channels=n_channels, volume=volume)


n_mins = math.floor(60 / secs_one_repetition) * 60
if n_mins > 0:
    sounds_2d_arr = np.concatenate([sounds_2d_arr for m in range(0, n_mins, 1)], axis=0)

name_file = 'audio_files\\noises\\' + color + '_' + duration_str + '.wav'

sf.write(name_file, sounds_2d_arr, samples_per_sec, 'PCM_16')
