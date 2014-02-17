
# Copyright (C) 2013-2014 LiuLang <gsushzhsosgsu@gmail.com>
# Use of this source code is governed by GPLv3 license that can be found
# in http://www.gnu.org/licenses/gpl-3.0.html


class LunarCalendar:

    # 公历中每月的天数, 其中的二月在平年是28天, 闰年是29天 
    gregorianDays = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # 十个天干名
    heavenlySterms = (
        '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸')
    # 十二个地支名
    earthlyBranches = (
        '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉',
        '戌', '亥')
    # 十二生肖名
    animalZodiac = (
        '鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '㺅', '鸡',
        '狗', '猪')
    # 农历月份大小的记录表, 1901-2100
    lunarMonths = (
        0x00, 0x04, 0xad, 0x08, 0x5a, 0x01, 0xd5, 0x54, 0xb4, 0x09,
        0x64, 0x05, 0x59, 0x45, 0x95, 0x0a, 0xa6, 0x04, 0x55, 0x24,
        0xad, 0x08, 0x5a, 0x62, 0xda, 0x04, 0xb4, 0x05, 0xb4, 0x55,
        0x52, 0x0d, 0x94, 0x0a, 0x4a, 0x2a, 0x56, 0x02, 0x6d, 0x71,
        0x6d, 0x01, 0xda, 0x02, 0xd2, 0x52, 0xa9, 0x05, 0x49, 0x0d,
        0x2a, 0x45, 0x2b, 0x09, 0x56, 0x01, 0xb5, 0x20, 0x6d, 0x01,
        0x59, 0x69, 0xd4, 0x0a, 0xa8, 0x05, 0xa9, 0x56, 0xa5, 0x04,
        0x2b, 0x09, 0x9e, 0x38, 0xb6, 0x08, 0xec, 0x74, 0x6c, 0x05,
        0xd4, 0x0a, 0xe4, 0x6a, 0x52, 0x05, 0x95, 0x0a, 0x5a, 0x42,
        0x5b, 0x04, 0xb6, 0x04, 0xb4, 0x22, 0x6a, 0x05, 0x52, 0x75,
        0xc9, 0x0a, 0x52, 0x05, 0x35, 0x55, 0x4d, 0x0a, 0x5a, 0x02,
        0x5d, 0x31, 0xb5, 0x02, 0x6a, 0x8a, 0x68, 0x05, 0xa9, 0x0a,
        0x8a, 0x6a, 0x2a, 0x05, 0x2d, 0x09, 0xaa, 0x48, 0x5a, 0x01,
        0xb5, 0x09, 0xb0, 0x39, 0x64, 0x05, 0x25, 0x75, 0x95, 0x0a,
        0x96, 0x04, 0x4d, 0x54, 0xad, 0x04, 0xda, 0x04, 0xd4, 0x44,
        0xb4, 0x05, 0x54, 0x85, 0x52, 0x0d, 0x92, 0x0a, 0x56, 0x6a,
        0x56, 0x02, 0x6d, 0x02, 0x6a, 0x41, 0xda, 0x02, 0xb2, 0xa1,
        0xa9, 0x05, 0x49, 0x0d, 0x0a, 0x6d, 0x2a, 0x09, 0x56, 0x01,
        0xad, 0x50, 0x6d, 0x01, 0xd9, 0x02, 0xd1, 0x3a, 0xa8, 0x05,
        0x29, 0x85, 0xa5, 0x0c, 0x2a, 0x09, 0x96, 0x54, 0xb6, 0x08,
        0x6c, 0x09, 0x64, 0x45, 0xd4, 0x0a, 0xa4, 0x05, 0x51, 0x25,
        0x95, 0x0a, 0x2a, 0x72, 0x5b, 0x04, 0xb6, 0x04, 0xac, 0x52,
        0x6a, 0x05, 0xd2, 0x0a, 0xa2, 0x4a, 0x4a, 0x05, 0x55, 0x94,
        0x2d, 0x0a, 0x5a, 0x02, 0x75, 0x61, 0xb5, 0x02, 0x6a, 0x03,
        0x61, 0x45, 0xa9, 0x0a, 0x4a, 0x05, 0x25, 0x25, 0x2d, 0x09,
        0x9a, 0x68, 0xda, 0x08, 0xb4, 0x09, 0xa8, 0x59, 0x54, 0x03,
        0xa5, 0x0a, 0x91, 0x3a, 0x96, 0x04, 0xad, 0xb0, 0xad, 0x04,
        0xda, 0x04, 0xf4, 0x62, 0xb4, 0x05, 0x54, 0x0b, 0x44, 0x5d,
        0x52, 0x0a, 0x95, 0x04, 0x55, 0x22, 0x6d, 0x02, 0x5a, 0x71,
        0xda, 0x02, 0xaa, 0x05, 0xb2, 0x55, 0x49, 0x0b, 0x4a, 0x0a,
        0x2d, 0x39, 0x36, 0x01, 0x6d, 0x80, 0x6d, 0x01, 0xd9, 0x02,
        0xe9, 0x6a, 0xa8, 0x05, 0x29, 0x0b, 0x9a, 0x4c, 0xaa, 0x08,
        0xb6, 0x08, 0xb4, 0x38, 0x6c, 0x09, 0x54, 0x75, 0xd4, 0x0a,
        0xa4, 0x05, 0x45, 0x55, 0x95, 0x0a, 0x9a, 0x04, 0x55, 0x44,
        0xb5, 0x04, 0x6a, 0x82, 0x6a, 0x05, 0xd2, 0x0a, 0x92, 0x6a,
        0x4a, 0x05, 0x55, 0x0a, 0x2a, 0x4a, 0x5a, 0x02, 0xb5, 0x02,
        0xb2, 0x31, 0x69, 0x03, 0x31, 0x73, 0xa9, 0x0a, 0x4a, 0x05,
        0x2d, 0x55, 0x2d, 0x09, 0x5a, 0x01, 0xd5, 0x48, 0xb4, 0x09,
        0x68, 0x89, 0x54, 0x0b, 0xa4, 0x0a, 0xa5, 0x6a, 0x95, 0x04,
        0xad, 0x08, 0x6a, 0x44, 0xda, 0x04, 0x74, 0x05, 0xb0, 0x25,
        0x54, 0x03)

    # 大闰月的闰年年份
    bigLeapMonthYears = (
         6, 14,  19,  25,  33,  36,  38,  41,  44,  52,
        55, 79, 117, 136, 147, 150, 155, 158, 185, 193)
    sectionalTermMap = (
        (),
        (7,6,6,6,6,6,6,6,6,5,6,6,6,5,5,6,6,5,5,5,5,5,5,5,5,4,5,5),  
        (5,4,5,5,5,4,4,5,5,4,4,4,4,4,4,4,4,3,4,4,4,3,3,4,4,3,3,3),  
        (6,6,6,7,6,6,6,6,5,6,6,6,5,5,6,6,5,5,5,6,5,5,5,5,4,5,5,5,5),
        (5,5,6,6,5,5,5,6,5,5,5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,4,4,5),
        (6,6,6,7,6,6,6,6,5,6,6,6,5,5,6,6,5,5,5,6,5,5,5,5,4,5,5,5,5),
        (6,6,7,7,6,6,6,7,6,6,6,6,5,6,6,6,5,5,6,6,5,5,5,6,5,5,5,5,4,5,5,5,5),
        (7,8,8,8,7,7,8,8,7,7,7,8,7,7,7,7,6,7,7,7,6,6,7,7,6,6,6,7,7),
        (8,8,8,9,8,8,8,8,7,8,8,8,7,7,8,8,7,7,7,8,7,7,7,7,6,7,7,7,6,6,7,7,7),
        (8,8,8,9,8,8,8,8,7,8,8,8,7,7,8,8,7,7,7,8,7,7,7,7,6,7,7,7,7),
        (9,9,9,9,8,9,9,9,8,8,9,9,8,8,8,9,8,8,8,8,7,8,8,8,7,7,8,8,8),
        (8,8,8,8,7,8,8,8,7,7,8,8,7,7,7,8,7,7,7,7,6,7,7,7,6,6,7,7,7),
        (7,8,8,8,7,7,8,8,7,7,7,8,7,7,7,7,6,7,7,7,6,6,7,7,6,6,6,7,7))
    sectionalTermYear = (
        (),
        (13, 49, 85, 117, 149, 185, 201, 250, 250),
        (13, 45, 81, 117, 149, 185, 201, 250, 250),
        (13, 48, 84, 112, 148, 184, 200, 201, 250),
        (13, 45, 76, 108, 140, 172, 200, 201, 250),
        (13, 44, 72, 104, 132, 168, 200, 201, 250),
        ( 5, 33, 68,  96, 124, 152, 188, 200, 201),
        (29, 57, 85, 120, 148, 176, 200, 201, 250),
        (13, 48, 76, 104, 132, 168, 196, 200, 201),
        (25, 60, 88, 120, 148, 184, 200, 201, 250),
        (16, 44, 76, 108, 144, 172, 200, 201, 250),
        (28, 60, 92, 124, 160, 192, 200, 201, 250),
        (17, 53, 85, 124, 156, 188, 200, 201, 250))
    principleTermMap = (
        (),
        (21, 21, 21, 21, 21, 20, 21, 21, 21, 20, 20, 21, 21, 20, 20, 20,
         20, 20, 20, 20, 20, 19, 20, 20, 20, 19, 19, 20),
        (20, 19, 19, 20, 20, 19, 19, 19, 19, 19, 19, 19, 19, 18, 19, 19,
         19, 18, 18, 19, 19, 18, 18, 18, 18, 18, 18, 18),
        (21, 21, 21, 22, 21, 21, 21, 21, 20, 21, 21, 21, 20, 20, 21, 21,
         20, 20, 20, 21, 20, 20, 20, 20, 19, 20, 20, 20, 20),
        (20, 21, 21, 21, 20, 20, 21, 21, 20, 20, 20, 21, 20, 20, 20, 20,
         19, 20, 20, 20, 19, 19, 20, 20, 19, 19, 19, 20, 20),
        (21, 22, 22, 22, 21, 21, 22, 22, 21, 21, 21, 22, 21, 21, 21, 21,
         20, 21, 21, 21, 20, 20, 21, 21, 20, 20, 20, 21, 21),
        (22, 22, 22, 22, 21, 22, 22, 22, 21, 21, 22, 22, 21, 21, 21, 22,
         21, 21, 21, 21, 20, 21, 21, 21, 20, 20, 21, 21, 21),
        (23, 23, 24, 24, 23, 23, 23, 24, 23, 23, 23, 23, 22, 23, 23, 23,
         22, 22, 23, 23, 22, 22, 22, 23, 22, 22, 22, 22, 23),
        (23, 24, 24, 24, 23, 23, 24, 24, 23, 23, 23, 24, 23, 23, 23, 23,
         22, 23, 23, 23, 22, 22, 23, 23, 22, 22, 22, 23, 23),
        (23, 24, 24, 24, 23, 23, 24, 24, 23, 23, 23, 24, 23, 23, 23, 23,
         22, 23, 23, 23, 22, 22, 23, 23, 22, 22, 22, 23, 23),
        (24, 24, 24, 24, 23, 24, 24, 24, 23, 23, 24, 24, 23, 23, 23, 24,
         23, 23, 23, 23, 22, 23, 23, 23, 22, 22, 23, 23, 23),
        (23, 23, 23, 23, 22, 23, 23, 23, 22, 22, 23, 23, 22, 22, 22, 23,
         22, 22, 22, 22, 21, 22, 22, 22, 21, 21, 22, 22, 22),
        (22, 22, 23, 23, 22, 22, 22, 23, 22, 22, 22, 22, 21, 22, 22, 22,
         21, 21, 22, 22, 21, 21, 21, 22, 21, 21, 21, 21, 22))
    principleTermYear = (
        (),
        (13, 45, 81, 113, 149, 185, 201),     
        (21, 57, 93, 125, 161, 193, 201),     
        (21, 56, 88, 120, 152, 188, 200, 201), 
        (21, 49, 81, 116, 144, 176, 200, 201), 
        (17, 49, 77, 112, 140, 168, 200, 201), 
        (28, 60, 88, 116, 148, 180, 200, 201), 
        (25, 53, 84, 112, 144, 172, 200, 201), 
        (29, 57, 89, 120, 148, 180, 200, 201), 
        (17, 45, 73, 108, 140, 168, 200, 201), 
        (28, 60, 92, 124, 160, 192, 200, 201), 
        (16, 44, 80, 112, 148, 180, 200, 201), 
        (17, 53, 88, 120, 156, 188, 200, 201))
    lunarMonthNames = (
        '', '正', '二', '三', '四', '五', '六', '七', '八', '九', '十',
        '冬', '腊')
    lunarDayNames = (
        '',     '初一', '初二', '初三', '初四', '初五', '初六', '初七',
        '初八', '初九', '初十', '十一', '十二', '十三', '十四', '十五',
        '十六', '十七', '十八', '十九', '廿十', '廿一', '廿二', '廿三',
        '廿四', '廿五', '廿六', '廿七', '廿八', '廿九', '三十')
    principleTermNames = (
        '',     '大寒', '雨水', '春分', '谷雨', '夏满', '夏至', '大暑',
        '处暑', '秋分', '霜降', '小雪', '冬至')
    sectionalTermNames = (
        '',     '小寒', '立春', '惊蛰', '清明', '立夏', '芒种', '小暑',
        '立秋', '白露', '寒露', '立冬', '大雪')
    # 公历中定义的节日
    # 以`d'开头, 表示根据月份日期来计算, 后面的数字表示月份和日期
    # 以`w'开头的, 表示某个月的第几周, 比如w0520表示:
    # 第(05)月第(2)周的星期日(0), 0-6表示周日到周六
    # 以`y'开头的, 表示本年的第多少天, 后面有3位数字,  比如y256表示第256天.
    solarHolidays = {
        'd0101': '元旦',
        'd0202': '世界湿地日',
        'd0210': '国际气象节',
        'd0214': '情人节',
        'd0303': '全国爱耳日',
        'd0308': '妇女节',
        'd0309': '保护母亲河日',
        'd0312': '植树节',
        'd0314': '国际警察日',
        'd0315': '国际消费者权益日',
        'd0322': '世界水日',
        'd0401': '愚人节',
        'd0404': '寒食节', #清明节的前一天'
        'd0407': '世界卫生日',
        'd0422': '世界地球日',
        'd0426': '世界知识产权日',
        'd0501': '劳动节',
        'd0503': '世界新闻自由日',
        'w0520': '母亲节',
        'd0504': '青年节',
        'd0507': '世界电信和信息社会日',
        'd0512': '护士节',
        'w0530': '全国助残日',
        'd0531': '世界无烟日',
        'd0601': '儿童节',
        'd0605': '世界环境日',
        'd0606': '全国爱眼日',
        'w0630': '父亲节',
        'd0707': '中国人民抗日战争纪念日',
        'd0711': '世界人口日',
        'd0801': '建军节',
        'd0808': '中国爸爸节',
        'd0812': '国际青年日',
        'd0903': '抗日战争胜利纪念日',
        'd0908': '国际扫盲日',
        'd0910': '教师节',
        'y256':  '程序员节', # 每年的第256天
        'd0916': '中国脑健康日',
        'd0918': '国耻日',
        'd0919': '国际和平日',
        'w0936': '国防教育日',
        'd0920': '全国爱牙日',
        'd1001': '国庆节',
        'd1008': '全国高血压日',
        'd1028': '中国男性键康日',
        'd1031': '万圣节',
        'd1109': '消防宣传日',
        'd1111': '光棍节',
        'd1201': '世界艾滋病日',
        'd1205': '国际志愿者日',
        'd1210': '国际人权日',
        'd1225': '圣诞节',
        }
    lunarHolidays = {
        'd0101': '春节',
        'd0115': '元宵节',
        'd0202': '春龙节',
        'd0505': '端午节',
        'd0606': '天贶节',
        'd0707': '七夕节',
        'd0715': '中元节',
        'd0815': '中秋节',
        'd0909': '重阳节',
        'd1001': '祭祖节',
        'd1208': '腊八节',
        'd1223': '小年',
        'd1224': '扫房日',
        'd1230': '除夕'
        }

    # 第一个对应日
    # 公历1901年1月1日, 对应农历4598年11月11日
    baseYear = 1901
    baseMonth = 1
    baseDay = 1
    baseIndex = 0
    baseLunarYear = 4598 - 1
    baseLunarMonth = 11
    baseLunarDay = 11

    def __init__(self, year=1901, month=1, day=1):
        if year < 1901 or year > 2100:
            raise ValueError('year is out of range')
        self.setGregorian(year, month, day)

    def __str__(self):
        return ''.join([
            'Gregorian Year: ', str(self.gregorianYear), '\n',
            'Gregorian Month: ', str(self.gregorianMonth), '\n',
            'Gregorian Day: ', str(self.gregorianDay), '\n',
            'Is Leap Year: ', str(self.isGregLeap), '\n',
            'Day Of Year: ', str(self.dayOfYear), '\n',
            'Day of Week: ', str(self.dayOfWeek), '\n',
            'Lunar Year: ', str(self.lunarYear), '\n',
            'Heavenly-Sterm: ', str(self.heavenlySterm), '\n',
            'Earthly-Branch: ', str(self.earthlyBranch), '\n',
            'Lunar Month: ', str(self.lunarMonth), '\n',
            'Lunar Day: ', str(self.lunarDay), '\n',
            'Sectional Term: ', str(self.sectionalTerm), '\n',
            'Principle Term: ', str(self.principleTerm), '\n',
            ])

    def setGregorian(self, year, month, day):
        self.gregorianYear = year
        self.gregorianMonth = month
        self.gregorianDay = day
        self.isGregLeap = self.isGregorianLeapYear(year)
        self.dayOfYear = self.getDayOfYear(year, month, day)
        self.weekOfMonth = self.getWeekOfMonth(year, month, day)
        self.dayOfWeek = self.getDayOfWeek(year, month, day)
        self.lunarYear = 0
        self.lunarMonth = 0
        self.lunarDay = 0
        self.sectionalTerm = 0
        self.principleTerm = 0
        self.heavenlySterm = 0
        self.earthlyBranch = 0

        self.calcLunarFields()
        self.calcSolarTerms()
        self.calcStermAndBranch()

    def getCalendar(self):
        return {
            'gregorianYear': self.gregorianYear,
            'gregorianMonth': self.gregorianMonth,
            'gregorianDay': self.gregorianDay,
            'isGregLeap': self.isGregLeap,
            'dayOfYear': self.dayOfYear,
            'weekOfMonth': self.weekOfMonth,
            'dayOfWeek': self.dayOfWeek,
            'lunarYear': self.lunarYear,
            'lunarMonth': self.getLunarMonth(),
            'lunarDay': self.getLunarDay(),
            'stermBranch': self.getStermBranch(),
            'animalZodiac': self.getAnimalZodiac(),
            'solarHoliday': self.getSolarHoliday(),
            'lunarHoliday': self.getLunarHoliday(),
            }

    def getLunarMonth(self):
        return self.lunarMonthNames[self.lunarMonth] + '月'

    def getLunarDay(self):
        print('lunar day: ', self.lunarDay)
        return self.lunarDayNames[self.lunarDay]

    def getSolarHoliday(self):
        '''得到公历中的假日

        一天可能是多个假日.
        '''
        w = 'w{0:02}{1}{2}'.format(
                self.gregorianMonth, self.weekOfMonth, self.dayOfWeek)
        d = 'd{0:02}{1:02}'.format(self.gregorianMonth, self.gregorianDay)
        y = 'y{0:03}'.format(self.dayOfYear)
        result = []
        if w in self.solarHolidays:
            result.append(self.solarHolidays[w])
        if d in self.solarHolidays:
            result.append(self.solarHolidays[d])
        if y in self.solarHolidays:
            result.append(self.solarHolidays[y])
        if result:
            return '\n'.join(result)
        return ''

    def getLunarHoliday(self):
        '''得到农历中的假日'''
        d = 'd{0:02}{1:02}'.format(self.lunarMonth, self.lunarDay)
        if d in self.lunarHolidays:
            return self.lunarHolidays[d]
        return ''

    def getStermBranch(self):
        '''得到本年的岁名.

        农历中的天干地支, 每六十年就是一个轮回.
        '''
        return (self.heavenlySterms[self.heavenlySterm] +
                self.earthlyBranches[self.earthlyBranch])

    def getAnimalZodiac(self):
        '''得到本年的十二生肖名.

        十二生肖是根据地支来计算的, 每隔十二年一个轮回.
        '''
        return self.animalZodiac[self.earthlyBranch]

    def getSolarTerm(self):
        '''得到节气名.

        如果这一天不是二十四节气中的一天, 就返回''.
        '''
        if self.gregorianDay == self.principleTerm:
            return self.principleTermNames[self.gregorianMonth]
        elif self.gregorianDay == self.sectionalTerm:
            return self.sectionalTermNames[self.gregorianMonth]
        else:
            return ''


    def isGregorianLeapYear(self, year):
        '''计算公历闰年

        公历中, 每4年会比天文年多出一天, 所以会每隔4年出现一闰年.
        在闰年里, 2月会有29天.
        '''
        is_leap = False
        if year % 4 == 0:
            is_leap = True
        if year % 100 == 0:
            is_leap = False
        if year % 400 == 0:
            is_leap = True
        return is_leap

    def getDayOfYear(self, year, month, day):
        '''确定某天是本年的第多少天'''
        count = day
        for m in range(1, month + 1):
            count = count + self.daysInGregorianMonth(year, m)
        return count

    def getWeekOfMonth(self, year, month, day):
        '''确定某天是本月中的第几周'''
        return (day - 1) // 7 + 1

    def getDayOfWeek(self, year, month, day):
        '''确定某天是周几

        以周日为一周的第一天, 从0开始计数
        '''
        week = 0
        y = (year - 1) % 400 + 1  # 400年循环一次
        leaps = (y - 1) // 4  + (y - 1) // 100  + (y - 1) // 400  # 闰年次数
        commons = y - 1 - leaps  # 平年次数
        week = week + commons + 2 * leaps # 星期在平年加1, 在闰年加2.
        week = week + self.getDayOfYear(y, month, day)
        week = (week - 1) % 7
        return week
        #date = datetime.date(year, month, day)
        #return date.weekday()

    def daysInGregorianMonth(self, year, month):
        '''确定公历中某年的某个月有多少天, 这里会计算闰年的'''
        days = self.gregorianDays[month]
        if month == 2 and self.isGregLeap:
            days = days + 1
        return days

    def daysInLunarMonth(self, year, month):
        '''计算农历中某年的某个月有几天
        
        在农历闰月中, lunarMonth < 0
        '''
        index = year - self.baseLunarYear + self.baseIndex
        v = 0
        l = 0
        d = 30
        if 1 <= month <= 8:
            v = self.lunarMonths[2 * index]
            l = month - 1
            if ((v >> l) & 0x01) == 1:
                d = 29
        elif 9 <= month <= 12:
            v = self.lunarMonths[2 * index + 1]
            l = month - 9
            if ((v >> l) & 0x01) == 1:
                d = 29
        else:
            v = self.lunarMonths[2 * index + 1]
            v = (v >> 4) & 0x0F
            if v != abs(month):
                d = 0
            else:
                d = 29
                for item in self.bigLeapMonthYears:
                    if item == index:
                        d = 30
                        break
        return d

    def nextLunarMonth(self, year, month):
        n = abs(month) + 1
        if month > 0:
            index = year - self.baseLunarYear + self.baseIndex
            v = self.lunarMonths[2 * index + 1]
            v = (v >> 4) & 0x0F
            if v == month:
                n = 0 - month
        if n == 13:
            n = 1
        return n

    def calcLunarFields(self):
        startYear = self.baseYear
        startMonth = self.baseMonth
        startDay = self.baseDay
        self.lunarYear = self.baseLunarYear
        self.lunarMonth = self.baseLunarMonth
        self.lunarDay = self.baseLunarDay

        if self.gregorianYear >= 2014:
            startYear = self.baseYear + 113
            startMonth = 1
            startDay = 1
            self.lunarYear = self.baseLunarYear + 113
            self.lunarMonth = 12
            self.lunarDay = 1

        # 第二个对应日, 用以提高计算效率
        # 公历2000年1月1日, 对应于4697年11月25日
        elif self.gregorianYear >= 2000:
            startYear = self.baseYear + 99
            startMonth = 1
            startDay = 1
            self.lunarYear = self.baseLunarYear + 99
            self.lunarMonth = 11
            self.lunarDay = 25
