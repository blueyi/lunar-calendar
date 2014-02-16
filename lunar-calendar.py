#!/usr/bin/env python3


from gi.repository import Gtk

from LunarCalendar import LunarCalendar

class App(Gtk.Window):

    def __init__(self):
        super().__init__()
        self.connect('delete-event', self.on_app_exit)

        self.lunar = LunarCalendar()

        self.cal = Gtk.Calendar.new()
        #self.cal.props.show_day_names = True
        self.cal.props.show_details = True 
        self.cal.props.show_heading = True
        self.cal.props.show_week_numbers = True
        self.cal.set_detail_width_chars(5)
        self.cal.set_detail_height_rows(2)
        self.cal.set_detail_func(self.update_cal, None)
        self.cal.connect('day-selected', self.on_cal_day_selected)
        self.add(self.cal)

    def run(self):
        self.show_all()
        Gtk.main()

    def on_app_exit(self, *args):
        Gtk.main_quit()

    def on_cal_day_selected(self, cal):
        print('on day_selected')
        cal.mark_day(12)
        year, month_, day = cal.get_date()
        month = month_ + 1
        self.lunar.setGregorian(year, month, day)
        stermBranch = self.lunar.getStermBranch()
        print(stermBranch)

    def update_cal(self, cal, year, month_, day, data):
        month = month_ + 1
        if day % 10 == 0:
            return '廿四'
        else:
            return ''


def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
