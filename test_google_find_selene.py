from selene.support.shared import browser
from selene import be, have


browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

# browser.open('https://google.com')
# query = browser.element('//input[@name="q"]').send_keys("selene")
# query.press_enter()
#
# list_of_results = browser.elements('//div[@data-sokoban-container]')
# element_with_certain_text = list_of_results.filtered_by_their('h3', have.text('yashaka/selene'))
# element_with_certain_text.should(have.text('yashaka/selene'))