#        start_date = datetime.date(startYear, startMonth, startDay)
#        end_date = datetime.date(
#                self.gregorianYear, self.gregorianMonth, self.gregorianDay)
#        date_delta = (end_date - start_date).days
        date_delta = 0
        for y in range(startYear, self.gregorianYear):
            date_delta += 365
            if self.isGregorianLeapYear(y):
                date_delta += 1
        for m in range(startMonth, self.gregorianMonth):
            date_delta = date_delta + self.daysInGregorianMonth(
                    self.gregorianYear, m)
        date_delta = date_delta + self.gregorianDay - startDay

        
        self.lunarDay = self.lunarDay + date_delta
        last_day = self.daysInLunarMonth(self.lunarYear, self.lunarMonth)
        next_month = self.nextLunarMonth(self.lunarYear, self.lunarMonth)

        while self.lunarDay > last_day:
            if abs(next_month) < abs(self.lunarMonth):
                self.lunarYear = self.lunarYear + 1
            self.lunarMonth = next_month
            self.lunarDay = self.lunarDay - last_day
            last_day = self.daysInLunarMonth(self.lunarYear, self.lunarMonth)
            next_month = self.nextLunarMonth(self.lunarYear, self.lunarMonth)

    def calcSolarTerms(self):
        self.sectionalTerm = self.getSectionalTerm(
                self.gregorianYear, self.gregorianMonth)
        self.principleTerm = self.getPrincipleTerm(
                self.gregorianYear, self.gregorianMonth)

    def getSectionalTerm(self, year, month):
        index = 0
        ry = year - self.baseYear + 1
        while ry > self.sectionalTermYear[month][index]:
            index = index + 1
        term = self.sectionalTermMap[month][4 * index + ry % 4]
        if ry == 121 and month == 4:
            term = 5
        elif ry == 132 and month == 4:
            term = 5
        elif ry == 194 and month == 6:
            term = 6
        return term

    def getPrincipleTerm(self, year, month):
        index = 0
        ry = year - self.baseYear + 1
        while ry >= self.principleTermYear[month][index]:
            index = index + 1
        term = self.principleTermMap[month][4 * index + ry % 4]
        if ry == 171 and month == 3:
            term = 21
        elif ry == 181 and month == 5:
            term = 21
        return term

    def calcStermAndBranch(self):
        self.heavenlySterm = (self.lunarYear - 1) % 10
        self.earthlyBranch = (self.lunarYear - 1) % 12
