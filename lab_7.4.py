def create_calendar_page(month=None, year=None):
    import calendar
    import datetime
    x = '--------------------\nMO TU WE TH FR SA SU\n--------------------\n'
    today = datetime.datetime.today()
    month = month or today.month
    year  = year or today.year
    a = calendar.TextCalendar()
    b = a.formatmonth(year, month)

    b = b[b.find('\n') + 1:]
    b = x + b[b.find('\n') + 1:]
    b = b[:len(b) - 1]
    string = ''
    for i in range(len(b)):
        if i < len(b) - 2:
            if (b[i] == ' ' and b[i + 1].isdigit() and b[i + 2] == ' ') or (b[i] == ' ' and b[i + 1].isdigit() and b[i + 2] == '\n'):
                string = string + "0"
            else:
                string += b[i]
        else:
            string += b[i]
    return string


print(create_calendar_page(1))
print(create_calendar_page())
print(create_calendar_page(3))
print(create_calendar_page(7, 1979))