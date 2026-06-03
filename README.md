<<<<<<< HEAD
# Proyecto Final - Automatización de Pruebas

**Autor:** Jesús David Hernández  
**Curso:** QA Automation - Talento Tech  
**Sitio bajo prueba:** [SauceDemo](https://www.saucedemo.com/)  
**API bajo prueba:** [ReqRes](https://reqres.in/)

---

## Propósito del proyecto

Framework de automatización de pruebas completo que combina pruebas de UI y API, implementando el patrón Page Object Model (POM), parametrización con múltiples fuentes de datos, generación de reportes HTML y sistema de logging.

---

## Tecnologías utilizadas

| Tecnología | Uso |
|-----------|-----|
| Python 3.14 | Lenguaje principal |
| Selenium WebDriver | Automatización de UI |
| pytest | Framework de testing |
| Requests | Pruebas de API |
| pytest-html | Reportes HTML |
| Faker | Generación de datos de prueba |
| webdriver-manager | Gestión automática de ChromeDriver |

---

## Estructura del proyecto

```
ENTREGA FINAL/
├── data/
│   ├── checkout.csv          # Datos de formulario de checkout
│   ├── ordenamiento.py       # Datos de ordenamiento
│   ├── precios.py            # Datos de precios esperados
│   ├── productos.py          # Datos de productos
│   ├── usuarios_invalidos.py # Credenciales inválidas
│   └── users.json            # Usuarios válidos
├── pages/
│   ├── agregar_producto_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   ├── login_error_page.py
│   ├── login_pages.py
│   ├── orden_page.py
│   └── precios_page.py
├── test/
│   ├── test_agregar_producto.py
│   ├── test_api.py
│   ├── test_checkout.py
│   ├── test_inventory.py
│   ├── test_login.py
│   ├── test_login_negativo.py
│   ├── test_ordenamiento.py
│   └── test_precios.py
├── utils/
│   ├── api_client.py         # Cliente HTTP para pruebas de API
│   └── helpers.py            # Driver, logging, screenshots, carga de datos
├── reports/                  # Reportes HTML generados
├── screenshots/              # Capturas automáticas en fallos
├── logs/                     # Logs de ejecución
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/jesusdavidht4/ENTREGA-FINAL-QA-AUTOMATION.git
cd proyecto-final-automation-testing-jesus-hernandez
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## Cómo ejecutar las pruebas

### Todos los tests
```bash
pytest test/ -v
```

### Solo tests de UI
```bash
pytest test/ -v --ignore=test/test_api.py
```

### Solo tests de API
```bash
pytest test/test_api.py -v
```

El reporte HTML se genera automáticamente en `reports/reporte.html` y puede abrirse en cualquier navegador.

---

## Tests incluidos

### UI - SauceDemo (35 tests)

| Archivo | Descripción |
|--------|-------------|
| test_login.py | Login con usuarios válidos (parametrizado con JSON) |
| test_login_negativo.py | Login con credenciales inválidas (parametrizado con Python) |
| test_inventory.py | Validación del catálogo de productos |
| test_agregar_producto.py | Agregar productos al carrito y validar |
| test_ordenamiento.py | Ordenamiento de productos por nombre y precio |
| test_precios.py | Validación de precios de productos |
| test_checkout.py | Flujo completo de checkout con CSV y Faker |

### API - ReqRes (3 tests)

| Test | Método | Descripción |
|------|--------|-------------|
| test_get_users | GET | Obtener lista de usuarios y validar estructura |
| test_create_user | POST | Crear usuario y validar respuesta |
| test_delete_user | DELETE | Eliminar usuario y validar status 204 |

---

## Cómo interpretar los reportes

- Abrí `reports/reporte.html` en cualquier navegador
- Los tests aparecen con estado **PASSED** (verde) o **FAILED** (rojo)
- Los tests fallidos incluyen el screenshot automático tomado en el momento del fallo
- Los logs detallados se encuentran en `logs/test_run.log`

---

## Credenciales de prueba

**UI - SauceDemo**
- Usuario válido: `standard_user` / `secret_sauce`
- Usuario bloqueado: `locked_out_user` / `secret_sauce`

**API - ReqRes**
- API Key requerida en `utils/api_client.py`
=======
# ENTREGA-FINAL-QA-AUTOMATION
Entrega Final curso QA Automation (JESUS DAVID HERNANDEZ)
>>>>>>> b60628cc305848512f679fa6f958486e1d7b9f98
