from radiation_toolkit.dose import calculate_dose

def test_calculate_dose():
    # Test case 1: Normal values
    assert calculate_dose(1000, 50, 10) == 0.0005

    # Test case 2: Zero activity
    assert calculate_dose(0, 50, 10) == 0.0

    # Test case 3: Zero time
    assert calculate_dose(1000, 0, 10) == 0.0

    # Test case 4: Zero distance (should raise an error)
    try:
        calculate_dose(1000, 50, 0)
        assert False, "Expected ValueError for zero distance"
    except ValueError:
        pass

    # Test case 5: Negative values (should raise an error)
    try:
        calculate_dose(-1000, 50, 10)
        assert False, "Expected ValueError for negative activity"
    except ValueError:
        pass

    try:
        calculate_dose(1000, -50, 10)
        assert False, "Expected ValueError for negative time"
    except ValueError:
        pass

    try:
        calculate_dose(1000, 50, -10)
        assert False, "Expected ValueError for negative distance"
    except ValueError:
        pass


