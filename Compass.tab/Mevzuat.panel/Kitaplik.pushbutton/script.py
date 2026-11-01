# -*- coding: utf-8 -*-
"""Read regulation sources offline. No model changes. Shift: classic WPF."""
from compass.ui import launch_reader

if __name__ == '__main__':
    _compass_reader = launch_reader(force_fallback=bool(globals().get('__shiftclick__', False)))
