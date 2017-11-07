Bar-chooser
===========

The script (`web-version`_) that helps you to choose a bar to drink with someone.

Why?
----

I spent too much time to choose a bar to go with different people:

- One need vegan food.
- Second wants to drink nice beer.
- Third wants perfect steak.
- Fourth has little money but want to drink a lot.
- I want to drink near my home.
- Sometimes we need to meet somewhere at the city center.

And all these metrics should be combined to find a perfect place for a given booze.

Installation
------------

.. code:: shell
  
  pip install bar-chooser

Usage
-----

.. code:: shell
  
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


Customizing
-----------

Create your own utility based on BarChooser.

.. code:: python
  
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

TODO
----

- [x] prototype
- [x] argparse
- [x] submit a package in PYPI
- [x] `web-version`_
- [ ] tests
- [ ] badges
- [ ] config support
- [ ] testing on linux
- [ ] android app
- [ ] iOS app
- [ ] pr

.. _web-version: https://strizhechenko.github.io/bar-chooser/web/
