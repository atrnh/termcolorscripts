# -*- coding: utf-8 -*-

from colors import Colors
from os import system



SWIRL = u"""\
                  ¸·`¨¯¨`·¸    ¸·`¨¯¨`·¸
    ¸·*¨¯¨*·.¸    `·-·`    )  (    `·-·`    ¸.·*¨¯¨*·¸
   (  ×¨¯)    `·.¸¸____¸.·`    `·.¸____¸¸.·´    (¯¨×  )
.¨* `·-·'╔═══·´¨¯¨`×¸════════════════¸×´¨¯¨`·═══╗'·-·` *¨.
 `¤·.,¸¸,║·′      `.˙                ˙·´      `·║,¸¸,.·¤´
         ║                                      ║\
"""
BEFORE_BORDER = 9
BORDER = u'║'
SPACE_INSIDE = 38


def make_blocks(width):
    """Return list of blocks."""

    block = ' ' * width
    return ['{}{}{}'.format(color, block, Colors.reset) for color in Colors.bg_colors ]


def print_line(line, width=None, real_w=None):
    space_left = SPACE_INSIDE
    width = width or len(line)

    s = (' ' * BEFORE_BORDER) + BORDER
    margin = int((SPACE_INSIDE - width) / 2)
    s += margin * ' '
    s += line
    if real_w:
        space_left -= margin + real_w

        if space_left > 0:
            s += space_left * ' '
    else:
        s += margin * ' '

    s += BORDER

    print(s)

if __name__ == '__main__':
    import sys

    system('clear')
    print(SWIRL)
    blocks = make_blocks(4)
    width = 4 * 8
    print_line(' ' * SPACE_INSIDE)
    print_line(sys.argv[1])
    print_line(' ' * SPACE_INSIDE)
    print_line(''.join(blocks[:8]), width)
    print_line(''.join(blocks[:8]), width)
    print_line(''.join(blocks[:8]), width)
    print_line(''.join(blocks[:8]), width)
    print_line(''.join(blocks[:8]), width)
    print_line(''.join(blocks[8:]), width)
    print_line(''.join(blocks[8:]), width)

    a = '{magenta}def{reset} {green}self{reset}.example'.format(
        magenta=Colors.magenta,
        reset=Colors.reset,
        green=Colors.green
    )
    b = ("  [{red}'string'{reset}, "
         '{red}1.0{reset}].each {yellow}do{reset} |{cyan}val{reset}|').format(
             red=Colors.red,
             reset=Colors.reset,
             yellow=Colors.yellow,
             cyan=Colors.cyan
        )
    c = '    puts {magenta}"#{{{reset}val.class{magenta}}}"{reset}'.format(
        magenta=Colors.magenta,
        reset=Colors.reset
    )
    d = '  {yellow}end{reset}'.format(yellow=Colors.yellow, reset=Colors.reset)
    e = '{yellow}end{reset}'.format(yellow=Colors.yellow, reset=Colors.reset)


    print_line(' ' * SPACE_INSIDE)
    print_line(a, 32, 16)
    print_line(b, 32, 31)
    print_line(c, 32, 23)
    print_line(d, 32, 5)
    print_line(e, 32, 3)
    print_line(' ' * SPACE_INSIDE)
    print_line(' ' * SPACE_INSIDE)
    print_line(' ' * SPACE_INSIDE)
    end = """\
         ╚══════════════════════════════════════╝\
    """
    print(end)
