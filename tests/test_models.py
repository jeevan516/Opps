import pytest
from pydantic import ValidationError

from exercises.models import Model, create_person

VALID_MODEL_DATA = {
    "short_str": "hi there",
    "regex_str": "apple tart",
    "strip_str": "  padded value  ",
    "big_int": 1001,
    "mod_int": 20,
    "pos_int": 7,
    "neg_int": -7,
    "short_list": [1, 2],
}


def test_model_accepts_valid_data_and_strips_whitespace():
    model = Model.model_validate(VALID_MODEL_DATA)
    assert model.strip_str == "padded value"
    assert model.big_int == 1001


def test_model_rejects_every_bad_field():
    bad = {
        "short_str": "h",
        "regex_str": "banana pie",
        "strip_str": "  keep me  ",
        "big_int": 999,
        "mod_int": 14,
        "pos_int": -5,
        "neg_int": 3,
        "short_list": [],
    }
    with pytest.raises(ValidationError) as excinfo:
        Model.model_validate(bad)
    assert excinfo.value.error_count() == 7


def test_model_rejects_too_long_list():
    with pytest.raises(ValidationError):
        Model.model_validate({**VALID_MODEL_DATA, "short_list": [1, 2, 3, 4, 5]})


def test_create_person_valid():
    person = create_person({"name": "Jane Doe", "age": 28, "email": "jane@example.com"})
    assert person.age == 28
    assert person.email == "jane@example.com"


def test_create_person_invalid_reports_three_errors():
    with pytest.raises(ValidationError) as excinfo:
        create_person({"name": "A" * 70, "age": 12, "email": "not-an-email"})
    assert {e["loc"][0] for e in excinfo.value.errors()} == {"name", "age", "email"}


@pytest.mark.parametrize("age", [17, 121])
def test_create_person_age_bounds(age):
    with pytest.raises(ValidationError):
        create_person({"name": "Jane", "age": age, "email": "jane@example.com"})
