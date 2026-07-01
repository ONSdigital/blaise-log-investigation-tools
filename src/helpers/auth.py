from __future__ import annotations

from typing import cast

import google.auth
import google.auth.credentials


def get_gcp_credentials_and_project() -> tuple[
    google.auth.credentials.Credentials, str
]:
    credentials, project = cast(
        tuple[google.auth.credentials.Credentials, str | None],
        google.auth.default(),  # type: ignore[no-untyped-call]
    )
    if not project:
        raise ValueError(
            "No GCP project could be inferred. "
            "Run `gcloud config set project <project-id>`"
        )
    return credentials, project
