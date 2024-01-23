from enum import Enum

class Outcome(Enum):
    PROGRESS = "Progress"
    TRAILER = "Progress (Module Trailer)"
    RETRIEVER = "Do not Progress - module retriever"
    EXCLUDE = "Exclude"