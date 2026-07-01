from __future__ import annotations

import pytest

from helpers.logging_client import get_logs_client


def test_get_logs_client_uses_credentials_and_project(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fake_credentials = object()
    observed: dict[str, object] = {}

    def fake_get_creds() -> tuple[object, str]:
        return fake_credentials, "resolved-project"

    class FakeClient:
        def __init__(self, *, credentials: object, project: str) -> None:
            observed["credentials"] = credentials
            observed["project"] = project

    monkeypatch.setattr(
        "helpers.logging_client.get_gcp_credentials_and_project", fake_get_creds
    )
    monkeypatch.setattr("helpers.logging_client.gcl.Client", FakeClient)

    client = get_logs_client()

    assert isinstance(client, FakeClient)
    assert observed == {
        "credentials": fake_credentials,
        "project": "resolved-project",
    }
