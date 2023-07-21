
from __future__ import annotations
import numpy as np
from . import tools


def synth_sound_1d(
        frequency_sound, duration_sec: int | float, samples_per_sec=44100, dtype='f', volume: int | float = 1.0):

    # n_frames = int(duration_sec * samples_per_sec)

    duration_sec_per_frame = 1 / samples_per_sec
    times_sec_frames = np.arange(0, duration_sec, duration_sec_per_frame, dtype=np.float64)

    sound_1d_arr = np.sin(2 * np.pi * frequency_sound * times_sec_frames)

    if (volume is None) or (volume == 1.0):
        pass
    else:
        sound_1d_arr *= volume

    if (dtype == 'f') or (dtype == float) or (dtype == np.float64):
        pass
    elif (dtype == 'i') or (dtype == int) or (dtype == np.int16):
        sound_1d_arr = tools.floats_to_ints(sound_1d_arr)
    else:
        raise ValueError('dtype')

    return sound_1d_arr


def synth_sound_2d(
        frequency_sound, duration_sec: int | float, samples_per_sec=44100, dtype='f',
        n_channels=2, volume: int | float = 1.0):

    sound_1d_arr = synth_sound_1d(
        frequency_sound=frequency_sound, duration_sec=duration_sec,
        samples_per_sec=samples_per_sec, dtype=dtype, volume=volume)

    sound_2d_arr = tools.add_channel_dim(sound_1d_arr=sound_1d_arr, n_channels=n_channels)

    return sound_2d_arr


def synth_sounds_1d(
        frequencies_sounds, duration_sec: int | float, samples_per_sec=44100, dtype='f', volume: int | float = 1.0):

    # n_frames = int(duration_sec * samples_per_sec)

    duration_sec_per_frame = 1 / samples_per_sec
    times_sec_frames = np.arange(0, duration_sec, duration_sec_per_frame, dtype=np.float64)

    # sum_sounds_1d_arr = 0.0
    sum_sounds_1d_arr = np.zeros(shape=times_sec_frames.shape, dtype=times_sec_frames.dtype)

    S = len(frequencies_sounds)
    for s in range(0, S, 1):

        sound_1d_arr_s = np.sin(2 * np.pi * frequencies_sounds[s] * times_sec_frames)

        # sound_1d_arr_s = synth_sound_1d(
        #     frequency_sound=frequencies_sounds[s], duration_sec=duration_sec,
        #     samples_per_sec=samples_per_sec, dtype='f', volume=None)

        sum_sounds_1d_arr += sound_1d_arr_s

    sounds_1d_arr = sum_sounds_1d_arr / S

    if (volume is None) or (volume == 1.0):
        pass
    else:
        sounds_1d_arr *= volume

    if (dtype == 'f') or (dtype == float) or (dtype == np.float64):
        pass
    elif (dtype == 'i') or (dtype == int) or (dtype == np.int16):
        sounds_1d_arr = tools.floats_to_ints(sounds_1d_arr)
    else:
        raise ValueError('dtype')

    return sounds_1d_arr


def synth_sounds_2d(
        frequencies_sounds, duration_sec: int | float, samples_per_sec=44100, dtype='f',
        n_channels=2, volume: int | float = 1.0):

    sum_sounds_1d_arr = 0.0

    sounds_1d_arr = synth_sounds_1d(
        frequencies_sounds=frequencies_sounds, duration_sec=duration_sec,
        samples_per_sec=samples_per_sec, dtype=dtype, volume=volume)

    sounds_2d_arr = tools.add_channel_dim(sound_1d_arr=sounds_1d_arr, n_channels=n_channels)

    return sounds_2d_arr
