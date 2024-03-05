import re
import string


def timeConversion(s):
    am_pm = s[-2:]
    hour = s[:-2].split(':')[0]
    min = s[:-2].split(':')[1]
    sec = s[:-2].split(':')[2]
    if hour == '12' and am_pm == 'AM':
        hour = '00'
    elif hour == '12' and am_pm == 'PM':
        hour = '12'
    else:
        if am_pm == 'PM':
            hour = str(int(hour) + 12)
    return_time = hour + ':' + min + ':' + sec
    return return_time


if __name__ == '__main__':
    input = '07:05:45PM'
    assert timeConversion(input) == '19:05:45'

    input = '12:00:00AM'
    assert timeConversion(input) == '00:00:00'

    input = '12:40:22AM'
    assert timeConversion(input) == '00:40:22'

    input = '12:00:00PM'
    assert timeConversion(input) == '12:00:00'

    input = '01:00:01AM'
    assert timeConversion(input) == '01:00:01'

    input = '12:00:01PM'
    assert timeConversion(input) == '12:00:01'
