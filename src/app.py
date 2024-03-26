import streamlit as st

import utils

# CONFIGURATION CONSTANTS
# App Configuration, for st.set_page_config, as it must be the first function called
APP_NAME = "Streamlit Authenticator Demo"
FAVICON = "🏠"  # icon or filename
LAYOUT = "centered"  # "centered" or "wide"
# Config file
APP_CONFIG_FILE = "./config/app_config.yaml"


def main(authenticator):
    """Main Application function"""
    # User "block"
    # User name
    st.sidebar.write(
        f'**{st.session_state.strings["login"]["welcome"]}** {st.session_state["name"]}'
    )
    # Logout button
    authenticator.logout(
        st.session_state.strings["login"]["logout"], location="sidebar"
    )
    # Horizontal separator
    st.sidebar.divider()

    # Language "block"
    language_options = list(st.session_state.languages.keys())
    st.sidebar.selectbox(
        label=st.session_state.strings["languages"]["select"],
        options=language_options,
        index=language_options.index(st.session_state.current_language),
        key="current_language",
        on_change=utils.update_language,
    )

    # Main content
    with st.container(border=False):
        st.write(f'# {st.session_state.strings["main"]["title"]} 👋')
        st.write(f'## {st.session_state.strings["main"]["content"]}')


if __name__ == "__main__":
    # Set app basic configuration
    st.set_page_config(
        page_title=APP_NAME,
        page_icon=FAVICON,
        layout=LAYOUT,
    )

    # App configuration
    if "config" not in st.session_state:
        st.session_state.config = utils.load_yaml(file_path=APP_CONFIG_FILE)

    # Load languages
    utils.load_languages_files(st.session_state.config)

    # Authenticator
    if "auth_config" not in st.session_state:
        st.session_state.auth_config = utils.load_yaml(
            st.session_state.config["config"]["auth"]
        )
    authenticator = utils.get_authenticator(st.session_state.auth_config)

    # st.title(st.session_state.strings["title"])

    # Alert messages placeholder
    alert_placeholder = st.empty()

    # Login
    authenticator.login()

    if st.session_state["authentication_status"]:
        main(authenticator=authenticator)
    elif st.session_state["authentication_status"] is False:
        alert_placeholder.error("Username/password is incorrect")
    elif st.session_state["authentication_status"] is None:
        alert_placeholder.warning("Please enter your username and password")
