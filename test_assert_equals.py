import pytest
from assert_equals import assert_equals

def test_first_scenario():
    with pytest.raises(Exception, match="No Error"):
        assert_equals("abc", "abc")

def test_second_scenario():
    with pytest.raises(Exception, match="Expected abcef but found abc"):
        assert_equals("abcef", "abc")

def test_third_scenario():
    with pytest.raises(Exception, match="No Error"):
        assert_equals(1, 1)

def test_fourth_scenario():
    with pytest.raises(Exception, match="Expected 1 but found 2"):
        assert_equals(1, 2)

def test_fifth_scenario():
    with pytest.raises(Exception, match="Expected type int but found type str"):
        assert_equals(1, '1')

def test_sixth_scenario():
    with pytest.raises(Exception, match="No Error"):
        assert_equals(["a", "b", "c"], ["a", "b", "c"])

def test_seventh_scenario():
    with pytest.raises(Exception, match="Expected list length 2 but found 3"):
        assert_equals(["a", "b"], ["a", "b", "c"])

def test_eight_scenario():
    with pytest.raises(Exception, match="Expected b but found d"):
        assert_equals(["a", "b"], ["a", "d"])

if __name__ == '__main__':
    pytest.main()
