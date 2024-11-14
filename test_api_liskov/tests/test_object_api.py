import allure
import pytest


@allure.suite('Objects API')
@allure.feature('Get objects')
@allure.story('Positive')
@allure.title('Get all objects')
@allure.severity('Critical')
def test_get_all_objects(count_objects, new_object, get_all_objects_endpoint):
    get_all_objects_endpoint.get_all_objects()
    get_all_objects_endpoint.check_status_200()
    get_all_objects_endpoint.compare_objects_quantity_before_and_after(
        count_objects,
        get_all_objects_endpoint.response.status_code
    )


@allure.suite('Objects API')
@allure.feature('Get objects')
@allure.story('Positive')
@allure.title('Get object by existing ID')
@allure.severity('Major')
def test_get_object_by_existing_id(new_object, payload, get_one_object_endpoint):
    get_one_object_endpoint.get_one_object(new_object)
    get_one_object_endpoint.check_status_200()
    get_one_object_endpoint.compare_object_data(new_object, payload)


@allure.suite('Objects API')
@allure.feature('Create objects')
@allure.story('Positive')
@allure.title('Create object with correct data')
@allure.severity('Critical')
def test_create_object_with_correct_data(new_object, create_object_endpoint):
    create_object_endpoint.check_status_200()
    create_object_endpoint.check_response_data()
    create_object_endpoint.check_id()


@allure.suite('Objects API')
@allure.feature('Create objects')
@allure.story('Negative')
@allure.title('Create object with invalid data')
@allure.severity('Minor')
@pytest.mark.parametrize('payload', [{"one": "two"}], indirect=True)
def test_create_object_with_invalid_body(count_objects, new_object, payload,
                                         create_object_endpoint, get_all_objects_endpoint):
    create_object_endpoint.check_status_400()
    get_all_objects_endpoint.compare_objects_quantity_before_and_after(
        count_objects,
        create_object_endpoint.response.status_code
    )


@allure.suite('Objects API')
@allure.feature('PUT update objects')
@allure.story('Positive')
@allure.title('Full object update with correct data')
@allure.severity('Critical')
def test_full_update_object_with_correct_data(new_object, payload, full_object_update_endpoint):
    full_object_update_endpoint.full_object_update(new_object, payload)
    full_object_update_endpoint.check_status_200()
    full_object_update_endpoint.check_id_not_changed()
    full_object_update_endpoint.check_response_data()


@allure.suite('Objects API')
@allure.feature('PUT update objects')
@allure.story('Negative')
@allure.title('Full object update with invalid data')
@allure.severity('Minor')
def test_full_update_object_with_invalid_body(new_object, full_object_update_endpoint):
    payload = {"one": "two"}
    full_object_update_endpoint.full_object_update(new_object, payload)
    full_object_update_endpoint.check_status_400()
    full_object_update_endpoint.check_after_update_failed()


@allure.suite('Objects API')
@allure.feature('PATCH update objects')
@allure.story('Positive')
@allure.title('Partially object update with correct data')
@allure.severity('Major')
def test_update_state_name_only(new_object, partially_object_update_endpoint):
    payload = {"name": "New South Wales"}
    partially_object_update_endpoint.partially_object_update(new_object, payload)
    partially_object_update_endpoint.check_status_200()
    partially_object_update_endpoint.check_state_name_changed(payload)
    partially_object_update_endpoint.check_object_data_not_changed()


@allure.suite('Objects API')
@allure.feature('PATCH update objects')
@allure.story('Negative')
@allure.title('Partially object update with invalid data')
@allure.severity('Minor')
def test_partially_update_with_invalid_data(new_object, partially_object_update_endpoint):
    payload = {"one": "two"}
    partially_object_update_endpoint.partially_object_update(new_object, payload)
    partially_object_update_endpoint.check_status_400()
    partially_object_update_endpoint.check_after_update_failed()


@allure.suite('Objects API')
@allure.feature('Delete objects')
@allure.story('Positive')
@allure.title('Delete existing object')
@allure.severity('Major')
def test_delete_existing_object(new_object, delete_object_endpoint, get_one_object_endpoint):
    delete_object_endpoint.delete_object(new_object)
    delete_object_endpoint.check_status_200()
    get_one_object_endpoint.check_object_after_deletion()
