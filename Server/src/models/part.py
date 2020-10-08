from .part_repository import PartRepository


class Part:

    unique_id = 0

    @staticmethod
    def generate_unique_id():
        id = Part.unique_id
        Part.unique_id += 1
        return id

    @staticmethod
    def from_dict(serialized):
        return Part(
            serialized["name"],
            serialized["description"],
            [(Part.from_dict(component), ammount) for component, ammount in serialized["components"]]
        )

    def __init__(self, name, description, components):
        self.unique_id = Part.generate_unique_id()
        self.name = name
        self.description = description
        self.components = [(component.unique_id, ammount) for component, ammount in components]
        PartRepository.add_part(self)

    def to_dict(self):
        return {
            "unique_id": self.unique_id,
            "name": self.name,
            "description": self.description,
            "components" : [{"unique_id": component, "ammount": ammount} for component, ammount in self.components]
        }
