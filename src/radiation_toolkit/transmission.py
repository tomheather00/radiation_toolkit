from radiation_toolkit.materials import Material

def calculate_transmission(material: Material, thickness: float) -> float:
    """
    Calculate the transmission of radiation through a material.

    Parameters:
    material (Material): The material through which the radiation passes.
    thickness (float): The thickness of the material in centimeters.

    Returns:
    float: The transmission factor (between 0 and 1).
    """
    transmission = 1.0 * (2.71828 ** (-material.attenuation_coefficient * thickness))
    return transmission

def calculate_hvl(material: Material, transmission:float) -> float:
    """
    Calculate the half-value layer (HVL) of a material.

    Parameters:
    material (Material): The material for which to calculate the HVL.
    transmission (float): The transmission factor (between 0 and 1).

    Returns:
    float: The half-value layer in centimeters.
    """
    if transmission <= 0 or transmission >= 1:
        raise ValueError("Transmission must be between 0 and 1.")
    
    hvl = 0.693 / material.attenuation_coefficient
    return hvl