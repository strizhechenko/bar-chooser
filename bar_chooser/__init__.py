#!/usr/bin/env python
# coding=utf-8

import argparse
from bar_chooser.ekaterinburg import OLEG_KEYS, EKB_BARS


class BarChooser(object):
    args = {}

    def __init__(self, keys=OLEG_KEYS, bars=EKB_BARS):
        self.bars = bars
        self.keys = keys
        self.__parse_args__()
        bars = dict((bar, self.rate(bar, self.args)) for bar in self.bars)
        for key in reversed(sorted(bars, key=bars.get)):
            print("{0}: {1}".format(key, bars[key]))

    def rate(self, bar_name, params):
        score = 0
        _bar = self.bars[bar_name]
        _bar_data = dict(zip(self.keys, _bar))
        for key in self.keys:
            if params.get(key):
                score += min(_bar_data[key], params[key])
        return score

    def __parse_args__(self):
        parser = argparse.ArgumentParser()
        parser.description = "Script that help you to choose a bar to drink with someone." \
                             "Just specify something like: bar-chooser --beer=2 --meat=1 --at-home=1"
        for arg in self.keys:
            parser.add_argument('--{0}'.format(arg.replace('_', '-')), type=int)
        self.args.update(parser.parse_args().__dict__)


def main():
    BarChooser()


if __name__ == '__main__':
    main()
