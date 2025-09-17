from datetime import time


def test_dark_theme_by_time():
    """
    Test the correctness of switching the dark theme on the website depending on the time of day
    """
    current_time = time(hour = 23)
    # Night - from 22:00 to 6:00
    is_dark_theme = None

    if current_time.hour >= 22 or current_time.hour < 6:
        is_dark_theme = True
        print("Dark theme is enabled now!")
    else:
        is_dark_theme = False
        print("Light theme is enabled now!")

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Test the correctness of switching the dark theme on the website
    depending on the time and the user's choice
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    is_dark_theme = None

    if dark_theme_enabled_by_user is True:
        is_dark_theme = True
        print("User enabled dark theme.")
    elif dark_theme_enabled_by_user is False:
        is_dark_theme = False
        print("User disabled dark theme.")
    else:
        if current_time.hour >= 22 or current_time.hour < 6:
            is_dark_theme = True
            print("Dark theme enabled by time.")
        else:
            is_dark_theme = False
            print("Dark theme disabled by time.")

    assert is_dark_theme is True



def test_find_suitable_user():
    """
    Find the suitable user according to the conditions in the list of users
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # Find the user with the name "Olga"
    for user in users:
        if user["name"] == "Olga":
            suitable_user = user
            print(suitable_user)
            assert suitable_user == {"name": "Olga", "age": 45}

    # Find all users under 20 years old
    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)

    print(suitable_users)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Function for readable output
def make_readable(func, *values, **named):
    # Transform function name
    func_name = func.__name__.replace("_", " ").title()

    # Collect all arguments into a list
    collected = []
    for v in values:
        collected.append(v)
    for v in named.values():
        collected.append(v)

    # Make the final string
    args_str = ", ".join(str(x) for x in collected)
    result = f"{func_name} [{args_str}]"

    print(result)
    return result


def test_readable_function():
    open_browser(browser_name = "Chrome")
    go_to_companyname_homepage(page_url = "https://companyname.com")
    find_registration_button_on_login_page(
        page_url = "https://companyname.com/login", button_text = "Register"
    )


def open_browser(browser_name):
    actual_result = make_readable(open_browser, browser_name = browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = make_readable(go_to_companyname_homepage, page_url = page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = make_readable(
        find_registration_button_on_login_page,
        page_url = page_url,
        button_text = button_text
    )
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
