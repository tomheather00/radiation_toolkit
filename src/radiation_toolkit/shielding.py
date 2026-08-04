from materials import Material

class sheilding_layer:
    def __init__(self, material, thickness):
        self.material = material
        self.thickness = thickness
    def describe(self):
        return f"{self.thickness}cm of {self.material.name}"
    def mass_per_unit(self):
        return self.material.density * self.thickness

lead = Material("Lead", 11.34, 0.12)
lead_layer = sheilding_layer(lead, 9.0)
steel_layer = sheilding_layer("Steel", 6.0)


print(lead_layer.mass_per_unit())
