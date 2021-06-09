from flask import Flask
import views
import error_views
from config import db

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Register normal views
app.register_blueprint(views.bp)

# Register error views
app.register_blueprint(error_views.bp)

if __name__ == '__main__':
    # Run the app
    app.run()
