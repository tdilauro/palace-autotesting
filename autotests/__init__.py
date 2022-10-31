from __future__ import annotations

import os
from urllib.parse import urljoin

BASE_URL_ENV_VAR = "TPP_CM_BASE_URL"


class PalaceManager:
    def __init__(self, base_url: str = None):
        self._base_url = (base_url or os.environ[BASE_URL_ENV_VAR]).rstrip("/")

    @property
    def base_url(self) -> str:
        return self._base_url

    def url_for(self, path: str) -> str:
        return urljoin(self._base_url, path.lstrip("/"))
