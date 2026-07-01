from __future__ import annotations

import pytest

from helpers.auth import get_gcp_credentials_and_project


def test_get_credentials_uses_inferred_project(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_credentials = object()

    def fake_default() -> tuple[object, str]:
        return fake_credentials, "inferred-project"

    monkeypatch.setattr("helpers.auth.google.auth.default", fake_default)

    credentials, project = get_gcp_credentials_and_project()

    assert credentials is fake_credentials
    assert project == "inferred-project"


def test_get_credentials_raises_when_no_project(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_default() -> tuple[object, None]:
        return object(), None

    monkeypatch.setattr("helpers.auth.google.auth.default", fake_default)

    with pytest.raises(ValueError, match="No GCP project could be inferred"):
        get_gcp_credentials_and_project()
        get_gcp_credentials_and_project()
