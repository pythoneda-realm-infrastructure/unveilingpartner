"""
pythonedarealminfrastructureunveilingpartner/pythonedaunveilingpartnerdbus/unveiling_partner_dbus_signal_listener.py

This file defines the UnveilingPartnerDbusSignalListener class.

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
from pythonedaartifacteventgittagging.tag_credentials_requested import TagCredentialsRequested
from pythonedaartifacteventinfrastructuregittagging.pythonedaartifacteventgittaggingdbus.dbus_tag_credentials_requested import DbusTagCredentialsRequested
from pythonedainfrastructure.pythonedadbus.dbus_signal_listener import DbusSignalListener

from dbus_next import BusType

from typing import Dict

class UnveilingPartnerDbusSignalListener(DbusSignalListener):

    """
    A Port that listens to UnveilingPartner-relevant d-bus signals.

    Class name: UnveilingPartnerDbusSignalListener

    Responsibilities:
        - Connect to d-bus.
        - Listen to signals relevant to UnveilingPartner.

    Collaborators:
        - PythonEDAApplication: Receives relevant domain events.
    """

    def __init__(self):
        """
        Creates a new UnveilingPartnerDbusSignalListener instance.
        """
        super().__init__()

    def signal_receivers(self, app) -> Dict:
        """
        Retrieves the configured signal receivers.
        :param app: The PythonEDA instance.
        :type app: PythonEDA from pythonedaapplication.pythoneda
        :return: A dictionary with the signal name as key, and the tuple interface, bus-type and function handler as value.
        :rtype: Dict
        """
        return {
            "TagCredentialsRequested": [ DbusTagCredentialsRequested, BusType.SYSTEM, self.listenTagCredentialsRequested ]
        }


    def listenTagCredentialsRequested(self, *args, **kwargs):
        """
        Gets notified when a signal for a TagCredentialsRequested event occurs.
        :param event: The event.
        :type event: TagCredentialsRequested from pythonedaartifactgittagging.tag_credentials_requested
        """
        print(f'Recceived TagCredentialsRequested signal! args: {args}, kwargs: {kwargs}')
