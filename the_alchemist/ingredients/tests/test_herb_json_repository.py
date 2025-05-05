def test_get_by_name(herb_repository):
    herb = herb_repository.get_by_name("Mandrake")
    assert herb is not None
    assert herb.name == "Mandrake"


def test_get_all(herb_repository):
    herbs = herb_repository.get_all()
    assert isinstance(herbs, list)
    assert len(herbs) > 0


def test_add_herb(herb_repository):
    from ingredients.models.herb import Herb

    new_herb = Herb(
        category="herb",
        name="Lavender",
        description="A fragrant herb used for relaxation.",
        features={"aroma": 8},
    )
    herb_repository.add(new_herb)
    added_herb = herb_repository.get_by_name("Lavender")
    assert added_herb is not None
    assert added_herb.name == "Lavender"
