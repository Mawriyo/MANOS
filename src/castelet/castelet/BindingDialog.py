from PyQt5.QtWidgets import QDialog, QComboBox, QVBoxLayout, QPushButton
from custom_msg.msg import ListString,Pos, MANOSBundle
from std_msgs.msg import Int16, String
finger_combinations = {
    "[1, 0, 0, 0, 0]": "Thumb",
    "[0, 1, 0, 0, 0]": "Pointer",
    "[0, 0, 1, 0, 0]": "Middle",
    "[0, 0, 0, 1, 0]": "Ring",
    "[0, 0, 0, 0, 1]": "Pinky",
    "[1, 1, 0, 0, 0]": "Pointer",
    "[0, 1, 1, 0, 0]": "Pointer",
    "[0, 0, 1, 1, 0]": "Middle",
    "[0, 0, 0, 1, 1]": "Ring",
    "[1, 1, 1, 0, 0]": "Middle",
    "[0, 1, 1, 1, 0]": "Middle",
    "[0, 0, 1, 1, 1]": "Middle",
    "[1, 1, 1, 1, 0]": "Middle",
    "[0, 1, 1, 1, 1]": "Middle",
    "[1, 1, 1, 1, 1]": "Middle",
}
class BindingDialog(QDialog):
    def __init__(self, topic, hand , parent=None):
        super().__init__(parent)
        self.topics = topic
        self.hand = hand
        self.finger_combinations = finger_combinations
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()

        # Combo box for topics
        self.topicComboBox = QComboBox()
        self.topicComboBox.addItem(self.topics)
        layout.addWidget(self.topicComboBox)

        # Combo box for finger combinations
        self.fingerComboBox = QComboBox()
        for combo in finger_combinations:
            self.fingerComboBox.addItem(str(combo)) 
        layout.addWidget(self.fingerComboBox)

        self.msgtype = QComboBox()
        self.msgtype.addItem("Pos")
        self.msgtype.addItem("FingersUp")
        layout.addWidget(self.msgtype)
        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(self.accept)
        layout.addWidget(self.okButton)

        self.setLayout(layout)

    def getSelectedTopic(self):
        temp = String()
        temp.data = self.topicComboBox.currentText()
        return temp

    def getSelectedFingerCombination(self):
        array = String()
        array.data = self.fingerComboBox.currentText()
        return array
    
    def getSelectedHand(self):
        hand = String()
        hand.data = self.hand
        return hand
    
    def getMsgType(self): 
        temp = String()
        temp.data = self.msgtype.currentText()
        return temp