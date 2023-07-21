import math

import numpy as np


def add_channel_dim(sound_1d_arr, n_channels=2):

    if sound_1d_arr.ndim == 0:
        sound_2d_arr_tmp = np.expand_dims(sound_1d_arr, axis=[0, 1])
    elif sound_1d_arr.ndim == 1:
        sound_2d_arr_tmp = np.expand_dims(sound_1d_arr, axis=1)
    elif sound_1d_arr.ndim == 2:
        if sound_1d_arr.shape[1] == 1:
            sound_2d_arr_tmp = sound_1d_arr
        elif sound_1d_arr.shape[1] == n_channels:
            return sound_1d_arr
        else:
            raise ValueError('sound_1d_arr')
    else:
        raise ValueError('sound_1d_arr')

    sound_2d_arr = np.concatenate([sound_2d_arr_tmp for c in range(0, n_channels, 1)], axis=1)

    return sound_2d_arr


def floats_to_ints(sound_arr_floats):

    bits_per_sample = -16
    half_n_possible_values = 2 ** (abs(bits_per_sample) - 1)
    n_possible_values = half_n_possible_values * 2

    if bits_per_sample < 0:
        abs_sound = np.abs(sound_arr_floats)
        if np.any(abs_sound > 1.0):
            max_abs = np.max(abs_sound, keepdims=False, initial=-math.inf)
            sound_arr_floats = sound_arr_floats / max_abs

    # a = np.floor(sound_arr_floats * (half_n_possible_values - 0.00000001))
    sound_arr_ints = np.floor(sound_arr_floats * (half_n_possible_values - 0.00000001)).astype(np.int16)

    return sound_arr_ints
