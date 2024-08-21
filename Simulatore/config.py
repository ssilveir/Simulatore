SECRET_KEY = 'SimulatoreCER'

SQLALCHEMY_DATABASE_URI = \
 '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
     SGBD = 'cockroachdb+psycopg2',
     usuario = 'samuel',
     senha = 'lK9cTVrsrJ6JFbmsl96qmg',
     servidor = 'cowing-plover-10465.7tc.aws-eu-central-1.cockroachlabs.cloud:26257',
     database = 'Simulatore',
     porta = '26257'
 )