#question sample to see how to access the count

class Furniture:

    materials = []
    material_count = {}

    def __init__(self, name, material):
        self.name = name
        self.material = material
        Furniture.materials.append(self.material)
        Furniture.count_material()

    @classmethod
    def count_material(cls):
        for material in cls.materials:
            cls.material_count[material] = cls.material_count.get(material, 0) + 1

Furniture("Chair", "Wood")
Furniture("Cushion", "Cotton")
Furniture("Table", "Glass")

print(Furniture.material_count)