# Convia · catálogo de COCINAS para restaurantes (pedido del usuario 2026-10-31: buscar por tipo de comida, incluidas las 8 regiones de Oaxaca).
# Lista cerrada a propósito: un filtro solo sirve si todos usan los mismos nombres. Fuente única para directorio y perfiles.
# Reglas [propuesta, pendiente de aprobación]:
#  - Cada restaurante declara 1 cocina principal y hasta 2 más (máx. 3), para que nadie marque todas.
#  - Una cocina regional se respalda con su menú en Convia: al menos 2 platillos marcados con esa región; se revisa en la admisión.
#  - «Vegana/vegetariana» NO es cocina: ya es el rasgo «Opciones veganas». «Variada» no se usa: no ayuda a buscar.
REGIONES = [  # las 8 regiones de Oaxaca
 ('valles', 'Valles Centrales'), ('sierra-norte', 'Sierra Norte'), ('sierra-sur', 'Sierra Sur'), ('mixteca', 'Mixteca'),
 ('canada', 'Cañada'), ('papaloapan', 'Papaloapan'), ('costa', 'Costa'), ('istmo', 'Istmo'),
]
OTRAS = [('mexicana', 'Mexicana de otros estados'), ('mariscos', 'Mariscos'), ('asiatica', 'Asiática'), ('italiana', 'Italiana'), ('internacional', 'Internacional')]
COCINAS = {k: dict(n=n, region=True) for k, n in REGIONES} | {k: dict(n=n, region=False) for k, n in OTRAS}
MAX = 3
