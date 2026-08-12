from dataclasses import dataclass
from datetime import datetime

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

