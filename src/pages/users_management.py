import logging
import traceback
from logging import getLogger

import streamlit as st

import utils

# CONFIGURATION CONSTANTS
# App Configuration, for st.set_page_config, as it must be the first function called
APP_NAME = "Users Management"
FAVICON = "🔑"  # icon or filename
LAYOUT = "centered"  # "centered" or "wide"
# Config file
APP_CONFIG_FILE = "./config/app_config.yaml"

def reset_password(authenticator, alert_placeholder):
    if utils.check_required_session_state_keys(required_keys=["username"]):
        if authenticator.reset_password(st.session_state["username"]):
            alert_placeholder.success("Password modified successfully")


def update_details(authenticator, alert_placeholder):
    if utils.check_required_session_state_keys(required_keys=["username"]):
        if authenticator.update_user_details(st.session_state["username"]):
            alert_placeholder.success("Details modified successfully")


def forgot_password(authenticator, alert_placeholder):
    username_of_forgotten_password, email_of_forgotten_password, new_random_password = (
        authenticator.forgot_password()
    )
    if username_of_forgotten_password:
        alert_placeholder.success("New password to be sent securely")
        # The developer should securely transfer the new password to the user.
        st.write(new_random_password)
    elif username_of_forgotten_password == False:
        alert_placeholder.error("Username not found")


def forgot_username(authenticator, alert_placeholder):
    username_of_forgotten_username, email_of_forgotten_username = (
        authenticator.forgot_username()
    )
    if username_of_forgotten_username:
        st.success("Username to be sent securely")
        # The developer should securely transfer the username to the user.
        st.write(username_of_forgotten_username)
    elif username_of_forgotten_username == False:
        alert_placeholder.error("Email not found")


def add_user(authenticator, alert_placeholder):
    email_of_registered_user, username_of_registered_user, name_of_registered_user = (
        authenticator.register_user(preauthorization=False)
    )
    if email_of_registered_user:
        alert_placeholder.success("User registered successfully")

def show_user_details(email: str):
    if utils.check_required_session_state_keys(required_keys=["username", "name"]):
        with st.container(border=True):
            st.write("## User details")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Username**:")
                st.write(f"**Name**:")
                st.write(f"**Email**:")
            with col2:
                st.write(f"{st.session_state["username"]}")
                st.write(f"{st.session_state["name"]}")
                st.write(f"{email}")

def main(auth_file, auth_config, authenticator, alert_placeholder):
    """Main user management function"""
    tabs = [
        "Reset Password",
        "Update Details",
        "Forgot Password",
        "Forgot Username",
        "Add User",
        "Account Details",
    ]
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(tabs)
    
    try:
        with tab1:
            reset_password(
                authenticator=authenticator,
                alert_placeholder=alert_placeholder,
            )
            utils.save_yaml(file_path=auth_file, data=auth_config)
        with tab2:
            update_details(
                authenticator=authenticator,
                alert_placeholder=alert_placeholder,
            )
            utils.save_yaml(file_path=auth_file, data=auth_config)
        with tab3:
            forgot_password(
                authenticator=authenticator,
                alert_placeholder=alert_placeholder,
            )
            utils.save_yaml(file_path=auth_file, data=auth_config)
        with tab4:
            forgot_username(
                authenticator=authenticator,
                alert_placeholder=alert_placeholder,
            )
            utils.save_yaml(file_path=auth_file, data=auth_config)
        with tab5:
            add_user(
                authenticator=authenticator,
                alert_placeholder=alert_placeholder,
            )
            utils.save_yaml(file_path=auth_file, data=auth_config)
        with tab6:
            if utils.check_required_session_state_keys(required_keys=["username"]):
                email = utils.get_email_for_username(file_path=auth_file, username=st.session_state["username"])
                show_user_details(email=email)
    except Exception as e:
        alert_placeholder.error(e)
        print(e)
        print(traceback.format_exc())
        print(st.session_state["username"])
        # import os
        # os._exit(0)
        # st.stop()
        # time.sleep(3600)


if __name__ == "__main__":
    st.set_page_config(page_title=APP_NAME, page_icon=FAVICON)

    app_logger = getLogger()
    app_logger.addHandler(logging.StreamHandler())

    # # App configuration
    # if "config" not in st.session_state:
    #     st.session_state.config = utils.load_yaml(file_path=APP_CONFIG_FILE)

    # # Load languages
    # utils.load_languages(st.session_state.config)

    # Authenticator
    if "auth_config" not in st.session_state:
        st.session_state.auth_config = utils.load_yaml(
            st.session_state.config["config"]["auth"]
        )
    authenticator = utils.get_authenticator(st.session_state.auth_config)

    # App Title
    st.write("# Users Management")

    # Alert messages placeholder
    alert_placeholder = st.empty()

    # Authenticator widget
    login_placeholder = st.empty()
    with login_placeholder:
        authenticator.login()

    if st.session_state["authentication_status"]:
        login_placeholder.empty()
        authenticator.logout(location="sidebar")
        main(
            auth_file=st.session_state.config["config"]["auth"],
            auth_config=st.session_state.auth_config,
            authenticator=authenticator,
            alert_placeholder=alert_placeholder,
        )
    elif st.session_state["authentication_status"] is False:
        alert_placeholder.error("Username/password is incorrect")
    elif st.session_state["authentication_status"] is None:
        alert_placeholder.warning("Please enter your username and password")
