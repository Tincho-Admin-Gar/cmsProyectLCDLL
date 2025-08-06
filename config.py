import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  #  SECRET_KEY = os.environ.get('SECRET_KEY') or '22ac660f-14d2-4acb-bbd8-0d32e7a87356'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'imageseleven'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'sp=r&st=2025-08-06T13:52:56Z&se=2025-08-06T22:07:56Z&spr=https&sv=2024-11-04&sr=c&sig=NgVPeqyQTZf9AC%2FTZwtGpAF9%2Fj7r0iyujhBOvN3E8CM%3D'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms-database-garcia.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'CMS_Test_Garcia'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cms-database-garcia-admin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CM4dmins'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "A1f8Q~K5RgdMYv2gFy5jjMXx0GwN2UWDBhlHSb3z"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "ccb3c7ab-5611-4d68-ab7a-f1a2ee9cd084"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
