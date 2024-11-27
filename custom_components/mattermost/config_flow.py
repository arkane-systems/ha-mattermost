"""Config flow for Mattermost integration."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_NAME

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({vol.Required(CONF_NAME): str})


class MattermostFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle the configuration flow for Mattermost."""

    VERSION = 0
    MINOR_VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a flow initiated by the user."""
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                info = user_input
            except Exception:
                _LOGGER.exception("Unexpected exception.")
                errors["base"] = "unknown"
            else:
                return self.async_create_entry(title=info["title"], data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=CONFIG_SCHEMA, errors=errors
        )


# class PlaceholderHub:
#     """Placeholder class to make tests pass.
#
#     TODO Remove this placeholder class and replace with things from your PyPI package.
#     """
#
#     def __init__(self, host: str) -> None:
#         """Initialize."""
#
#     async def authenticate(self, username: str, password: str) -> bool:
#         """Test if we can authenticate with the host."""
#
#
# async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
#     """Validate the user input allows us to connect.
#
#     Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
#     """
#     # TODO validate the data can be used to set up a connection.
#
#     # If your PyPI package is not built with async, pass your methods
#     # to the executor:
#     # await hass.async_add_executor_job(
#
#
#     if not await hub.authenticate(data[CONF_USERNAME], data[CONF_PASSWORD]):
#         raise InvalidAuth
#
#     # If you cannot connect:
#     # throw CannotConnect
#     # If the authentication is wrong:
#     # InvalidAuth
#
#     # Return info that you want to store in the config entry.
#
#
# class ConfigFlow(ConfigFlow, domain=DOMAIN):
#     """Handle a config flow for Mattermost."""
#
#
#     async def async_step_user(
#         self, user_input: dict[str, Any] | None = None
#     ) -> ConfigFlowResult:
#         """Handle the initial step."""
#         if user_input is not None:
#
#         return self.async_show_form(
#
#
# class CannotConnect(HomeAssistantError):
#     """Error to indicate we cannot connect."""
#
#
# class InvalidAuth(HomeAssistantError):
#     """Error to indicate there is invalid auth."""
