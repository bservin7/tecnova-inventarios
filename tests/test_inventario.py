import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.inventario import calcular_stock


def test_calcular_stock():
    assert calcular_stock(10, 3) == 7
    assert calcular_stock(5, 5) == 0
    assert calcular_stock(20, 1) == 19

from src.inventario import agregar_producto

def test_agregar_producto():
    assert agregar_producto(10, 5) == 15
    assert agregar_producto(0, 3) == 3
    assert agregar_producto(7, 0) == 7

from src.inventario import eliminar_producto

def test_eliminar_producto():
    assert eliminar_producto(10, 3) == 7
    assert eliminar_producto(5, 10) == 0  # no permite negativo
    assert eliminar_producto(8, 0) == 8
