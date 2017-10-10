# coding=UTF-8

import sys
import datetime
import unittest
sys.path.append("..")
from utils.calendar import Calendar

class TestCalendarMethods(unittest.TestCase):

    def test_generate(self):
        self.assertRaises(TypeError, Calendar.generate, "")

        calendar = Calendar.generate(
            datetime.datetime.strptime("2016071403", "%Y%m%d%H"))

        calendar = Calendar.generate(
            datetime.datetime.strptime("2016050112", "%Y%m%d%H"))
        

        self.assertEqual(calendar["CUR_DATE"], "20160501")
        self.assertEqual(calendar["CUR_YEAR"], "2016")
        self.assertEqual(calendar["CUR_MONTH"], "05")
        self.assertEqual(calendar["CUR_DAY"], "01")
        self.assertEqual(calendar["CUR_HOUR"], "12")
        self.assertEqual(calendar["CUR_DATEHOUR"], "2016050112")

        self.assertEqual(calendar["THREE_HOURS_AGO_DATE"], "20160501")
        self.assertEqual(calendar["THREE_HOURS_AGO_YEAR"], "2016")
        self.assertEqual(calendar["THREE_HOURS_AGO_MONTH"], "05")
        self.assertEqual(calendar["THREE_HOURS_AGO_DAY"], "01")
        self.assertEqual(calendar["THREE_HOURS_AGO_HOUR"], "09")
        self.assertEqual(calendar["THREE_HOURS_AGO_DATEHOUR"], "2016050109")

        self.assertEqual(calendar["ONE_DAY_AGO_DATE"], "20160430")
        self.assertEqual(calendar["ONE_DAY_AGO_YEAR"], "2016")
        self.assertEqual(calendar["ONE_DAY_AGO_MONTH"], "04")
        self.assertEqual(calendar["ONE_DAY_AGO_DAY"], "30")
        self.assertEqual(calendar["ONE_DAY_AGO_HOUR"], "12")
        self.assertEqual(calendar["ONE_DAY_AGO_DATEHOUR"], "2016043012")

        self.assertEqual(calendar["TWO_DAYS_AGO_DATE"], "20160429")
        self.assertEqual(calendar["TWO_DAYS_AGO_YEAR"], "2016")
        self.assertEqual(calendar["TWO_DAYS_AGO_MONTH"], "04")
        self.assertEqual(calendar["TWO_DAYS_AGO_DAY"], "29")
        self.assertEqual(calendar["TWO_DAYS_AGO_HOUR"], "12")
        self.assertEqual(calendar["TWO_DAYS_AGO_DATEHOUR"], "2016042912")

        self.assertEqual(calendar["ONE_HOUR_LATER_DATE"], "20160501")
        self.assertEqual(calendar["ONE_HOUR_LATER_YEAR"], "2016")
        self.assertEqual(calendar["ONE_HOUR_LATER_MONTH"], "05")
        self.assertEqual(calendar["ONE_HOUR_LATER_DAY"], "01")
        self.assertEqual(calendar["ONE_HOUR_LATER_HOUR"], "13")
        self.assertEqual(calendar["ONE_HOUR_LATER_DATEHOUR"], "2016050113")


        self.assertEqual(calendar["ONE_DAY_LATER_DATE"], "20160502")
        self.assertEqual(calendar["ONE_DAY_LATER_YEAR"], "2016")
        self.assertEqual(calendar["ONE_DAY_LATER_MONTH"], "05")
        self.assertEqual(calendar["ONE_DAY_LATER_DAY"], "02")
        self.assertEqual(calendar["ONE_DAY_LATER_HOUR"], "12")
        self.assertEqual(calendar["ONE_DAY_LATER_DATEHOUR"], "2016050212")


if __name__ == '__main__':
    unittest.main()