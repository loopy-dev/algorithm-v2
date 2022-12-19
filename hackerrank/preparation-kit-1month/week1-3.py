"""
Time Conversion
Given a time in 12-hour AM/PM format, convert it to military(24 hour) time.

example:
s = '12:01:00PM'
return '12:01:00'
"""


def timeConversion(s):
    """
    1. 우선 공통적이지 않은 부분부터 떼어낸다. -> AM, PM
    2. 떼어낸 뒤 남은 글자들을 ':'로 split 하여 숫자를 분리한다.
    3. 시간을 12로 나눈 나머지를 구한다. 그리고 PM이라면 그 숫자에 12를 더하면 된다.
    """
    am_pm_format = s[-2:]
    s = s[:-2]
    offset = 12 if am_pm_format == "PM" else 0

    # get time
    time = list(map(int, s.split(":")))

    # add offset
    time[0] = (time[0] % 12) + offset

    # int형을 str형으로 바꿔주면서, 포맷 형식에 맞게끔 정리한다.
    return ":".join(list(map(lambda x: format(x, "02"), time)))


s = "12:01:00AM"
print(timeConversion(s))
