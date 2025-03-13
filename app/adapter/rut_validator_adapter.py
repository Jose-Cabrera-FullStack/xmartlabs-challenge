"""
This module contains the RUT (Rol Único Tributario) validator adapter logic.

The RUT is a unique tax identifier used in Chile. This module provides
functions to validate the format and check the validity of a given RUT.
"""

from app.domain.rut_validator import RUTValidator

class RUTValidatorAdapter:
    """
    A class to adapt the RUT (Rol Único Tributario) validation logic.
    """

    @staticmethod
    def validate_rut(rut: str) -> bool:
        """
        Adapt the validation of the given RUT (Rol Único Tributario).

        Args:
            rut (str): The RUT to validate.

        Returns:
            bool: True if the RUT is valid, False otherwise.
        """
        # Use the domain layer's RUTValidator to perform the validation
        return RUTValidator.validate_rut(rut)
