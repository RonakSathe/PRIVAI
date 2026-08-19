from dataclasses import dataclass,field
from datetime import datetime
from privai.models.data_signal import DataSignal



@dataclass
class WebRequest:
    request_id: int
    timestamp: datetime
    domain: str
    method: str
    endpoint: str
    content_type: str
    payload_size: int
    destination: str
    datasignals: list[DataSignal] = field(default_factory=list)
    

