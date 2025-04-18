# Basic Backend Connection to MSSQL Using SQLAlchemy, Alembic, and Flask

This project sets up a basic backend with **Flask**, using **SQLAlchemy** for ORM and **Alembic** for database migrations.  
It connects to an MSSQL database consisting of **three tables** with defined relationships.

Basic **CRUD operations** are available through RESTful endpoints.  
Since there's no frontend interface, tools like **Postman** are used for testing.

---

### 🔧 Configure Your Database URL

Make sure to set your SQL connection URL in the following places:

- `alembic.ini` → `sqlalchemy.url`
- `config.py` → `SQLALCHEMY_DATABASE_URI`
