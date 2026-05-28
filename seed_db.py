import os
import django

# Setup django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vinoteca.settings')
django.setup()

from catalogo.models import Bodega, Vino, UsuarioPersonalizado

def seed():
    print("Iniciando la siembra de base de datos (seeding)...")
    
    # Clean existing data to avoid duplicates
    Vino.objects.all().delete()
    Bodega.objects.all().delete()
    UsuarioPersonalizado.objects.all().delete()
    
    # Create Superuser (Admin)
    admin_user = UsuarioPersonalizado.objects.create_superuser(
        username="admin",
        email="admin@vinotecadonlucas.com",
        password="adminpassword",
        dni="12345678A",
        telefono="+54 9 11 2233-4455",
        direccion="Av. de Mayo 800, CABA"
    )
    print(f"Superusuario creado: {admin_user.username} (contraseña: adminpassword)")
    
    # Create Regular User
    regular_user = UsuarioPersonalizado.objects.create_user(
        username="leonardo",
        email="leonardo@example.com",
        password="userpassword",
        dni="23456789B",
        telefono="+54 9 261 445-5667",
        direccion="Av. San Martín 1500, Mendoza"
    )
    print(f"Usuario regular creado: {regular_user.username} (contraseña: userpassword)")
    
    # Create Bodegas
    bodegas_data = [
        {"nombre": "Bodega Catena Zapata", "ubicacion": "Mendoza, Argentina"},
        {"nombre": "Bodega Rutini Vinos", "ubicacion": "Mendoza, Argentina"},
        {"nombre": "Bodega El Esteco", "ubicacion": "Salta, Argentina"},
        {"nombre": "Bodega Concha y Toro", "ubicacion": "Valle del Maipo, Chile"}
    ]
    
    bodegas = {}
    for data in bodegas_data:
        b, created = Bodega.objects.get_or_create(nombre=data["nombre"], defaults={"ubicacion": data["ubicacion"]})
        bodegas[data["nombre"]] = b
        print(f"Bodega creada: {b.nombre}")
        
    # Create Vinos
    vinos_data = [
        {
            "nombre": "Catena Zapata Malbec Argentino",
            "precio": 120.00,
            "tipo": "Malbec",
            "bodega": bodegas["Bodega Catena Zapata"]
        },
        {
            "nombre": "Rutini Colección Cabernet Sauvignon",
            "precio": 45.50,
            "tipo": "Cabernet",
            "bodega": bodegas["Bodega Rutini Vinos"]
        },
        {
            "nombre": "Rutini Colección Merlot",
            "precio": 48.00,
            "tipo": "Merlot",
            "bodega": bodegas["Bodega Rutini Vinos"]
        },
        {
            "nombre": "El Esteco Chardonnay Selección",
            "precio": 35.00,
            "tipo": "Chardonnay",
            "bodega": bodegas["Bodega El Esteco"]
        },
        {
            "nombre": "Casillero del Diablo Cabernet Sauvignon",
            "precio": 25.00,
            "tipo": "Cabernet",
            "bodega": bodegas["Bodega Concha y Toro"]
        }
    ]
    
    for data in vinos_data:
        v = Vino.objects.create(
            nombre=data["nombre"],
            precio=data["precio"],
            tipo=data["tipo"],
            bodega=data["bodega"]
        )
        print(f"Vino creado: {v.nombre} ({v.tipo}) - ${v.precio}")
        
    print("Siembra de base de datos completada con éxito.")

if __name__ == '__main__':
    seed()
