from selenium.webdriver.support.ui import Select


def select_option(dropdown, criteria, value):
    select = Select(dropdown)

    if criteria == "text":
        select.select_by_visible_text(value)
    elif criteria == "index":
        select.select_by_index(int(value))  # Convert value to int for index selection
    elif criteria == "value":
        select.select_by_value(value)
    else:
        raise ValueError("Invalid criteria. Use 'text', 'index', or 'value'.")
