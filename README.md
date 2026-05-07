## PROYECTO DE AUTOMATIZACION DE SAUCEDEMO

# AUTOR: JESUS DAVID hERNANDEZ

# Automatización de Pruebas - SauceDemo

## Propósito del proyecto
Este proyecto tiene como objetivo automatizar las pruebas funcionales del sitio web 
[SauceDemo](https://www.saucedemo.com/), simulando el comportamiento de un usuario real 
para verificar que las funcionalidades principales funcionen correctamente.

Las pruebas cubren:
- Inicio de sesión con credenciales válidas
- Visualización del catálogo de productos
- Agregar un producto al carrito de compras

## Tecnologías utilizadas
- **Python 3.14** - Lenguaje de programación
- **Selenium** - Automatización del navegador
- **pytest** - Framework de pruebas
- **pytest-html** - Generación de reportes HTML
- **ChromeDriver 147** - Driver para controlar Chrome

## Cómo instalar las dependencias

### 1. Clonar el repositorio
```bash
git clone https://github.com/jesusdavidht4/PRE_ENTREGA_JESUS_DAVID_HERNANDEZ.git
cd PRE_ENTREGA_JESUS_DAVID_HERNANDEZ
```

### 2. Instalar las dependencias
```bash
pip install -r requirements.txt
```

## Cómo ejecutar las pruebas

### Ejecutar todos los tests
```bash
pytest
```

### Ejecutar con reporte HTML
```bash
pytest --html=reports/reporte.html --self-contained-html
```

El reporte se genera en la carpeta `reports/` y se puede abrir en cualquier navegador.

## Estructura del proyecto
PRE ENTREGA/
├── test/
│   └── test_saucede.py
├── utils/
│   ├── init.py
│   └── helpers.py
├── reports/
│   └── reporte.html
├── datos/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

## Tests incluidos
- **test_loging**: Verifica que el login con credenciales válidas redirige al inventario
- **test_catalogo_productos**: Verifica que el catálogo muestra productos correctamente
- **test_agregar_al_carrito**: Verifica que se puede agregar un producto al carrito

## Credenciales de prueba
- **Usuario**: standard_user
- **Contraseña**: secret_sauce