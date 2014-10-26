import allure

def test_true():
    with allure.step('Check value'):
        assert True

def test_false():
    with allure.step('Check value'):
        assert False
