from privai.detector.data_detector import DataDetector
from privai.models.data_signal import DataSignal

def test_detects_email():
    detector = DataDetector()

    signals = detector.detect("Contact me at alice@example.com")

    assert DataSignal.EMAIL in signals

def test_does_not_detect_email_when_absent():
    detector = DataDetector()

    signals = detector.detect(
        "This request contain no email"
    )

    assert DataSignal.EMAIL not in signals