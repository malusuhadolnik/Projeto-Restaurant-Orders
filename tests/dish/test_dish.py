import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    dish1 = Dish("lasanha presunto", 25.90)
    dish2 = Dish("lasanha berinjela", 27.00)
    dish3 = Dish("lasanha presunto", 25.90)

    assert dish1.name == "lasanha presunto"
    assert dish1.__hash__() == dish3.__hash__()
    assert dish1.__hash__() != dish2.__hash__()
    assert dish1 != dish2
    assert dish1 == dish3
    assert dish1.__repr__() == "Dish('lasanha presunto', R$25.90)"
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("lasanha presunto", None)
    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish("lasanha presunto", 0)
    # p/ os prox teztes vamos simular a criação de uma receita de lasanha
    ing1 = Ingredient("queijo mussarela")
    dish1.add_ingredient_dependency(ing1, 10)

    assert dish1.get_ingredients() == {ing1}
    assert dish1.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
