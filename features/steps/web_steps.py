@when('I click the "Submit" button')
def step_impl(context):
    context.driver.find_element_by_id("submit").click()

@then('I should see the text "{text}"')
def step_impl(context, text):
    assert text in context.driver.page_source
