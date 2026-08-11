# 💸 PlataGone

> **¿Dónde se fue la plata?**

**PlataGone** es una aplicación para gestionar gastos y finanzas personales, permitiendo registrar compras, tickets y comprobantes, organizar gastos y productos por categorías, mantener un historial de movimientos y realizar un seguimiento de tarjetas de crédito, deudas y créditos personales.

El objetivo es centralizar la información financiera y generar resúmenes que permitan entender mejor **en qué se está yendo la plata**. 💸

---

## 🚀 Funcionalidades

* 🛒 Registro y gestión de compras.
* 🧾 Carga y gestión de tickets y comprobantes.
* 💰 Registro y seguimiento de gastos y consumos.
* 🏷️ Organización de gastos y productos mediante categorías.
* 📜 Historial de movimientos.
* 💳 Gestión de tarjetas de crédito.
* 📊 Seguimiento de deudas y consumos de tarjetas.
* 💵 Gestión de créditos personales.
* 📈 Resúmenes y estadísticas financieras.
* 🔎 Consulta del historial financiero para analizar los gastos.

---

## 🏗️ Arquitectura

Este repositorio contiene el **backend de PlataGone**, encargado de proporcionar la API y gestionar la lógica de negocio, persistencia de datos y procesamiento de la información financiera.

```text
┌─────────────────────┐
│     PlataGone       │
│      Frontend       │
└──────────┬──────────┘
           │
           │ HTTP / API
           ▼
┌─────────────────────┐
│     PlataGone       │
│       Backend       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      Database       │
└─────────────────────┘
```

---

## 🧩 Módulos principales

La aplicación se organiza alrededor de diferentes áreas relacionadas con las finanzas personales:

```text
Compras
Tickets y comprobantes
Gastos
Productos
Categorías
Tarjetas de crédito
Deudas
Créditos personales
Movimientos
Resúmenes financieros
```

---

## ⚙️ Requisitos

Antes de comenzar, asegurate de tener instaladas las herramientas necesarias para ejecutar el proyecto.

> Los requisitos específicos y las versiones utilizadas se documentarán a medida que avance el desarrollo.

---

## 🔧 Instalación

Cloná el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd platagone
```

Luego instalá las dependencias correspondientes al proyecto.

```bash
# TODO: agregar instrucciones de instalación
```

---

## 🔐 Variables de entorno

El proyecto utiliza variables de entorno para configurar diferentes aspectos de la aplicación.

Crear un archivo `.env` a partir del ejemplo:

```bash
cp .env.example .env
```

> Las variables requeridas se documentarán en `.env.example`.

---

## ▶️ Ejecución

Para iniciar el servidor de desarrollo:

```bash
# TODO: agregar comando de ejecución
```

Una vez iniciado, la API estará disponible en la URL configurada para el entorno local.

---

## 🧪 Tests

Para ejecutar los tests:

```bash
# TODO: agregar comando de tests
```

---

## 📚 API

La API de PlataGone permitirá gestionar los diferentes recursos relacionados con las finanzas personales.

Entre ellos:

* Compras
* Gastos
* Productos
* Categorías
* Tickets
* Comprobantes
* Tarjetas
* Deudas
* Créditos
* Movimientos
* Resúmenes

> La documentación de la API se incorporará en esta sección.

---

## 🗺️ Roadmap

Algunas funcionalidades previstas para el proyecto:

* [ ] Gestión de compras.
* [ ] Gestión de gastos y consumos.
* [ ] Carga de tickets y comprobantes.
* [ ] Categorías de gastos.
* [ ] Categorías de productos.
* [ ] Historial de movimientos.
* [ ] Gestión de tarjetas de crédito.
* [ ] Gestión de deudas.
* [ ] Gestión de créditos personales.
* [ ] Resúmenes financieros.
* [ ] Estadísticas y análisis de gastos.
* [ ] Mejoras en la visualización de la información financiera.

---

## 🤝 Contribuciones

Las contribuciones, sugerencias y mejoras son bienvenidas.

Si encontraste un problema o tenés una idea para mejorar PlataGone, podés abrir un **Issue** o realizar un **Pull Request**.

---

## 📄 Licencia

> TODO: definir licencia del proyecto.

---

## 💸 Finalmente...

Porque todos tenemos esa pregunta alguna vez:

> **¿Dónde se fue la plata?**

**PlataGone** intenta ayudarte a encontrar la respuesta. 😅
