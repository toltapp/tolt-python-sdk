import httpx
import pytest

from tolt import NotFoundError, ToltApi

PARTNER = {
    "id": "part_1",
    "email": "sam@example.com",
    "status": "active",
    "created_at": "2026-01-01T00:00:00Z",
    "updated_at": "2026-01-01T00:00:00Z",
    "custom_fields": [],
}


def client_for(handler) -> ToltApi:
    return ToltApi(token="tok_test", base_url="https://api.test", httpx_client=httpx.Client(transport=httpx.MockTransport(handler)))


def test_get_sends_auth_and_parses_the_response() -> None:
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"success": True, "message": "ok", "data": PARTNER})

    partner = client_for(handler).partners.get(id="part_1").data

    assert partner.id == "part_1"
    assert seen[0].url == "https://api.test/v2/partners/part_1"
    assert seen[0].headers["authorization"] == "Bearer tok_test"


def test_error_status_maps_to_its_error_class() -> None:
    body = {"success": False, "message": "Partner not found", "code": "not_found", "doc_url": "https://docs.tolt.com/errors#not_found"}

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(404, json=body, headers={"Request-Id": "req_1"})

    with pytest.raises(NotFoundError) as caught:
        client_for(handler).partners.get(id="part_missing")

    assert caught.value.status_code == 404
    assert caught.value.headers is not None and caught.value.headers["request-id"] == "req_1"


def test_timeouts_surface_as_httpx_timeouts() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("timed out", request=request)

    with pytest.raises(httpx.TimeoutException):
        client_for(handler).partners.get(id="part_1", request_options={"max_retries": 0})
