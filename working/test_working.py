import sys

sys.path.append('/workspaces/21178063/working')

from working import convert
import pytest

def main():
    test_nice_format()
    test_without_minute()
    test_mixed_format()
    test_printing_hours_off_by_one()
    test_printing_minutes_off_by_five()
    test_invalid()
    test_PM_AM_no_space()

def test_nice_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_without_minute():
    assert convert("9 AM to 5 PM")         == "09:00 to 17:00"

def test_mixed_format():
    assert convert("9:00 AM to 5 PM")      == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM")      == "09:00 to 17:00"
    assert convert("8 PM to 8 AM")         == "20:00 to 08:00"
    assert convert("8:00 PM to 8:00 AM")   == "20:00 to 08:00"
    assert convert("12 AM to 12 PM")       == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("10 AM to 8:50 PM")     == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM")     == "22:30 to 08:00"

def test_printing_hours_off_by_one():
    assert convert("10:40 PM to 11:40 PM")     == "22:40 to 23:40"

def test_printing_minutes_off_by_five():
    assert convert("10:30 PM to 10:35 PM")     == "22:30 to 22:35"


def test_invalid():
    #with pytest.raises(ValueError, match="Invalid time range format"):
    with pytest.raises(ValueError):
        convert('CS50 Cat')

def test_PM_AM_no_space():
    #with pytest.raises(ValueError, match="Invalid time range format"):
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
        convert("8:60 AM to 4:60 PM")
        convert("9:60 AM to 5:60 PM")
        convert("09:00 to 17:00")
        convert("9 AM - 5 PM")
        convert("10:7 AM - 5:1 PM")
        convert("9 AM - 5 PM")

def test_when_user_omits_to():
    #with pytest.raises(ValueError, match="Invalid time range format"):
    with pytest.raises(ValueError):
        convert("9AM 5PM")
def test_out_of_range_times():
    #with pytest.raises(ValueError, match="Invalid time range format"):
    with pytest.raises(ValueError):
        convert("13:00 AM to 14:00 PM")

if __name__ == "__main__":
    main()
    #exit_code = pytest.main()
    #sys.exit(exit_code)


