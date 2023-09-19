from selene.support.shared import browser
from selene import be, have


def test_check_text_insearch_browser(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element(".LC20lb.MBeuO.DKV0Md").should(have.text('User-oriented Web UI browser tests'))


def test_empty_search_result():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('nfkjdsgnfdgkjfbsdjhgbkjfdbjkgasd').press_enter()
    browser.element('#search').should(be.absent)
    browser.element('.card-section [aria-level="3"]').should(have.text('По запросу nfkjdsgnfdgkjfbsdjhgbkjfdbjkgasd '
                                                                       'ничего не найдено.'))