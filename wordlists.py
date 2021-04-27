import os

class words:
    def __init__(self):
        self.easywords = os.getenv('EASY_WORDS')
        self.mediumwords = os.getenv('MEDIUM_WORDS')
        self.hardwords = os.getenv('HARD_WORDS')
        self.crazywords = os.getenv('CRAZY_WORDS')
