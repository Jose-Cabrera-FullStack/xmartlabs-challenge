"""
This module contains the RUT (Rol Único Tributario) validator service logic.

The RUT is a unique tax identifier used in Chile. This module provides
a service to validate the format and check the validity of a given RUT.
"""

from app.adapter.rut_validator_adapter import RUTValidatorAdapter

class RUTValidatorService:
    """
    A service class to validate the RUT (Rol Único Tributario).
    """

    @staticmethod
    def validate_rut(rut: str) -> bool:
        """
        Validate the given RUT (Rol Único Tributario) using the adapter.

        Args:
            rut (str): The RUT to validate.

        Returns:
            bool: True if the RUT is valid, False otherwise.
        """
        return RUTValidatorAdapter.validate_rut(rut)
