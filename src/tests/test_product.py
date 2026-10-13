from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product_list = dao.select_all()
    assert len(product_list) >= 3

def test_product_insert():
    product = Product(None, 'Test Product', 'Test Brand', 19.99)
    assigned_id = dao.insert(product)
    assert assigned_id is not None

def test_product_update():
    product = Product(None, 'Test Product', 'Test Brand', 19.99)
    assigned_id = dao.insert(product)
    product.id = assigned_id
    product.name = 'Updated Test Product'
    product.brand = 'Updated Test Brand'
    product.price = 29.99
    rows_affected = dao.update(product)
    assert rows_affected == 1

def test_product_delete():
    product = Product(None, 'Test Product', 'Test Brand', 19.99)
    assigned_id = dao.insert(product)
    rows_affected = dao.delete(assigned_id)
    assert rows_affected == 1