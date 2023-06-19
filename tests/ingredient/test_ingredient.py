from src.models.ingredient import Ingredient, Restriction # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ing1 = Ingredient("tomate")
    ing2 = Ingredient("queijo mussarela")
    ing3 = Ingredient("tomate")
    assert ing1.__hash__() != ing2.__hash__()
    assert ing1.__hash__() == ing3.__hash__()
    assert ing1 != ing2  # TestIngredientInvalidEqualDifferent
    assert ing1 == ing3  # operador identifica ingredientes iguais
    assert ing2.name == "queijo mussarela"
    assert ing1.__repr__() == "Ingredient('tomate')"
    assert ing2.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
