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
from pythonedainfrastructure.pythonedadbus.dbus_signal_emitter import DbusSignalEmitter

import asyncio
from dbus_next.aio import MessageBus
from dbus_next import BusType, Message, MessageType

from typing import Dict

class UnveilingPartnerDbusSignalEmitter(DbusSignalEmitter):

    """
    A Port that emits UnveilingPartner events as d-bus signals.

    Class name: UnveilingPartnerDbusSignalEmitter

    Responsibilities:
        - Connect to d-bus.
        - Emit domain events as d-bus signals on behalf of UnveilingPartner.

    Collaborators:
        - PythonEDAApplication: Requests emitting events.
    """
    def __init__(self):
        """
        Creates a new UnveilingPartnerDbusSignalEmitter instance.
        """
        super().__init__()

    def transformTagCredentialsProvided(self, event: TagCredentialsProvided) -> str:
        """
        Transforms given event to string.
        :param event: The event to transform.
        :type event: TagCredentialsProvided from pythonedaartifactgittagging.tag_credentials_provided
        :return: The serialized version of the event.
        :rtype: str
        """
        return str(event)

    def emitters(self) -> Dict:
        """
        Retrieves the configured event emitters.
        :return: A dictionary with the event class name as key, and a dictionary as value. Such dictionary must include the following entries:
          - "destination": the event destination,
          - "path": the path,
          - "interface": the interface,
          - "member": the signal name,
          - "transformer": a function capable of transforming the event into a string.
        :rtype: Dict
        """
        return {
            "TagCredentialsProvided": {
                "destination": "pythoneda.artifact.git-tagging",
                "path": "/pythoneda/artifact/git-tagging",
                "interface": "pythoneda.realm.UnveilingPartner",
                "member": "TagCredentialsProvided",
                "transformer": transformTagCredentialsProvided
            }
        }

    async def emit(self, event: Event):
        """
        Emits given event as d-bus signal.
        :param event: The domain event to emit.
        :type event: Event from pythoneda.event
        """
        await super().emit(event)
        emitters = signal_emitters().items()

        if emitters:
            emitter = emitters.get(event.__class__, None)
            if emitter:
                message = Message(
                    destination = emitter["destination"],
                    path = emitter["path"],
                    interface = emitter["interface"],
                    member = emitter["signal"],
                    body = emitter["transformer"](event)
                )
                await bus.send(message)
