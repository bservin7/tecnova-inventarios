from src.inventario import calcular_stock

def test_calcular_stock():
    assert calcular_stock(10, 3) == 7
    assert calcular_stock(5, 5) == 0
    assert calcular_stock(20, 1) == 19
