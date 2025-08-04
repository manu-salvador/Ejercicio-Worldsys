import pytest

#test de happy path
@pytest.mark.parametrize("person_id", [111, 222])
def test_import_happy_path(api, person_id):
    response = api.import_person(person_id)
    assert response is not None, "No se recibió respuesta"
    assert response.status_code == 200, f"Status inesperado: {response.status_code}"
    assert "success" in response.text.lower() or response.json(), "No se encontró mensaje de éxito"
    print("Happy path OK para personId:", person_id)

#ejemplos de sad path
@pytest.mark.parametrize("payload", [
    [{}],  # personId sin enviar
    [{"personId": ""}],  # personId vacio
    [{"personId": None}],  # personId null
    [{"personId": "abc"}],  # personId inválido con letras
])

#test de sad path
def test_import_sad_path(api, payload):
    response = api.import_person_raw(payload)
    assert response is not None, "No se recibió respuesta"
    assert response.status_code != 200, "Se esperaba error pero fue exitoso"
    assert "error" in response.text.lower() or response.json(), "No se encontró mensaje de error"
    print("Sad path OK para payload:", payload)