from flask import Flask
from properties_management import properties_mgt_file
from users_management import user_mgt_file
import os

app = Flask(__name__)

app.register_blueprint(properties_mgt_file)
app.register_blueprint(user_mgt_file)
app.secret_key = os.urandom(16)

if __name__ == '__main__':
    app.debug = True
    app.config['db_name'] = 'properties'
    app.run()
