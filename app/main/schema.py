from pydantic import BaseModel, ValidationError, Field

from model import AnimalEntity


class FormSchema(BaseModel):
    animal_type: str
    image_filepath: str

    @classmethod
    def from_entity(cls, animal_entity: AnimalEntity) -> "FormSchema":
        return cls(animal_type=animal_entity.label_en, image_filepath=animal_entity.filepath)
