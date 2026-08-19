from privai.models.data_signal import DataSignal
from privai.models.sensitivity import SensitivityLevel


def test_email_has_medium_sensitivity():
    assert DataSignal.EMAIL.sensitivity == SensitivityLevel.MEDIUM


def test_auth_token_has_critical_sensitivity():
    assert DataSignal.AUTH_TOKEN.sensitivity == SensitivityLevel.CRITICAL