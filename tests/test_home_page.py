from __future__ import annotations

from typing import TYPE_CHECKING

from playwright.sync_api import expect

from autotests.pages.admin_home import AdminHomePage
from autotests.pages.admin_login import AdminLoginPage

if TYPE_CHECKING:
    from playwright.sync_api import Page

ADMIN_UI_LOGIN_PATH = "/admin/sign_in"
WEB_APP_TITLE = "Palace Collection Manager"


def test_home_page(page: Page) -> None:
    home_page = AdminHomePage(page)
    login_page = AdminLoginPage(page)

    # Given a link to a CM admin UI home page,
    # when visiting the page,
    home_page.load()

    # ...we are redirected to the login page.
    # The login page has a title.
    expect(page).to_have_title(f"{WEB_APP_TITLE}")
    expect(page).to_have_url(login_page.url_re)

    # The login page has a product logo...
    logo = login_page.img_locator(WEB_APP_TITLE)
    assert logo.get_attribute("src") is not None

    # ...a login form with username and password input fields
    # and a submit button.
    form = login_page.login_form_locators
    expect(form["self"]).not_to_be_empty()

    expect(form["username"]).to_have_attribute("type", "text")
    expect(form["username"]).to_be_enabled()
    expect(form["username"]).to_be_empty()

    expect(form["password"]).to_have_attribute("type", "password")
    expect(form["password"]).to_be_enabled()
    expect(form["password"]).to_be_empty()

    expect(form["submit_button"]).to_be_enabled()
    expect(form["submit_button"]).to_have_text(
        "sign in", use_inner_text=True, ignore_case=True
    )
