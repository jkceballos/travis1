from app import saludar

def test_saludo():
    assert saludar() == "Hola, Travis CI funcionando correctamente!"
