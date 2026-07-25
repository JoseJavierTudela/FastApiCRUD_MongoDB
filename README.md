# 🍃 FastAPI CRUD MongoDB

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)

API RESTful asíncrona moderna desarrollada con **FastAPI** y **MongoDB** que implementa un ciclo de vida CRUD completo (Create, Read, Update, Delete) aplicando principios de código limpio, validación estricta de datos y arquitectura modular.

---

## ✨ Características Principales

- ⚡ **Operaciones Asíncronas**: Interacción de alto rendimiento con la base de datos NoSQL aprovechando el modelo `async/await`.
- 🛡️ **Validación Estricta con Pydantic**: Serialización, tipado estático y parseo automático de schemas de datos y ObjectIDs de MongoDB.
- 🏗️ **Estructura Modular**: Arquitectura limpia que separa rutas, modelos de datos, configuración de base de datos y lógica de negocio.
- 📖 **Documentación Interactiva NAtiva**: Integración automática con **Swagger UI** y **ReDoc**.
- 🛠️ **Manejo Centralizado de Excepciones**: Respuestas HTTP estandarizadas para errores de validación, recursos no encontrados (404) y fallos del servidor.

---

## 🏗️ Estructura del Proyecto

```text
FastApiCRUD_MongoDB/
├── app/
│   ├── config/
│   │   └── database.py    # Conexión asíncrona y cliente de MongoDB
│   ├── models/
│   │   └── item.py        # Modelos Pydantic y Schemas de datos
│   ├── routes/
│   │   └── item.py        # Endpoints de la API (CRUD)
│   └── main.py            # Instancia principal de la aplicación FastAPI
├── .env.example           # Plantilla de variables de entorno
├── .gitignore             # Filtro de archivos para Git
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación oficial
