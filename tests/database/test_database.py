import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    database = Database()
    database.test_connection()

@pytest.mark.database
def test_check_all_users():
    database = Database()
    users = database.get_all_users()
    print(users)

@pytest.mark.database
def test_check_user_sergii():
    database = Database()
    user = database.get_user_address_by_name("Sergii")

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    database = Database()
    database.update_product_qnt_by_id(1, 25)
    quantity_product = database.select_product_qnt_by_id(1)

    assert quantity_product[0][0] == 25

@pytest.mark.database
def test_product_insert():
    database = Database()
    database.insert_product(4, 'печиво', 'солодке', 30)
    biscuit_qnt = database.select_product_qnt_by_id(4)

    assert biscuit_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    database = Database()
    database.insert_product(99, 'тестові', 'дані', 999)
    database.delete_product_by_id(99)
    qnt = database.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    database = Database()
    detailed_orders = database.get_detailed_orders()
    print("Замовлення", detailed_orders)

    assert len(detailed_orders) == 1

    assert detailed_orders[0][0] == 1
    assert detailed_orders[0][1] == 'Sergii'
    assert detailed_orders[0][2] == 'солодка вода'
    assert detailed_orders[0][3] == 'з цукром'