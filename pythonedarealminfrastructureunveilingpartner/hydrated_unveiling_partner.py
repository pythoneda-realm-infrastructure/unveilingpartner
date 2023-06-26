"""
pythonedarealminfrastructureunveilingpartner/hydrated_unveiling_partner.py

This file declares the HydratedUnveilingPartner class.

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
from pythonedarealmunveilingpartner.unveiling_partner import UnveilingPartner

class HydratedUnveilingPartner(UnveilingPartner):
    """
    Injects an hydrated version of UnveilingPartner as singleton.

    Class name: HydratedUnveilingPartner

    Responsibilities:
        - Injects the master password into the UnveilingPartner singleton instance.

    Collaborators:
        - None
    """

    _master_password = None

    @classmethod
    def set_master_password(cls, passwd: str):
        """
        Specifies the master password.
        :param passwd: The password.
        :type passwd: str
        """
        cls._master_password = passwd

    @classmethod
    def initialize(cls) -> UnveilingPartner:
        """
        Initializes the singleton instance.
        :return: The singleton instance.
        :rtype: UnveilingPartner
        """
        return HydratedUnveilingPartner(cls._master_password)
