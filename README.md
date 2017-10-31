# bar-chooser

Script that help you to choose a bar to drink with someone.

## Why?

I spent too much time to choose bar to go with different person:

- One need vegan food
- second wants to drink nice bear
- third wants perfect steak
- fourth has little money but want to drink a lot
- I want to drink near my home
- sometimes we need to meet somewhere at the city center

And all these metrics should be combined to find a perfect place for given booze.

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
