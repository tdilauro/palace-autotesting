from __future__ import annotations

import os
import re
from typing import TYPE_CHECKING

from playwright.sync_api import expect

if TYPE_CHECKING:
    from playwright.sync_api import Page

BASE_URL_ENVVAR = "TPP_CM_BASE_URL"
ADMIN_UI_HOME_PATH = "/admin/web"
ADMIN_UI_LOGIN_PATH = "/admin/sign_in"
WEB_APP_TITLE = "Palace Collection Manager"


def test_home_page(page: Page) -> None:
    cm_base_url = os.environ[BASE_URL_ENVVAR].rstrip("/")
    admin_ui_home_page = f"{cm_base_url}{ADMIN_UI_HOME_PATH}"
    admin_ui_signin_page = re.compile(
        f"{cm_base_url}{ADMIN_UI_LOGIN_PATH}" + r"\?redirect=.*", re.IGNORECASE
    )

    # Given a link to a CM admin UI home page,
    # when visiting the page,
    page.goto(admin_ui_home_page)

    # ...we are redirected to the login page.
    # The login page has a title.
    expect(page).to_have_title(f"{WEB_APP_TITLE}")
    expect(page).to_have_url(admin_ui_signin_page)

    # The login page has a product logo...
    logo_locator = page.locator(f"img[alt='{WEB_APP_TITLE}']")
    assert logo_locator.get_attribute("src") is not None

    # ...a login form with username and password input fields
    # and a submit button.
    login_form = page.locator(
        "form[method='post'][action='/admin/sign_in_with_password']"
    )
    username_field = login_form.locator("input[name='email']")
    password_field = login_form.locator("input[name='password']")
    submit_button = login_form.locator("button[type='submit']")

    expect(login_form).not_to_be_empty()

    expect(username_field).to_have_attribute("type", "text")
    expect(username_field).to_be_enabled()
    expect(username_field).to_be_empty()

    expect(password_field).to_have_attribute("type", "password")
    expect(password_field).to_be_enabled()
    expect(password_field).to_be_empty()

    expect(submit_button).to_be_enabled()
    expect(submit_button).to_have_text("sign in", use_inner_text=True, ignore_case=True)
