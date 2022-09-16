import sys

from qtpy.QtWidgets import QApplication

from davy_jones.deepsee import DeepSee
from davy_jones.gui import DeepSeeGui

ds = DeepSee(fake=True)

app = QApplication(sys.argv)
gui = DeepSeeGui(ds)
gui.show()
app.exec()
