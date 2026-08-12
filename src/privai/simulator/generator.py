import random
from datetime import datetime

from privai.models.request import WebRequest

class RequestSimulator:

    def __init__(self,seed:int=42):
        self.rng = random.Random(seed)

    def generate_request(self,request_id:int) -> WebRequest:
        domain= "example.com"
        method = self.rng.choice(["GET","POST"])
        endpoint = self.rng.choice([
            "/",
            "/products",
            "/api/products",
            "/api/search",
            "/api/profile",
            "/api/analytics",
        ])

        content_type = self.rng.choice([
                "application/json",
                "text/html",
                "application/javascript",
            ])

        payload_size = self.rng.randint(0,1000)

        return WebRequest(
            request_id=request_id,
            timestamp=datetime.now(),
            domain=domain,
            method=method,
            endpoint=endpoint,
            content_type=content_type,
            payload_size=payload_size,
            destination=domain,
        )

    def generate(self,count: int = 100):
        return [self.generate_request(i) for i in range(count)]

    