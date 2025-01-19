from behave import when
from selenium import webdriver

@when('I click on the "{button_name}" button')
def step_impl(context, button_name):
    """
    This step clicks on a button with the specified name on the webpage.
    """
    button = context.browser.find_element_by_name(button_name)
    button.click()

from behave import then

@then('I should see "{text}" on the page')
def step_impl(context, text):
    """
    This step verifies if a specific text appears on the page.
    """
    body_text = context.browser.page_source
    assert text in body_text, f"Expected '{text}' to be present on the page."

from behave import then

@then('I should not see "{text}" on the page')
def step_impl(context, text):
    """
    This step verifies if a specific text is not present on the page.
    """
    body_text = context.browser.page_source
    assert text not in body_text, f"Expected '{text}' not to be present on the page."

from behave import then

@then('I should see the message "{message}"')
def step_impl(context, message):
    """
    This step verifies if a specific message is present on the page.
    """
    body_text = context.browser.page_source
    assert message in body_text, f"Expected message '{message}' to be present on the page."
