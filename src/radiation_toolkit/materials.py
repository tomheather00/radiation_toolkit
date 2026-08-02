class Material:
    def __init__(self, name, density):
        self.name = name
        self.density = density  # in g/cm^3

lead = Material("Lead", 11.34)

print(lead.name)