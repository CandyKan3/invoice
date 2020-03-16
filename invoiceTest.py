import pytest
from Invoice import Invoice
@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5}, 'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products
@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice
def test_canAddProduct(invoice, products):
    invoice.addProduct(10, 20, 10)
    assert invoice.items == {'discount': 10, 'qnt': 10, 'unit_price': 20}

def test_CanCalculateImpurePrices(invoice, products):

    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75
def test_canCalculateTotalDiscount(invoice ,products):

    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62
def test_canCalculateTotalPurePrices(invoice ,products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38
def test_clearProducts(invoice, products):
    invoice.addProduct(10, 20, 10)
    assert invoice.items == {'discount': 10, 'qnt': 10, 'unit_price': 20}
    assert invoice.clearProducts(products) =={}

