# Copyright (C) 2013-2014 LiuLang <gsushzhsosgsu@gmail.com>
# Use of this source code is governed by GPLv3 license that can be found
# in http://www.gnu.org/licenses/gpl-3.0.html

import os
import gettext
import locale

if __file__.startswith('/usr/local/'):
    PREF = '/usr/local/share'
elif __file__.startswith('/usr/'):
    PREF = '/usr/share'
else:
    PREF = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'share')

LOCALEDIR = os.path.join(PREF, 'locale')
gettext.bindtextdomain('lunar-calendar', LOCALEDIR)
gettext.textdomain('lunar-calendar')
locale.bindtextdomain('lunar-calendar', LOCALEDIR)
locale.textdomain('lunar-calendar')
_ = gettext.gettext

APPNAME = _('Lunar Calendar')
VERSION = '1.1'
HOMEPAGE = 'https://github.com/LiuLang/lunar_calendar'
AUTHORS = ['LiuLang <gsushzhsosgsu@gmail.com>', ]
DESCRIPTION = _('A Chinese lunar calendar for linux desktop users')

MENUS_UI = os.path.join(PREF, 'lunar-calendar', 'menus.ui')
