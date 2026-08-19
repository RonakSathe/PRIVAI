import re

from privai.models.data_signal import DataSignal


class DataDetector:

    EMAIL_PATTERN = re.compile(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    )

    def detect(self, text: str) -> list[DataSignal]:
        signals = []

        if self.EMAIL_PATTERN.search(text):
            signals.append(DataSignal.EMAIL)

        return signals