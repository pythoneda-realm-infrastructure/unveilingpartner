"""
pythonedarealminfrastructureunveilingpartner/pythonedarealmunveilingpartnercli/master_password_cli.py

This file defines the MasterPasswordCli class.

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
from pythoneda.primary_port import PrimaryPort

import argparse


class MasterPasswordCli(PrimaryPort):

    """
    A PrimaryPort that provides UnveilingPartner's master password.

    Class name: MasterPasswordCli

    Responsibilities:
        - Parse the command-line to retrieve the master password.

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
        parser = argparse.ArgumentParser(description="Master password")
        parser.add_argument("-M", "--master-password", required=True, help="The master password")
        args, unknown_args = parser.parse_known_args()

        await app.accept_master_password(args.master_password)
