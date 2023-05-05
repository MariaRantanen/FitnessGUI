# TEST FOR MODULE TIMETOOLS.PY
# ============================

# Lets import module to be tested
import timetools

# UNIT TESTS DEFINITIONS

# Tests if datediff function calculates correct absolute values
def test_datediff():
    assert timetools.datediff('2023-04-28', '2023-04-10') == 18
    assert timetools.datediff('2023-04-10', '2023-04-28') == 18

# Tests if timediff function calculates correct absolute values
def test_timediff():
    assert round(timetools.timediff('11:30:15', '10:10:05'), 4) == 1.3361
    assert round(timetools.timediff('10:10:05', '11:30:15'), 4) == 1.3361

# Test if dateTimeDiff works correctly     
def test_dateTimeDiff():
    assert timetools.dateTimeDiff('2023-04-27 10:00:00', '2023-04-28 12:30:00') == 26.5
        
def test_datediff2():
    assert timetools.datediff2('2023-04-10', '2023-04-12', 'day') == 2
    assert timetools.datediff2('2023-04-10', '2023-06-09', 'month') == 2
    assert timetools.datediff2('2023-04-10', '2025-04-09', 'year') == 2   

def test_timediff2():
    assert timetools.timediff2('10:00:00', '12:30:00', 'hour') == 2.5
    assert timetools.timediff2('10:00:00', '12:30:00', 'minute') == 150
    assert timetools.timediff2('10:00:00', '12:30:00', 'second') == 9000
    
def  test_dateTimeDiff2():
    assert round(timetools.dateTimeDiff2('2023-04-27 10:00:00', '2023-04-28 12:30:00', 'day'), 1) == 1.1
    assert timetools.dateTimeDiff2('2023-04-27 10:00:00', '2023-04-28 12:30:00', 'hour') == 26.5
    assert timetools.dateTimeDiff2('2023-04-27 10:00:00', '2023-04-28 12:30:00', 'minute') == 1590
    
def test_finnishweekdayOrder():
    assert timetools.finnishweekdayOrder('maanantai') == 'maanantai on viikon 1. päivä'
    assert timetools.finnishweekdayOrder('tiistai') == 'tiistai on viikon 2. päivä'
    assert timetools.finnishweekdayOrder('keskiviikko') == 'keskiviikko on viikon 3. päivä'
    assert timetools.finnishweekdayOrder('torstai') == 'torstai on viikon 4. päivä'
    assert timetools.finnishweekdayOrder('perjantai') == 'perjantai on viikon 5. päivä'
    assert timetools.finnishweekdayOrder('lauantai') == 'lauantai on viikon 6. päivä'
    assert timetools.finnishweekdayOrder('sunnuntai') == 'sunnuntai on viikon 7. päivä'
    
    input_value = 'perjanatai'
    assert timetools.finnishweekdayOrder('perjanatai') == f'{input_value} ei ole viikonpäivä, tarkista syötteesi'
    