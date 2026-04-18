# Lista global de ventas (Los 10 registros iniciales)
ventas_restaurante = [
    {"idVenta": 1, "nombreCliente": "Ana", "numeroMesa": 5, "platoPrincipal": "Bandeja Paisa", "valorConsumo": 35000, "metodoPago": "EFECTIVO", "estadoPedido": "ENTREGADO"},
    {"idVenta": 2, "nombreCliente": "Luis", "numeroMesa": 2, "platoPrincipal": "Ajiaco", "valorConsumo": 28000, "metodoPago": "TARJETA", "estadoPedido": "ENTREGADO"},
    {"idVenta": 3, "nombreCliente": "Marta", "numeroMesa": 8, "platoPrincipal": "Sancocho", "valorConsumo": 30000, "metodoPago": "TRANSFERENCIA", "estadoPedido": "PENDIENTE"},
    {"idVenta": 4, "nombreCliente": "Carlos", "numeroMesa": 3, "platoPrincipal": "Tamales", "valorConsumo": 25000, "metodoPago": "EFECTIVO", "estadoPedido": "ENTREGADO"},
    {"idVenta": 5, "nombreCliente": "Sofía", "numeroMesa": 6, "platoPrincipal": "Lechona", "valorConsumo": 40000, "metodoPago": "TARJETA", "estadoPedido": "PENDIENTE"},
    {"idVenta": 6, "nombreCliente": "Diego", "numeroMesa": 1, "platoPrincipal": "Arroz con Pollo", "valorConsumo": 22000, "metodoPago": "TRANSFERENCIA", "estadoPedido": "ENTREGADO"},
    {"idVenta": 7, "nombreCliente": "Laura", "numeroMesa": 4, "platoPrincipal": "Mondongo", "valorConsumo": 32000, "metodoPago": "EFECTIVO", "estadoPedido": "ENTREGADO"},
    {"idVenta": 8, "nombreCliente": "Andrés", "numeroMesa": 7, "platoPrincipal": "Frijoles con Chicharrón", "valorConsumo": 27000, "metodoPago": "TARJETA", "estadoPedido": "PENDIENTE"},
    {"idVenta": 9, "nombreCliente": "Valentina", "numeroMesa": 9, "platoPrincipal": "Cazuela de Mariscos", "valorConsumo": 45000, "metodoPago": "TRANSFERENCIA", "estadoPedido": "ENTREGADO"},
    {"idVenta": 10, "nombreCliente": "Jorge", "numeroMesa": 10, "platoPrincipal": "Carne a la Llanera", "valorConsumo": 38000, "metodoPago": "EFECTIVO", "estadoPedido": "PENDIENTE"}
]
# Diccionario para el usuario registrado
usuario_db = {}

# --- FUNCIONES DE SEGURIDAD ---
def registrar_usuario():
    print("\n--- REGISTRO ---")
    usuario_db['correo'] = input("Correo: ")
    usuario_db['password'] = input("Password: ")

def login():
    intentos = 4
    while intentos > 0:
        c = input("\nLogin - Correo: ")
        p = input("Login - Password: ")
        if c == usuario_db.get('correo') and p == usuario_db.get('password'):
            print("✅ Login exitoso")
            return True
        intentos -= 1
        print(f"❌ Incorrecto. Quedan {intentos} intentos")
    print("🚫 Cuenta bloqueada")
    return False

    