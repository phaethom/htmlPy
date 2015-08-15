import os
import htmlPy
from PyQt4 import QtGui


# Initial confiurations
BASE_DIR = str(os.path.dirname(__file__))


# GUI initializations
app = htmlPy.AppWindow("Application", maximized=True, flash=True)


# GUI configurations
app.set_asset_path(BASE_DIR + '/static/')
app.set_template_path(BASE_DIR + "/templates/")

app.web_app.setMinimumWidth(1024)
app.web_app.setMinimumHeight(768)
app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/static/img/icon.png"))


# Binding of back-end functionalities with GUI

# Import back-end functionalities
from html_to_python import ClassName

# Register back-end functionalities
app.register(ClassName())


# Instructions for running application
if __name__ == "__main__":
    # The driver file will have to be imported everywhere in back-end.
    # So, always keep app.start() in if __name__ == "__main__" conditional
    app.start()
