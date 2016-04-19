#!/usr/bin/env python

from __future__ import print_function

import random
import time

from progress.bar import (Bar, ChargingBar, FillingSquaresBar,
                          FillingCirclesBar, IncrementalBar, ShadyBar, Random)
from progress.spinner import Spinner, PieSpinner, MoonSpinner, LineSpinner
from progress.counter import Counter, Countdown, Stack, Pie


def sleep(t=0.01):
    t += t * random.uniform(-0.1, 0.1)  # Add some variance
    time.sleep(t)

for bar_cls in (Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar, DottedBar):
    suffix = '%(index)d/%(max)d [%(elapsed)d / %(eta)d]'
    bar = bar_cls(bar_cls.__name__, suffix=suffix)
    for i in bar.iter(range(200)):
        sleep()

for bar_cls in (IncrementalBar, ShadyBar):
    suffix = '%(percent)d%% [%(elapsed_td)s / %(eta_td)s]'
    bar = bar_cls(bar_cls.__name__, suffix=suffix)
    for i in bar.iter(range(200)):
        sleep()

for spin in (Spinner, PieSpinner, MoonSpinner, LineSpinner, DotSpinner):
    for i in spin(spin.__name__ + ' ').iter(range(25)):
        sleep(0.1)
    print()

for singleton in (Counter, Countdown, Stack, Pie):
    for i in singleton(singleton.__name__ + ' ').iter(range(100)):
        sleep()
    print()

bar = IncrementalBar('Random', suffix='%(index)d')
for i in range(100):
    bar.goto(random.randint(0, 100))
    sleep()
bar.finish()
