from radiation_toolkit.dose import calculate_dose

def main():
    # Example usage of the calculate_dose function
    activity = 1000  # in becquerels (Bq)
    time = 50        # in seconds
    distance = 4     # in meters

    dose = calculate_dose(activity, time, distance)
    print(f"The calculated radiation dose is: {dose} Sv")

if __name__ == "__main__":
    main()