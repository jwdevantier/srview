import logging
import coloredlogs
from srview import app

if __name__ == '__main__':
    coloredlogs.install(level=logging.DEBUG, show_hostname=False)
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)