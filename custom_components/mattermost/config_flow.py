"""Config flow for Mattermost integration."""

from __future__ import annotations

import logging
from typing import Any

import mattermost
import voluptuous as vol
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_ACCESS_TOKEN, CONF_FRIENDLY_NAME, CONF_URL
from homeassistant.exceptions import HomeAssistantError

from .const import DOMAIN, CONF_CHANNEL

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({
    vol.Required(CONF_FRIENDLY_NAME): str,
    vol.Required(CONF_URL): str,
    vol.Required(CONF_ACCESS_TOKEN) : str,
    vol.Required(CONF_CHANNEL) :str
})

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

                await self.test_credentials (info)

            except LoginFailed as exception:
                _LOGGER.error(exception)
                errors["base"] = "auth"
            except Exception:
                _LOGGER.exception("Unexpected exception.")
                errors["base"] = "unknown"
            else:
                return self.async_create_entry(title=info[CONF_FRIENDLY_NAME], data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=CONFIG_SCHEMA, errors=errors
        )

    async def test_credentials (self, info: dict[str, Any]) -> None:
        """Validate provided credentials."""

        # Create API instance
        mm = mattermost.MMApi(info[CONF_URL])
        uid = mm.login(bearer=info[CONF_ACCESS_TOKEN])

        if uid is None:
            raise LoginFailed

        mm.logout()

class LoginFailed(HomeAssistantError):
    """Error to indicate that we cannot log in to Mattermost."""
