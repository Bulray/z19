from application.app import create_app
import os
from application.config import Config


app = create_app(Config())
app.debug = True
if __name__ == '__main__':
    app.run(debug=True)