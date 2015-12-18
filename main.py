#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

from numpy import pi

TWOPI = pi*2.

NMAX = 10**6
SIZE = 1400
ONE = 1./SIZE

INIT_NUM = 20000
INIT_RAD = 0.4
INIT_DST = 2*ONE

MID = 0.5

LINEWIDTH = ONE*2

BACK = [1,1,1,1]
FRONT = [0,0,0,5]
RED = [1,0,0,0.3]
BLUE = [0,0,1,0.3]


i = 0


def show(render,f):

  sources = f.sources

  render.clear_canvas()

  render.ctx.set_source_rgba(*RED)

  for s in sources:

    render.circle(*s, r=ONE, fill=True)

  render.ctx.set_source_rgba(*FRONT)

  for fractures in f.old_fractures:

    s,_ = fractures[0]
    render.ctx.move_to(*sources[s,:].flatten())

    for c,_ in fractures[1:]:
      render.ctx.line_to(*sources[c,:].flatten())

    render.ctx.stroke()


def step(f):

  global i
  i += 1

  res = f.fracture()

  if i % 1 == 0:
    print('asdfasdf')
    f.make_fracture_from_old()

  return res


def main():

  import gtk
  from render.render import Animate

  from modules.fracture import Fracture

  F = Fracture(INIT_NUM, INIT_RAD, INIT_DST)


  def wrap(render):

    global i

    show(render,F)
    res = step(F)

    i += 1

    return res

  render = Animate(SIZE, BACK, FRONT, wrap)
  render.set_line_width(LINEWIDTH)
  gtk.main()


if __name__ == '__main__':

  main()

