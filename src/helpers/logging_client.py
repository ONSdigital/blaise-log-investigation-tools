from __future__ import annotations

import google.cloud.logging as gcl

from helpers.auth import get_gcp_credentials_and_project


def get_logs_client() -> gcl.Client:
    credentials, project = get_gcp_credentials_and_project()
    return gcl.Client(credentials=credentials, project=project)
