-- Create n8n database (already created by POSTGRES_DB, but safe to include)
CREATE DATABASE n8n_db;
GRANT ALL PRIVILEGES ON DATABASE n8n_db TO n8n_user;

-- (Optional) Create OpenWebUI database if you want it to persist in Postgres
CREATE DATABASE openwebui_db;
GRANT ALL PRIVILEGES ON DATABASE openwebui_db TO n8n_user;
