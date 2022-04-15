from Module import Person, Wizard, HealthPotion


def test_person_get_life_point():
    test_person = Person("test")
    result = test_person.get_life_points()
    expected_result = test_person.life_points
    assert result == expected_result

def test_personne_hit():
    test_person_get_hit = Person("getHit")
    test_person_hit = Person("Hit")
    life = test_person_get_hit.get_life_points()
    test_person_hit.hit(test_person_get_hit)
    life_after_hit = test_person_get_hit.get_life_points()
    result = life - life_after_hit
    expected_result = 10
    assert result == expected_result

def test_wizard():
    test_wizard = Wizard("getHit")
    result = test_wizard.get_life_points()
    expected_result = 80
    assert result == expected_result


def test_wizard_hit():
    test_wizard_get_hit = Wizard("getHit")
    test_wizard_hit = Wizard("Hit")
    life = test_wizard_get_hit.get_life_points()
    test_wizard_hit.hit(test_wizard_get_hit)
    life_after_hit = test_wizard_get_hit.get_life_points()
    result = life - life_after_hit
    expected_result = 15
    assert result == expected_result

def test_person_is_dead_false():
    test_person = Person("test")
    result = test_person.is_dead()
    expected_result = False
    assert result == expected_result


def test_person_is_dead_false():
    test_person = Person("test")
    test_person.life_points = -5
    result = test_person.is_dead()
    expected_result = True
    assert result == expected_result

def test_person_gained_life_points():
    test_person = Person("test")
    life = test_person.get_life_points()
    test_person.gained_life_points(20)
    life_after_gained_life_points = test_person.get_life_points()
    result = life_after_gained_life_points
    expected_result = life + 20
    assert result == expected_result

def test_health_potion():
    test_person = Person("test")
    life = test_person.get_life_points()
    HealthPotion.was_used_by(test_person)
    life_after_use_popo = test_person.get_life_points()
    result = life_after_use_popo
    expected_result = life + 10
    assert result == expected_result