

import soundfile as sf
import synth_sounds


frequencies_sounds = [300, 400, 500]  # [Hz]
#frequencies_sounds = list(range(300, 5000 + 1, 500))

# Duration
duration_sec = 10
duration_str = '10_sec'

# duration_sec = 1 * 60 * 60
# duration_str = '1_hour'

samples_per_sec = 44100  # default value for the pygame mixer
n_channels = 2

volume = 0.1
fadein_ms = 1000
fadeout_ms = 1000

sounds_2d_arr = synth_sounds.synth_sounds_2d(
    frequencies_sounds=frequencies_sounds, duration_sec=duration_sec, samples_per_sec=samples_per_sec,
    dtype='i', n_channels=n_channels, volume=volume)

name_file = 'stereo_file_' + duration_str + '.wav'

sf.write(name_file, sounds_2d_arr, samples_per_sec, 'PCM_16')


