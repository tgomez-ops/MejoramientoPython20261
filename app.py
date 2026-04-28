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

    # --- FUNCIONES DE VENTAS ---
def mostrar_ventas():
    print("\n--- TODAS LAS VENTAS ---")
    for v in ventas_restaurante:
        print(f"ID {v['idVenta']} | {v['nombreCliente']} | Mesa {v['numeroMesa']} | {v['platoPrincipal']} | ${v['valorConsumo']} | {v['metodoPago']} | {v['estadoPedido']}")

def ordenar_ventas():
    # Ordena de menor a mayor basado en valorConsumo
    ventas_restaurante.sort(key=lambda x: x['valorConsumo'])
    print("\n✅ Ventas ordenadas por valor de consumo (Menor a Mayor).")

def buscar_venta():
    id_buscar = int(input("\nIngrese el ID de la venta a buscar: "))
    for v in ventas_restaurante:
        if v['idVenta'] == id_buscar:
            print(f"🔍 Encontrado: {v}")
            return
    print("❌ No se encontró ninguna venta con ese ID.")

def eliminar_venta():
    id_eliminar = int(input("\nIngrese el ID de la venta a eliminar: "))
    for i, v in enumerate(ventas_restaurante):
        if v['idVenta'] == id_eliminar:
            venta_quitada = ventas_restaurante.pop(i)
            print(f"✅ Venta ID {id_eliminar} eliminada con éxito.")
            return
    print("❌ No se encontró el ID para eliminar.")

def agregar_venta():
    print("\n--- AGREGAR NUEVA VENTA ---")
    nueva_v = {
        "idVenta": int(input("ID Venta: ")),
        "nombreCliente": input("Nombre Cliente: "),
        "numeroMesa": int(input("Número Mesa: ")),
        "platoPrincipal": input("Plato Principal: "),
        "valorConsumo": float(input("Valor Consumo: ")),
        "metodoPago": input("Método (EFECTIVO/TARJETA/TRANSFERENCIA): ").upper(),
        "estadoPedido": input("Estado (ENTREGADO/PENDIENTE): ").upper()
    }
    ventas_restaurante.append(nueva_v)
    print("✅ Venta agregada.")

# --- MENÚ PRINCIPAL ---
def menu():
    registrar_usuario()
    if login():
        while True:
            print("\n--- MENÚ RESTAURANTE ---")
            print("1. Mostrar todas las ventas")
            print("2. Ordenar ventas por valor")
            print("3. Buscar venta por ID")
            print("4. Eliminar una venta")
            print("5. Agregar nueva venta")
            print("6. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1": mostrar_ventas()
            elif opcion == "2": ordenar_ventas()
            elif opcion == "3": buscar_venta()
            elif opcion == "4": eliminar_venta()
            elif opcion == "5": agregar_venta()
            elif opcion == "6": 
                print("👋 Saliendo del sistema...")
                break
            else:
                print("⚠️ Opción no válida.")

# Ejecución
if __name__ == "__main__":
    menu()