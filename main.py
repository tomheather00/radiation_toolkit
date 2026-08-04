from radiation_toolkit.dose import calculate_dose
from radiation_toolkit.materials import Material, lead, concrete, water, steel, air
from radiation_toolkit.transmission import calculate_transmission, calculate_hvl


def main():
    # Example usage of the calculate_dose function
    activity = 1000  # in becquerels (Bq)
    time = 50        # in seconds
    distance = 10      # in meters
    material = lead # Using the lead material as an example

    if activity <= 0 or time <= 0 or distance <= 0:
        raise ValueError("Activity, time, and distance must be positive values.")

        print("Activity, time, and distance must be positive values.")
        return
    dose = calculate_dose(activity, time, distance)
    print(f"The calculated radiation dose is: {dose} Sv")

    transmission = calculate_transmission(material, thickness=5.77)  # Example thickness of 5 cm
    print(f"The transmission of radiation through {material.name} with thickness 5 cm is: {transmission}")

    hvl = calculate_hvl(material, transmission)
    print(f"The half-value layer (HVL) of {material.name} is: {hvl} cm")

if __name__ == "__main__":
    main()