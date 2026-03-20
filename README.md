create venv
`uv venv`

to activate venv
`.venv\Scripts\activate`

To create fast api project, you need the following dependencies
`uv add fastapi uvicorn`

To run try the following command
`uv run uvicorn main:app --reload`

===
In REST API, we need to follow standard recommended practices

Endpoint should be like this
localhost:8000/api/v1/users

==

## CRUD

Create
Add User -- POST
Read
List Users. -- GET
User Details -- GET
Update
Update User -- PUT / PATCH
Delete
Delete User -- DELETE

====

TODO:

1. Create rest for products-management
2. add product
3. list products
4. get product by id
5. update product by id
6. delete product by id (soft delete)

TechStack: Postgres, SQLAlchemy

uv add sqlalchemy psycopg2-binary asyncpg
