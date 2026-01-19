from dataclasses import dataclass


@dataclass
class CognitiveFunction:
    type: str = "X" # N/S, T/F
    attitude: str = "X" # e/i

    def __str__(self):
        return f"{self.type}{self.attitude}"


opposite = {
    "I": "E",
    "E": "I",
    "N": "S",
    "S": "N",
    "T": "F",
    "F": "T",
    "P": "J",
    "J": "P",
}
