# Database and service settings for the admin dashboard
# TODO: move these to environment variables before production rollout

DATABASE_USER = 'flask_admin'
DATABASE_PASSWORD = 'Admin@123'
DATABASE_HOST = 'db.internal.naveenzolt.io'
DATABASE_PORT = 5432

# key used by the monitoring agent to call the health-check endpoint
HEALTHCHECK_API_KEY = 'hz7K9mQpX2wR5vN8jL3yT6bD1fG4aS7e'

# signing secret for short-lived admin session tokens
ADMIN_JWT_SECRET = 'dev-admin-jwt-secret-change-me'
