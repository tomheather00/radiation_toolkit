def calculate_dose(Activity:float, time:int, distance:int) -> float:
    """
    Calculate the radiation dose based on activity, time, and distance.

    Parameters:
    Activity (float): The activity of the radioactive source in becquerels (Bq).
    time (float): The exposure time in seconds.
    distance (float): The distance from the source in meters.

    Returns:
    float: The calculated dose in sieverts (Sv).
    """
    # Constants
    decay_constant = 0.693 / 30  # Example decay constant for a specific isotope
    dose_conversion_factor = 1e-6  # Conversion factor to sieverts

    # Calculate the dose
    dose = (Activity * time * dose_conversion_factor) / (distance ** 2)
    
    return dose
