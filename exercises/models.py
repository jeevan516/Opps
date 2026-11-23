"""Pydantic models from 04-pydantic.ipynb."""

from typing import Annotated

from pydantic import BaseModel, Field, NegativeInt, PositiveInt, StringConstraints


class Model(BaseModel):
    short_str: Annotated[str, StringConstraints(min_length=2, max_length=10)]
    regex_str: Annotated[str, StringConstraints(pattern=r"^apple (pie|tart|sandwich)$")]
    strip_str: Annotated[str, StringConstraints(strip_whitespace=True)]
    big_int: Annotated[int, Field(gt=1000, lt=1024)]
    mod_int: Annotated[int, Field(multiple_of=5)]
    pos_int: PositiveInt
    neg_int: NegativeInt
    short_list: Annotated[list[int], Field(min_length=1, max_length=4)]


class Person(BaseModel):
    name: Annotated[str, StringConstraints(max_length=50)]
    age: Annotated[int, Field(ge=18, le=120)]
    email: Annotated[str, StringConstraints(pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")]


def create_person(data: dict) -> Person:
    return Person.model_validate(data)
