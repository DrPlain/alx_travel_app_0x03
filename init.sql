-- Grant full privileges to the user
GRANT ALL PRIVILEGES ON *.* TO '${DATABASE_USER}' @'%' IDENTIFIED BY '${DATABASE_PASSWORD}' WITH
GRANT OPTION;
-- Ensure changes take effect
FLUSH PRIVILEGES;