import pytest
from app import calendar_v1_3

# TC.1. Sprawdzenie przestępności roku - rok przestępny

@pytest.mark.parametrize("year, expected", [(4, True), (1944, True), (2000, True), (9996, True)])
def test_leap_year(year, expected):

    assert calendar_v1_3.leap_year(year) == expected

# TC.2. Sprawdzenie przestępności roku - rok nieprzestępny

@pytest.mark.parametrize("year, expected", [(1, False), (1945, False), (2003, False), (9999, False)])
def test_leap_year2(year, expected):
    assert calendar_v1_3.leap_year(year) == expected

# TC.3. Sprawdzenie ilości dni w miesiącu - miesiące, które mają 31 dni

@pytest.mark.parametrize("month, year, expected", [(1, 1, 31), (1, 9999, 31), (12, 1, 31), (12, 9999, 31)])
def test_days_in_month(month, year, expected):
    assert calendar_v1_3.days_in_month(month, year) == expected

# TC.4. Sprawdzenie ilości dni w miesiącu - miesiące, które mają 30 dni

@pytest.mark.parametrize("month, year, expected", [(4, 1, 30), (4, 9999, 30), (11, 1, 30), (11, 9999, 30)])
def test_days_in_month(month, year, expected):
    assert calendar_v1_3.days_in_month(month, year) == expected

# TC.5. Sprawdzenie ilości dni w miesiącu - luty w roku nieprzestępnym

@pytest.mark.parametrize("month, year, expected", [(2, 1, 28), (2, 9999, 28)])
def test_days_in_month2(month, year, expected):
    assert calendar_v1_3.days_in_month(month, year) == expected

# TC.6. Sprawdzenie ilości dni w miesiącu - luty w roku przestępnym

@pytest.mark.parametrize("month, year, expected", [(2, 4, 29), (2, 9996, 29)])
def test_days_in_month2(month, year, expected):
    assert calendar_v1_3.days_in_month(month, year) == expected

# TC.7. Sprawdzenie, który to dzień w roku - rok nieprzestępny

@pytest.mark.parametrize("day, month, year, expected", [(28, 2, 1, 59), (28, 2, 9999, 59)])
def test_day_of_the_year(day, month, year, expected):
    assert calendar_v1_3.day_of_the_year(day, month, year) == expected

# TC.8. Sprawdzenie, który to dzień w roku - rok przestępny

@pytest.mark.parametrize("day, month, year, expected", [(29, 2, 4, 60), (29, 2, 9996, 60)])
def test_day_of_the_year(day, month, year, expected):
    assert calendar_v1_3.day_of_the_year(day, month, year) == expected

# TC.9. Sprawdzanie poprawności wczytywania danych - poprawne wpisanie wartości liczbowych (int)

def test_correct_data():
    year = 4
    month = 1
    day = 1
    assert calendar_v1_3.leap_year(year) == True
    assert calendar_v1_3.days_in_month(month, year) == calendar_v1_3.DAYS_IN_MONTHS[month - 1]
    assert calendar_v1_3.day_of_the_year(day, month, year) == 1

# TC.10. i TC.11. Sprawdzanie poprawności wczytywania danych - niepoprawne wpisanie wartości liczbowych (int)

def test_day_input(capsys, mocker):
    mocker.patch('builtins.input', side_effect=[32, 0, 1])
    day = calendar_v1_3.get_int_from_user("Enter the day:", (1, 32))
    assert day == 1
    out = capsys.readouterr()[0]
    assert 'Please enter a number from 1 and below 32' in out

def test_month_input(capsys, mocker):
    mocker.patch('builtins.input', side_effect=[13, 0, 1])
    month = calendar_v1_3.get_int_from_user("Enter the month:", (1, 13))
    assert month == 1
    out = capsys.readouterr()[0]
    assert 'Please enter a number from 1 and below 13' in out

def test_year_input(capsys, mocker):
    mocker.patch('builtins.input', side_effect=[10000, 0, 4])
    year = calendar_v1_3.get_int_from_user("Enter the year:", (1, 10000))
    assert year == 4
    out = capsys.readouterr()[0]
    assert 'Please enter a number from 1 and below 10000' in out

# TC.12. Sprawdzanie poprawności wczytywania danych - wpisanie wartości innych niż liczbowe

def test_day_input(capsys, mocker):
    mocker.patch('builtins.input', side_effect=['magda', 'sto', 'wdcnbnk', '!@#$%^&*', 1])
    day = calendar_v1_3.get_int_from_user("Enter the day:", (1, 32))
    assert day == 1
    out = capsys.readouterr()[0]
    assert 'Please type in a number!' in out

def test_month_input(capsys, mocker):
    mocker.patch('builtins.input', side_effect=['magda', 'sto', 'wdcnbnk', '!@#$%^&*', 1])
    month = calendar_v1_3.get_int_from_user("Enter the month:", (1, 13))
    assert month == 1
    out = capsys.readouterr()[0]
    assert 'Please type in a number!' in out

def test_year_input(capsys, mocker):
    mocker.patch('builtins.input', side_effect=['magda', 'sto', 'wdcnbnk', '!@#$%^&*', 4])
    year = calendar_v1_3.get_int_from_user("Enter the year:", (1, 10000))
    assert year == 4
    out = capsys.readouterr()[0]
    assert 'Please type in a number!' in out
