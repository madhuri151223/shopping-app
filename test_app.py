from app import delivery_charge

def test_free_delivery():
    assert delivery_charge(70) == 0

def test_paid_delivery():
    assert delivery_charge(30) == 5
