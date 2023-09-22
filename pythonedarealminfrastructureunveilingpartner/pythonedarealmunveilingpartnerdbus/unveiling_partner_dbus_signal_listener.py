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
from dbus_next import BusType, Message
from pythoneda.event import Event
from pythonedaartifacteventchanges.change_staging_from_folder_requested import ChangeStagingFromFolderRequested
from pythonedaartifacteventgittagging.tag_credentials_requested import TagCredentialsRequested
from pythonedaartifacteventinfrastructurechanges.pythonedaartifacteventchangesdbus.dbus_change_staging_from_folder_requested import DbusChangeStagingFromFolderRequested
from pythonedaartifacteventinfrastructuregittagging.pythonedaartifacteventgittaggingdbus.dbus_tag_credentials_requested import DbusTagCredentialsRequested
from pythonedainfrastructure.pythonedadbus.dbus_signal_listener import DbusSignalListener
from typing import Dict

class UnveilingPartnerDbusSignalListener(DbusSignalListener):

    """
    A Port that listens to UnveilingPartner-relevant d-bus signals.

    Class name: UnveilingPartnerDbusSignalListener

    Responsibilities:
        - Connect to d-bus.
        - Listen to signals relevant to UnveilingPartner.

    Collaborators:
        - pythonedaapplication.pythoneda.PythonEDA: Receives relevant domain events.
        - pythonedaartifacteventinfrastructurechanges.pythonedaartifacteventchangesdbus.dbus_change_staging_from_folder_requested.DbusChangeStagingFromFolderRequested
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
        :return: A dictionary with the signal name as key, and the tuple interface and bus type as the value.
        :rtype: Dict
        """
        result = {}
        key = self.fqdn_key(TagCredentialsRequested)
        result[key] = [
            DbusTagCredentialsRequested, BusType.SYSTEM
        ]
        key = self.fqdn_key(ChangeStagingFromFolderRequested)
        result[key] = [
            DbusChangeStagingFromFolderRequested, BusType.SYSTEM
        ]
        return result

    def parse_pythonedaartifactgittagging_TagCredentialsRequested(self, message: Message) -> TagCredentialsRequested:
        """
        Parses given d-bus message containing a TagCredentialsRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The TagCredentialsRequested event.
        :rtype: pythonedaartifacteventgittagging.tag_credentials_requested.TagCredentialsRequested
        """
        return DbusTagCredentialsRequested.parse_pythonedaartifactgittagging_TagCredentialsRequested(message)

    async def listen_pythonedaartifactgittagging_TagCredentialsRequested(self, event: TagCredentialsRequested):
        """
        Gets notified when a signal for a TagCredentialsRequested event occurs.
        :param event: The event.
        :type event: pythonedaartifacteventgittagging.tag_credentials_requested.TagCredentialsRequested
        """
        await self.app.accept(event)

    def parse_pythonedaartifactchanges_ChangeStagingFromFolderRequested(self, message: Message) -> ChangeStagingFromFolderRequested:
        """
        Parses given d-bus message containing a ChangeStagingFromFolderRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The ChangeStagingFromFolderRequested event.
        :rtype: pythonedaartifacteventchanges.change_staging_from_folder_requested.ChangeStagingFromFolderRequested
        """
        return DbusTagCredentialsRequested.parse_pythonedaartifactchanges_ChangeStagingFromFolderRequested(message)

    async def listen_pythonedaartifactchanges_ChangeStagingFromFolderRequested(self, event: ChangeStagingFromFolderRequested):
        """
        Gets notified when a signal for a ChangeStagingFromFolderRequested event occurs.
        :param event: The event.
        :type event: pythonedaartifacteventchanges.change_staging_from_folder_requested.ChangeStagingFromFolderRequested
        """
        await self.app.accept(event)
