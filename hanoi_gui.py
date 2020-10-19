from test import Window as GuiWindow
from Hanoi import Hanoi as HanoiWidget 
 

class QtGuiThread():

    def __init__(self):
        self.widget = HanoiWidget()
        self.gui = GuiWindow(self.widget)

