from typing import Optional

from pydantic import BaseModel, ValidationError, Field

from model import AnimalEntity


class FormSchema(BaseModel):
    animal_type: str
    image_filepath: str
    image_discription: str = Field(min_length=1)

    @classmethod
    def from_entity(cls, animal_entity: Optional[AnimalEntity], image_discription: str) -> "FormSchema":
        if not animal_entity:
            raise ValidationError()
        return cls(animal_type=animal_entity.label_en, image_filepath=animal_entity.filepath, image_discription=image_discription)
