import sys
sys.path.append('/workspaces/21178063/seasons/')
import pytest
#from freezegun import freeze_time
#from seasons import print_say_age_in_minutes, Minutes, get_minutes
from seasons import get_minutes
from datetime import date


#def test_incorrect():
#    with pytest.raises(SystemExit) as excinfo:
#        my_date = Minutes('January 1, 1999')  # Invalid day
#    assert excinfo.type == SystemExit
#    assert excinfo.value.code == "Invalid Date"

def test_get_incorrect_format():
    with pytest.raises(SystemExit):
        assert get_minutes('January 1, 1999')

#@freeze_time("2000-01-01")
def test_for_1999():
    birthday = "1999-01-01"
    when_today_is = date.fromisoformat('2000-01-01')
   # get_minutes(birthday, when_today_is)   == "Five hundred twenty-five thousand, six hundred minutes"
    get_minutes(birthday) == "Thirteen million, seven hundred twenty-six thousand eighty minutes"
'''
#@freeze_time("2023-01-01")
def test_for_20023():
    birthday = "2001-01-01"
    when_today_is = date.fromisoformat('2023-01-01')
    get_minutes(birthday,when_today_is) == "One million, fifty-one thousand, two hundred minutes"
    get_minutes(birthday) == "Twelve million, six hundred seventy-three thousand, four hundred forty minutes"

#@freeze_time("1995-01-01")
def test_for_1995():
    birthday = "2001-01-01"
    when_today_is = date.fromisoformat('1995-01-01')
    get_minutes(birthday,when_today_is) == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"
    get_minutes(birthday) == "Twelve million, six hundred seventy-three thousand, four hundred forty minutes"

#@freeze_time("2032-01-01")
def test_for_2032():
    birthday = "2020-06-01"
    when_today_is = date.fromisoformat('2032-01-01')
    get_minutes(birthday,when_today_is) ==  "Six million, ninety-two thousand, six hundred forty minutes"
    get_minutes(birthday) ==  "Two million, four hundred sixty-two thousand, four hundred minutes"

#@freeze_time("2000-01-01")
def test_for_2032():
    birthday = "1998-06-20"
    when_today_is = date.fromisoformat('2000-01-01')
    get_minutes(birthday,when_today_is) == "Eight hundred six thousand, four hundred minutes"
    get_minutes(birthday) == "Fourteen million, six thousand, eight hundred eighty minutes"

if __name__ == "__main__":
    pytest.main()
'''
