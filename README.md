# bar-chooser

Script that help you to choose a bar to drink with someone.

## Installation

``` shell
pip install bar-chooser
```


## Usage

``` shell
$ bar-chooser --meat=2 --beer=1 --cheap=1 --at-work=1 --at-home=1
pan-smetan: 4
8500: 4
ratskeller: 3
new-bar: 3
peperonni: 3
yankee-bar: 3
jawsspot: 2
marusya: 2
misantrop: 2
```

## Customizing

Create your own utility based on BarChooser.

``` python
from bar_chooser import BarChooser

MY_KEYS = ['vodka', 'seledka']
MY_BARS = {
    'bar1': [2, 1],
    'bar2': [0, 2],
}

def main():
    BarChooser(MY_KEYS, MY_BARS)

if __name__ == '__main__':
    main()
```
