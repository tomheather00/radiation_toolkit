from radiation_toolkit.dose import calculate_dose

def main():
    # Example usage of the calculate_dose function
    activity = 1000  # in becquerels (Bq)
    time = 50        # in seconds
    distance = 10      # in meters

    if activity <= 0 or time <= 0 or distance <= 0:
        raise ValueError("Activity, time, and distance must be positive values.")

        print("Activity, time, and distance must be positive values.")
        return
    dose = calculate_dose(activity, time, distance)
    print(f"The calculated radiation dose is: {dose} Sv")

if __name__ == "__main__":
    main()