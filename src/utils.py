import streamlit as st
import streamlit_authenticator as stauth
import yaml


# YAML
def load_yaml(file_path: str) -> dict[str, any]:
    """Loads the content of a yaml file in a string or a dict.

    Args:
        file_path (str): Name of the yaml file to load.

    Returns:
        dict[str, any]: Content of the yaml file.
    """
    with open(file=file_path, mode="r") as file:
        data = yaml.load(file, Loader=yaml.SafeLoader)
    return data


def save_yaml(file_path: str, data: dict[str, any]) -> None:
    """Saves the content of a dict to a yaml file.

    Args:
        file_path (str): Name of the yaml file to write.
        data (Dict[str, any]): Dict with the data to write.
    """
    with open(file=file_path, mode="w") as file:
        yaml.dump(data, file, default_flow_style=False)


# Languages
def load_languages_files(config: dict[str, any]):
    """Load the languages strings into streamlit session_state.
    Looks for the keys 'languages' and 'default_language',
    like in the following yaml sample:
        languages:
            [language_code]: [strings_yaml_file]
        default_language: [language_code]

    Args:
        config (dict[str, any]): Configuration file loaded in a dictionary.
    """
    # Session State keys
    languages_key = "languages"
    strings_key = "strings"
    # Initializing the "languages" object in the session_state
    if languages_key not in st.session_state:
        st.session_state[languages_key] = {}
    # Loading the languages files into the session_state object
    for language, file in config[languages_key].items():
        st.session_state[languages_key][language] = load_yaml(file)
    # Initializing the strings
    if strings_key not in st.session_state:
        st.session_state[strings_key] = st.session_state[languages_key][
            config["default_language"]
        ]


def update_language() -> None:
    """Updates the 'st.session_state.strings' to the strings of the 'st.session_state.language'"""
    selected_language = st.session_state.language
    st.session_state.strings = st.session_state.languages[selected_language]


# Streamlit
def get_horizontal_row() -> str:
    """
    Generates an HTML string representing a horizontal row.

    This function is useful for adding a visual separation in Streamlit applications using HTML.

    Returns:
        str: An HTML string that renders a horizontal rule (<hr />) when used with an HTML renderer.
    """
    return """<hr />"""


def check_required_session_state_keys(required_keys: list[str]) -> bool:
    """Check if specified keys exist and are not None in Streamlit's session state.

    Args:
        required_keys (List[str]): A list of keys to check in the session state.

    Returns:
        bool: True if all specified keys exist and their values are not None, False otherwise.
    """
    return all(st.session_state.get(key) is not None for key in required_keys)


# Streamlit-Authenticator
def get_email_for_username(file_path: str, username: str) -> str:
    """Returns the email address for a given username.

    Args:
        file_path (str): File path for the streamlit-authenticator configuration file.
        username (str): Username of a user present in streamlit-authenticator configuration file.

    Returns:
        str: Email address for the given username.
    """
    data = load_yaml(file_path=file_path)
    return data["credentials"]["usernames"][username]["email"]


def get_authenticator(config: dict) -> stauth.Authenticate:
    """Returns a streamlit-authenticator Authenticate object from a streamlit-authenticator dictionary.

    Args:
        config (dict): streamlit-authenticator dictionary.

    Returns:
        stauth.Authenticate: The streamlit-authenticator Authenticate object.
    """
    return stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
    )
