from pydantic import BaseModel, ValidationError, Field

from model import AnimalEntity


class FormSchema(BaseModel):
    animal_type: str
    image_filepath: str
    image_discription: str

    @classmethod
    def from_entity(cls, animal_entity: AnimalEntity, image_discription: str) -> "FormSchema":
        return cls(animal_type=animal_entity.label_en, image_filepath=animal_entity.filepath, image_discription=image_discription)
