
-- data/global_schema.sql
DROP TABLE IF EXISTS Global_Settings;
CREATE TABLE Global_Settings (
    setting_id INTEGER PRIMARY KEY AUTOINCREMENT,
    setting_name TEXT UNIQUE NOT NULL,
    setting_value TEXT,
    setting_type TEXT CHECK(setting_type IN ('string', 'integer', 'float', 'boolean'))
);

-- Insert default settings
INSERT INTO Global_Settings (setting_name, setting_value, setting_type) VALUES
('default_dimension_unit', 'cm', 'string'),
('default_currency', 'CAD', 'string');

-- Settings table
DROP TABLE IF EXISTS Settings;
CREATE TABLE Settings (
    setting_id INTEGER PRIMARY KEY AUTOINCREMENT,
    default_dimension_unit TEXT CHECK(default_dimension_unit IN ('cm', 'in')),
    default_currency TEXT CHECK(default_currency IN ('CAD', 'USD'))
);
