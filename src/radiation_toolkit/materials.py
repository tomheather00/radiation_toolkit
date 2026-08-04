class Material:
    def __init__(self, name, density, attenuation_coefficient):
        self.name = name
        self.density = density  # in g/cm^3
        self.attenuation_coefficient = attenuation_coefficient  # in cm^-1
    def describe(self):
        return f"{self.name} has a density:{self.density} g/cm^3 and attenuation coefficient:{self.attenuation_coefficient} cm^-1"

lead = Material("Lead", 11.34, 0.12)
concrete = Material("Concrete", 2.3, 0.05)
water = Material("Water", 1.0, 0.02)
steel = Material("Steel", 7.85, 0.08)
air = Material("Air", 0.0012, 0.0001)
material_list = [lead, concrete, water, steel, air]
for material in material_list:
    print(material.describe())