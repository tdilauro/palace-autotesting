from __future__ import annotations

from typing import TYPE_CHECKING

from autotests import PalaceManager

if TYPE_CHECKING:
    from playwright.sync_api import Page


class AdminHomePage:

    PATH = "/admin/web"

    def __init__(self, page: Page, base_url: str = None):
        self.page = page
        self.url = PalaceManager(base_url).url_for(self.PATH)

    def load(self) -> None:
        self.page.goto(self.url)
