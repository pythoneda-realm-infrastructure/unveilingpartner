"""
pythonedarealminfrastructureunveilingpartner/pythonedarealmunveilingpartnercli/request_change_staging_cli.py

This file defines the RequestChangeStagingCli class.

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
import argparse
from pythoneda.primary_port import PrimaryPort
from pythonedaartifacteventchanges.change_staging_from_folder_requested import ChangeStagingFromFolderRequested

class RequestChangeStagingCli(PrimaryPort):

    """
    A PrimaryPort that makes UnveilingPartner emit a ChangeStagingRequest.

    Class name: RequestChangeStagingCli

    Responsibilities:
        - Parse the command-line to retrieve the change to request staging.

    Collaborators:
        - PythonEDA subclasses: They are notified back with the information retrieved from the command line.
    """

    def priority(self) -> int:
        return 100

    async def accept(self, app):
        """
        Processes the command specified from the command line.
        :param app: The PythonEDA instance.
        :type app: PythonEDA
        """
        parser = argparse.ArgumentParser(description="Request change staging")
        parser.add_argument(
            "-r", "--repository-folder", required=False, help="The repository folder"
        )
        args, unknown_args = parser.parse_known_args()

        if args.repository_folder:
            await app.accept(ChangeStagingFromFolderRequested(args.repository_folder))
