from privai.simulator.generator import RequestSimulator
from privai.models.request import WebRequest
from privai.models.data_signal import DataSignal


def test_generator_creates_requested_number_of_requests():
    simulator = RequestSimulator(seed=42)
    requests = simulator.generate(10)
    assert len(requests) == 10

def test_generated_request_has_required_fields():
    simulator = RequestSimulator(seed=42)
    request: WebRequest = simulator.generate_request(1)

    assert request.request_id == 1
    assert request.domain == "example.com"
    assert request.method in {"GET", "POST"}
    assert request.payload_size >= 0

def test_request_can_contain_data_signals():
    simuator = RequestSimulator(seed=42)
    request = simuator.generate_request(1)

    request.datasignals = [DataSignal.EMAIL,DataSignal.LOCATION]

    assert DataSignal.EMAIL in request.datasignals
    assert DataSignal.LOCATION in request.datasignals