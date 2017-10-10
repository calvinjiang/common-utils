# coding=UTF-8

import datetime


class Calendar:

    @classmethod
    def generate(cls, current_datetime=None, seperate_char=None):

        if seperate_char is None:
            seperate_char = ''
            date_formatter = "%%Y%s%%m%s%%d" % (seperate_char, seperate_char)
            date_hour_formatter = "%Y%m%d%H"
        else:
            date_formatter = "%%Y%s%%m%s%%d" % (seperate_char, seperate_char)
            date_hour_formatter = "%%Y%s%%m%s%%d %%H:00:00" % (
                seperate_char, seperate_char)

        if current_datetime is None:
            current_datetime = datetime.datetime.now()
        elif not isinstance(current_datetime, datetime.datetime):
            raise TypeError("the argument must be datetime type.")

        three_hours_ago_datetime = current_datetime - \
            datetime.timedelta(hours=3)
        one_day_ago_datetime = current_datetime - datetime.timedelta(days=1)
        two_days_ago_datetime = current_datetime - datetime.timedelta(days=2)
        one_hour_later_datetime = current_datetime + \
            datetime.timedelta(hours=1)
        one_day_later_datetime = current_datetime + datetime.timedelta(days=1)

        CUR_DATE = current_datetime.strftime(date_formatter)
        CUR_YEAR = current_datetime.strftime("%Y")
        CUR_MONTH = current_datetime.strftime("%m")
        CUR_DAY = current_datetime.strftime("%d")
        CUR_HOUR = current_datetime.strftime("%H")

        CUR_DATEHOUR = current_datetime.strftime(date_hour_formatter)

        calendar = {}
        calendar["CUR_DATE"] = CUR_DATE
        calendar["CUR_YEAR"] = CUR_YEAR
        calendar["CUR_MONTH"] = CUR_MONTH
        calendar["CUR_DAY"] = CUR_DAY
        calendar["CUR_HOUR"] = CUR_HOUR
        calendar["CUR_DATEHOUR"] = CUR_DATEHOUR

        THREE_HOURS_AGO_DATE = three_hours_ago_datetime.strftime(
            date_formatter)
        THREE_HOURS_AGO_YEAR = three_hours_ago_datetime.strftime("%Y")
        THREE_HOURS_AGO_MONTH = three_hours_ago_datetime.strftime("%m")
        THREE_HOURS_AGO_DAY = three_hours_ago_datetime.strftime("%d")
        THREE_HOURS_AGO_HOUR = three_hours_ago_datetime.strftime("%H")


        THREE_HOURS_AGO_DATEHOUR = three_hours_ago_datetime.strftime(date_hour_formatter)

        calendar["THREE_HOURS_AGO_DATE"] = THREE_HOURS_AGO_DATE
        calendar["THREE_HOURS_AGO_YEAR"] = THREE_HOURS_AGO_YEAR
        calendar["THREE_HOURS_AGO_MONTH"] = THREE_HOURS_AGO_MONTH
        calendar["THREE_HOURS_AGO_DAY"] = THREE_HOURS_AGO_DAY
        calendar["THREE_HOURS_AGO_HOUR"] = THREE_HOURS_AGO_HOUR
        calendar["THREE_HOURS_AGO_DATEHOUR"] = THREE_HOURS_AGO_DATEHOUR

        ONE_DAY_AGO_DATE = one_day_ago_datetime.strftime(date_formatter)
        ONE_DAY_AGO_YEAR = one_day_ago_datetime.strftime("%Y")
        ONE_DAY_AGO_MONTH = one_day_ago_datetime.strftime("%m")
        ONE_DAY_AGO_DAY = one_day_ago_datetime.strftime("%d")
        ONE_DAY_AGO_HOUR = one_day_ago_datetime.strftime("%H")
        ONE_DAY_AGO_DATEHOUR = one_day_ago_datetime.strftime(date_hour_formatter)

        calendar["ONE_DAY_AGO_DATE"] = ONE_DAY_AGO_DATE
        calendar["ONE_DAY_AGO_YEAR"] = ONE_DAY_AGO_YEAR
        calendar["ONE_DAY_AGO_MONTH"] = ONE_DAY_AGO_MONTH
        calendar["ONE_DAY_AGO_DAY"] = ONE_DAY_AGO_DAY
        calendar["ONE_DAY_AGO_HOUR"] = ONE_DAY_AGO_HOUR
        calendar["ONE_DAY_AGO_DATEHOUR"] = ONE_DAY_AGO_DATEHOUR

        TWO_DAYS_AGO_DATE = two_days_ago_datetime.strftime(date_formatter)
        TWO_DAYS_AGO_YEAR = two_days_ago_datetime.strftime("%Y")
        TWO_DAYS_AGO_MONTH = two_days_ago_datetime.strftime("%m")
        TWO_DAYS_AGO_DAY = two_days_ago_datetime.strftime("%d")
        TWO_DAYS_AGO_HOUR = two_days_ago_datetime.strftime("%H")
        TWO_DAYS_AGO_DATEHOUR = two_days_ago_datetime.strftime(date_hour_formatter)

        calendar["TWO_DAYS_AGO_DATE"] = TWO_DAYS_AGO_DATE
        calendar["TWO_DAYS_AGO_YEAR"] = TWO_DAYS_AGO_YEAR
        calendar["TWO_DAYS_AGO_MONTH"] = TWO_DAYS_AGO_MONTH
        calendar["TWO_DAYS_AGO_DAY"] = TWO_DAYS_AGO_DAY
        calendar["TWO_DAYS_AGO_HOUR"] = TWO_DAYS_AGO_HOUR
        calendar["TWO_DAYS_AGO_DATEHOUR"] = TWO_DAYS_AGO_DATEHOUR

        ONE_HOUR_LATER_DATE = one_hour_later_datetime.strftime(date_formatter)
        ONE_HOUR_LATER_YEAR = one_hour_later_datetime.strftime("%Y")
        ONE_HOUR_LATER_MONTH = one_hour_later_datetime.strftime("%m")
        ONE_HOUR_LATER_DAY = one_hour_later_datetime.strftime("%d")
        ONE_HOUR_LATER_HOUR = one_hour_later_datetime.strftime("%H")
        ONE_HOUR_LATER_DATEHOUR = one_hour_later_datetime.strftime(date_hour_formatter)

        calendar["ONE_HOUR_LATER_DATE"] = ONE_HOUR_LATER_DATE
        calendar["ONE_HOUR_LATER_YEAR"] = ONE_HOUR_LATER_YEAR
        calendar["ONE_HOUR_LATER_MONTH"] = ONE_HOUR_LATER_MONTH
        calendar["ONE_HOUR_LATER_DAY"] = ONE_HOUR_LATER_DAY
        calendar["ONE_HOUR_LATER_HOUR"] = ONE_HOUR_LATER_HOUR
        calendar["ONE_HOUR_LATER_DATEHOUR"] = ONE_HOUR_LATER_DATEHOUR

        ONE_DAY_LATER_DATE = one_day_later_datetime.strftime(date_formatter)
        ONE_DAY_LATER_YEAR = one_day_later_datetime.strftime("%Y")
        ONE_DAY_LATER_MONTH = one_day_later_datetime.strftime("%m")
        ONE_DAY_LATER_DAY = one_day_later_datetime.strftime("%d")
        ONE_DAY_LATER_HOUR = one_day_later_datetime.strftime("%H")
        ONE_DAY_LATER_DATEHOUR = one_day_later_datetime.strftime(date_hour_formatter)

        calendar["ONE_DAY_LATER_DATE"] = ONE_DAY_LATER_DATE
        calendar["ONE_DAY_LATER_YEAR"] = ONE_DAY_LATER_YEAR
        calendar["ONE_DAY_LATER_MONTH"] = ONE_DAY_LATER_MONTH
        calendar["ONE_DAY_LATER_DAY"] = ONE_DAY_LATER_DAY
        calendar["ONE_DAY_LATER_HOUR"] = ONE_DAY_LATER_HOUR
        calendar["ONE_DAY_LATER_DATEHOUR"] = ONE_DAY_LATER_DATEHOUR

        return calendar
