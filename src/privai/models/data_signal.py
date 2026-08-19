from enum import Enum
from privai.models.sensitivity import SensitivityLevel

class DataSignal(Enum):
    EMAIL = "email"
    PHONE = "phone"
    LOCATION = "location"
    DEVICE_ID = "device_id"
    SESSION_ID = "session_id"
    AUTH_TOKEN = "auth_token"

    @property
    def sensitivity(self) -> SensitivityLevel:
        sensitivity_map = {
            DataSignal.EMAIL: SensitivityLevel.MEDIUM,
            DataSignal.PHONE: SensitivityLevel.HIGH,
            DataSignal.LOCATION: SensitivityLevel.HIGH,
            DataSignal.DEVICE_ID: SensitivityLevel.MEDIUM,
            DataSignal.SESSION_ID: SensitivityLevel.HIGH,
            DataSignal.AUTH_TOKEN: SensitivityLevel.CRITICAL,
        }

        return sensitivity_map[self]