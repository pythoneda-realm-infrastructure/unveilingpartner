"""
pythonedarealminfrastructureunveilingpartner/pythonedaunveilingpartnerdbus/unveiling_partner_dbus_signal_emitter.py

This file defines the UnveilingPartnerDbusSignalEmitter class.

Copyright (C) 2023-today rydnr's pythoneda-realm-infrastructure/unveilingpartner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.event import Event
from pythonedaartifacteventgittagging.tag_credentials_provided import TagCredentialsProvided
from pythonedaartifacteventinfrastructuregittagging.pythonedaartifacteventgittaggingdbus.dbus_tag_credentials_provided import DbusTagCredentialsProvided
from pythonedainfrastructure.pythonedadbus.dbus_signal_emitter import DbusSignalEmitter

import asyncio
from dbus_next.aio import MessageBus
from dbus_next import BusType, Message, MessageType

from typing import Dict, List

class UnveilingPartnerDbusSignalEmitter(DbusSignalEmitter):

    """
    A Port that emits UnveilingPartner events as d-bus signals.

    Class name: UnveilingPartnerDbusSignalEmitter

    Responsibilities:
        - Connect to d-bus.
        - Emit domain events as d-bus signals on behalf of UnveilingPartner.

    Collaborators:
        - PythonEDA: Requests emitting events.
    """
    def __init__(self):
        """
        Creates a new UnveilingPartnerDbusSignalEmitter instance.
        """
        super().__init__()

    def transform_TagCredentialsProvided(self, event: TagCredentialsProvided) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythonedaartifactgittagging.tag_credentials_provided.TagCredentialsProvided
        :return: The event information.
        :rtype: List[str]
        """
        return [ str(event.request_id), event.repository_url, event.branch, event.ssh_username, event.private_key_file.get(), event.private_key_passphrase.get() ]

    def signature_for_TagCredentialsProvided(self, event: TagCredentialsProvided) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythonedaartifacteventgittagging.tag_credentials_provided.TagCredentialsProvided
        :return: The signature.
        :rtype: str
        """
        return 'ssssss'

    def emitters(self) -> Dict:
        """
        Retrieves the configured event emitters.
        :return: A dictionary with the event class name as key, and a dictionary as value. Such dictionary must include the following entries:
          - "interface": the event interface,
          - "busType": the bus type,
          - "transformer": a function capable of transforming the event into a string.
          - "signature": a function capable of returning the types of the event parameters.
        :rtype: Dict
        """
        result = {}
        key = self.fqdn_key(TagCredentialsProvided)
        result[key] = {
                "interface": DbusTagCredentialsProvided,
                "busType": BusType.SYSTEM,
                "transformer": self.transform_TagCredentialsProvided,
                "signature": self.signature_for_TagCredentialsProvided
            }

        return result
