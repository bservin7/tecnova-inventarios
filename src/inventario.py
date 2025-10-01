def calcular_stock(inicial, salida):
    """
    Calcula el stock restante después de una salida.
    """
    return inicial - salida

def agregar_producto(stock, cantidad):
    """
    Agrega productos al stock.
    """
    return stock + cantidad

def eliminar_producto(stock, cantidad):
    """
    Resta productos del stock sin permitir valores negativos.
    """
    return max(stock - cantidad, 0)
