-- Create the leads table with the correct schema
CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(320) NOT NULL,
    company VARCHAR(100),
    business_need TEXT,
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
);

-- Create an index on the id column
CREATE INDEX ix_leads_id ON leads (id);

-- Create an index on the email column
CREATE INDEX ix_leads_email ON leads (email);