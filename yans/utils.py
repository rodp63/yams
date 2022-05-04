from datetime import date, datetime, timedelta


def str_to_date(str_date):
    return datetime.strptime(str_date, "%Y-%m-%d").date()


def date_range(start_date, end_date, inclusive=False):
    start_date = str_to_date(start_date)
    end_date = str_to_date(end_date)
    for n in range(int((end_date - start_date).days) + int(inclusive)):
        yield start_date + timedelta(n)


def today(to_str=False):
    return str(date.today()) if to_str else date.today()
