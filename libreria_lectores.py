import sqlite3

# Conexión a la base de datos (creará el archivo si no existe)
conn = sqlite3.connect('libreria_lectores.db')
cursor = conn.cursor()

# Creación de la tabla de clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        genero TEXT
    )
''')

# Creación de la tabla de ventas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        libro_id INTEGER,
        cantidad INTEGER,
        importe_bruto REAL,
        monto_descuento REAL,
        importe_neto REAL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
''')

# Función para insertar un nuevo cliente
def insertar_cliente(nombre, genero):
    cursor.execute('INSERT INTO clientes (nombre, genero) VALUES (?, ?)', (nombre, genero))
    conn.commit()
    return cursor.lastrowid  # Devuelve el ID del cliente insertado

# Función para insertar una nueva venta
def realizar_venta(cliente_id, libro_id, cantidad, importe_bruto, monto_descuento, importe_neto):
    cursor.execute('''
        INSERT INTO ventas (cliente_id, libro_id, cantidad, importe_bruto, monto_descuento, importe_neto)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (cliente_id, libro_id, cantidad, importe_bruto, monto_descuento, importe_neto))
    conn.commit()

# Ejemplo de uso:
# Insertar un cliente
cliente_id = insertar_cliente('Juan', 'M')

# Realizar una venta
realizar_venta(cliente_id, 1, 3, 270, 13.5, 256.5)

# Cerrar la conexión a la base de datos
conn.close()
