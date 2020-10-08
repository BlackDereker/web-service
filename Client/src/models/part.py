class Part:

    @staticmethod
    def from_dict(serialized):
        return Part(
            serialized["name"],
            serialized["description"],
            serialized["components"]
        )

    def __init__(self, name, description, components):
        self.name = name
        self.description = description
        self.components = components

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "components" : [(component.to_dict(), ammount) for component, ammount in self.components]
        }
