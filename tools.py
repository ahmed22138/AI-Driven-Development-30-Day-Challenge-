import json
from agents import function_tool

USER_PROFILE_FILE = "user_profile.json"

@function_tool
def read_user_profile() -> dict:
    """
    Reads the user profile from user_profile.json.
    Returns an empty dictionary if the file does not exist.
    """
    try:
        with open(USER_PROFILE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@function_tool
def update_user_profile(key: str, value: str) -> str:
    """
    Updates a specific key-value pair in the user profile and saves it to user_profile.json.
    Returns a confirmation message.
    """
    user_profile = read_user_profile()
    user_profile[key] = value
    with open(USER_PROFILE_FILE, "w") as f:
        json.dump(user_profile, f, indent=4)
    return f"User profile updated: {key} = {value}"
