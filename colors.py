class Colors:
    """Store color strings & other utilities."""

    esc = u'\u001b'

    reset = esc + u'[0m'

    black = esc + u'[30m'
    red = esc + u'[31m'
    green = esc + u'[32m'
    yellow = esc + u'[33m'
    blue = esc + u'[34m'
    magenta= esc + u'[35m'
    cyan = esc + u'[36m'
    white = esc + u'[37m'

    b_black = esc + u'[90m'
    b_red = esc + u'[91m'
    b_green = esc + u'[92m'
    b_yellow = esc + u'[93m'
    b_blue = esc + u'[94m'
    b_magenta = esc + u'[95m'
    b_cyan = esc + u'[96m'
    b_white = esc + u'[97m'

    bg_black = esc + u'[40m'
    bg_red = esc + u'[41m'
    bg_green = esc + u'[42m'
    bg_yellow = esc + u'[43m'
    bg_blue = esc + u'[44m'
    bg_magenta= esc + u'[45m'
    bg_cyan = esc + u'[46m'
    bg_white = esc + u'[47m'

    bg_b_black = esc + u'[100m'
    bg_b_red = esc + u'[101m'
    bg_b_green = esc + u'[102m'
    bg_b_yellow = esc + u'[103m'
    bg_b_blue = esc + u'[104m'
    bg_b_magenta = esc + u'[105m'
    bg_b_cyan = esc + u'[106m'
    bg_b_white = esc + u'[107m'


    bg_colors = [
        bg_black,
        bg_red,
        bg_green,
        bg_yellow,
        bg_blue,
        bg_magenta,
        bg_cyan,
        bg_white,
        bg_b_black,
        bg_b_red,
        bg_b_green,
        bg_b_yellow,
        bg_b_blue,
        bg_b_magenta,
        bg_b_cyan,
        bg_b_white
    ]
