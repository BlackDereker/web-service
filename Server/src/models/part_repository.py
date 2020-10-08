class PartRepository:
    parts = {}

    @staticmethod
    def get_part(unique_id):
        return PartRepository.parts.get(unique_id)

    @staticmethod
    def add_part(part):
        PartRepository.parts[part.unique_id] = part

    @staticmethod
    def list_parts():
        print(PartRepository.parts)
        return [part.to_dict() for part in PartRepository.parts.values()]
