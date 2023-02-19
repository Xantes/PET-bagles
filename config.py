WTF_CSRF_ENABLED = True
SECRET_KEY = 'bimbimbim'

POSTGRE_USER = 'admin'
POSTGRE_PASS = '1111'
POSTGRE_HOST = 'localhost'
POSTGRE_DB = 'bagles_db'

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRE_USER}:{POSTGRE_PASS}@{POSTGRE_HOST}/{POSTGRE_DB}"


LOG_CFG = 'settings/log.yml'
MAIN_CFG = 'settings/main.yml'
MENU_CFG = 'settings/menu.yml'
