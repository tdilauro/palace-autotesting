from __future__ import annotations

import re
from typing import TYPE_CHECKING

from autotests import PalaceManager

if TYPE_CHECKING:
    from playwright.sync_api import Locator, Page


class AdminLoginPage:

    PATH = "/admin/sign_in"
    FORM_METHOD = "post"
    FORM_ACTION = "/admin/sign_in_with_password"

    def __init__(self, page: Page, base_url: str = None):
        self.page = page
        pm = PalaceManager(base_url)
        self.url = pm.url_for(self.PATH)
        self.url_re = re.compile(
            f"{pm.url_for(self.PATH)}" + r"\?redirect=.*", re.IGNORECASE
        )
        login_form = self.page.locator(
            f"form[method='{self.FORM_METHOD}'][action='{self.FORM_ACTION}']"
        )
        self.login_form_locators = {
            "self": login_form,
            "username": login_form.locator("input[name='email']"),
            "password": login_form.locator("input[name='password']"),
            "submit_button": login_form.locator("button[type='submit']"),
        }

    def img_locator(self, text: str) -> Locator:
        return self.page.locator(f"img[alt='{text}']")

    def load(self) -> None:
        self.page.goto(self.url)
