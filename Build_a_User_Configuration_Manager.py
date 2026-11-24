#In this lab, you will build a User Configuration Manager 
#that allows users to manage their settings such as theme, language, 
#and notifications. You will implement functions to add, update, delete, and view user settings.

def add_setting(settings, setting_pair):
    key, value = setting_pair
    key = str(key).lower()
    value = str(value).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, setting_pair):
    key, value = setting_pair
    key = str(key).lower()
    value = str(value).lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    key = str(key).lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    output = "Current User Settings:\n"
    for key, value in settings.items():
        output += f"{key.capitalize()}: {value}\n"
    
    return output


# Dictionary for testing
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

print(view_settings(test_settings))
print(add_setting(test_settings, ('language', 'vietnamese')))