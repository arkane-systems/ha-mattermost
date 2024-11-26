"""The Mattermost integration."""

from __future__ import annotations

import logging

from homeassistant.auth.providers.command_line import CONFIG_SCHEMA
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform, CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .const import (
    DOMAIN,

    DATA_HASS_CONFIG
)

_LOGGER = logging.getLogger(__name__)

# Platforms which this integration supports.
PLATFORMS: list[Platform] = [Platform.NOTIFY]

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Mattermost integration."""
    _LOGGER.info("Mattermost integration started.")

    hass.data[DATA_HASS_CONFIG] = config
    return True

async def async_setup_entry (hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up a Mattermost instance from a config entry."""
    _LOGGER.info("Set up Mattermost instance " + entry.data[CONF_NAME])

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry (hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Shut down and unload a Mattermost instance and its config entry."""

    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

# # TODO Create ConfigEntry type alias with API object
# # TODO Rename type alias and update all entry annotations
# type New_NameConfigEntry = ConfigEntry[MyApi]  # noqa: F821
#
#
# # TODO Update entry annotation
# async def async_setup_entry(hass: HomeAssistant, entry: New_NameConfigEntry) -> bool:
#     """Set up Mattermost from a config entry."""
#
#     # TODO 1. Create API instance
#     # TODO 2. Validate the API connection (and authentication)
#     # TODO 3. Store an API object for your platforms to access
#     # entry.runtime_data = MyAPI(...)
#
#     await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
#
#     return True
