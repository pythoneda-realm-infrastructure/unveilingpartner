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
from dbus_next import BusType
from pythoneda.event import Event
from pythonedaartifacteventchanges.change_staging_requested import ChangeStagingRequested
from pythonedaartifacteventgittagging.tag_credentials_provided import TagCredentialsProvided
from pythonedaartifacteventinfrastructurechanges.pythonedaartifacteventchangesdbus.dbus_change_staging_requested import DbusChangeStagingRequested
from pythonedaartifacteventinfrastructuregittagging.pythonedaartifacteventgittaggingdbus.dbus_tag_credentials_provided import DbusTagCredentialsProvided
from pythonedainfrastructure.pythonedadbus.dbus_signal_emitter import DbusSignalEmitter
from typing import Dict

class UnveilingPartnerDbusSignalEmitter(DbusSignalEmitter):

    """
    A Port that emits UnveilingPartner events as d-bus signals.

    Class name: UnveilingPartnerDbusSignalEmitter

    Responsibilities:
        - Connect to d-bus.
        - Emit domain events as d-bus signals on behalf of UnveilingPartner.

    Collaborators:
        - pythonedaapplication.pythoneda.PythonEDA: Requests emitting events.
        - pythonedaartifacteventinfrastructurechanges.pythonedaartifacteventchangesdbus.dbus_change_staging_requested.DbusChangeStagingRequested
        - pythonedaartifacteventinfrastructuregittagging.pythonedaartifacteventgittaggingdbus.dbus_tag_credentials_provided.DbusTagCredentialsProvided
        -
    """
    def __init__(self):
        """
        Creates a new UnveilingPartnerDbusSignalEmitter instance.
        """
        super().__init__()

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
        key = self.fqdn_key(ChangeStagingRequested)
        result[key] = {
                "interface": DbusChangeStagingRequested,
                "busType": BusType.SYSTEM,
                "transformer": DbusChangeStagingRequested.transform_ChangeStagingRequested,
                "signature": DbusChangeStagingRequested.signature_for_ChangeStagingRequested
            }
        key = self.fqdn_key(TagCredentialsProvided)
        result[key] = {
                "interface": DbusTagCredentialsProvided,
                "busType": BusType.SYSTEM,
                "transformer": DbusTagCredentialsProvided.transform_TagCredentialsProvided,
                "signature": DbusTagCredentialsProvided.signature_for_TagCredentialsProvided
            }

        return result
