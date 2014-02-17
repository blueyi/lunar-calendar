#!/usr/bin/env python3

# Copyright (C) 2013-2014 LiuLang <gsushzhsosgsu@gmail.com>
# Use of this source code is governed by GPLv3 license that can be found
# in http://www.gnu.org/licenses/gpl-3.0.html


import os
import sys
sys.path.append(os.path.dirname(__file__))

from gi.repository import Gio
from gi.repository import Gtk

from LunarCalendar import LunarCalendar
import Config

APP_NAME = 'org.liulang.lunar_calendar'


class App:

    def __init__(self):
        self.app = Gtk.Application.new(APP_NAME, 0)
        self.app.connect('startup', self.on_app_startup)
        self.app.connect('activate', self.on_app_activate)

    def on_app_startup(self, app):
        self.window = Gtk.ApplicationWindow(application=app)
        self.window.set_icon_name('lunar-calendar')
        app.add_window(self.window)

        self.lunar = LunarCalendar()

        self.cal = Gtk.Calendar.new()
        self.cal.props.show_day_names = True
        self.cal.props.show_details = True 
        self.cal.props.show_heading = True
        self.cal.props.show_week_numbers = True
        self.cal.set_detail_width_chars(6)
        self.cal.set_detail_height_rows(2)
        self.cal.set_detail_func(self.update_cal, None)
        self.window.add(self.cal)
        self.cal.connect('day-selected', self.on_cal_day_selected)

        builder = Gtk.Builder()
        builder.add_from_file(Config.MENUS_UI)
        appmenu = builder.get_object('appmenu')
        app.set_app_menu(appmenu)
        self.add_simple_action('about', self.on_action_about_activate)
        self.add_simple_action('quit', self.on_action_quit_activate)

    def on_app_activate(self, app):
        self.window.show_all()

    def run(self, argv):
        self.app.run(argv)

    def add_simple_action(self, name, callback):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.app.add_action(action)

    def on_action_about_activate(self, action, param):
        dialog = Gtk.AboutDialog()
        dialog.set_modal(True)
        dialog.set_transient_for(self.window)
        dialog.set_program_name(Config.APPNAME)
        dialog.set_logo_icon_name('lunar-calendar')
        dialog.set_version(Config.VERSION)
        dialog.set_comments(Config.DESCRIPTION)
        dialog.set_copyright('Copyright (c) 2014 LiuLang')
        dialog.set_website(Config.HOMEPAGE)
        dialog.set_license_type(Gtk.License.GPL_3_0)
        dialog.set_authors(Config.AUTHORS)
        dialog.run()
        dialog.destroy()

    def on_action_quit_activate(self, action, param):
        self.app.quit()

    def on_cal_day_selected(self, cal):
        year, month_, day = cal.get_date()
        month = month_ + 1
        info = self.get_day_info(year, month, day)
        print(info)
        self.update_window_title(info)

    def update_cal(self, cal, year, month_, day, data):
        month = month_ + 1
        info = self.get_day_info(year, month, day)
        holiday = []
        if info['lunarHoliday']:
            holiday.append(info['lunarHoliday'])
        if info['solarHoliday']:
            holiday.append(info['solarHoliday'])
        if holiday:
            if len(holiday) == 2:
                return '\n'.join(holiday)
            return holiday[0]

        if info['lunarDay'] == '初一':
            return info['lunarMonth']
        return info['lunarDay']

    def update_window_title(self, info):
        title = '{0} 年  农历 {1}年 {2}年'.format(
                info['gregorianYear'],
                info['stermBranch'],
                info['animalZodiac'])
        self.window.props.title = title

    def get_day_info(self, year, month, day, memory={}):
        key = '{0}-{1}-{2}'.format(year, month, day)
        if key in memory:
            return memory[key]
        self.lunar.setGregorian(year, month, day)
        memory[key] = self.lunar.getCalendar()
        return memory[key]

