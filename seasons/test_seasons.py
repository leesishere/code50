import sys
sys.path.append('/workspaces/21178063/seasons/')
from seasons import age_in_minutes

def test_correct():
    assert age_in_minutes('Jamuary 1, 1999') == 'Invalid Date'

def test_incorrect():
    assert age_in_minutes('1999-01-01') == 'five hundred and twenty-five thousand, six hundred'
    assert age_in_minutes('1999-12-31') == 'one thousand, four hundred and forty'
    assert age_in_minutes('1970-01-01') == 'fifteen million, seven hundred and seventy-eight thousand and eighty'



#for example, fail to raise a ValueError when it should. Run your tests by executing pytest test_seasons.py. pytest should
