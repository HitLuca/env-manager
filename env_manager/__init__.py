"""
environment manager class
"""
import os
from enum import Enum
from typing import Type

from env_flag import env_flag

from ._version import get_versions  # type:ignore

__version__ = get_versions()["version"]
del get_versions


class EnvManager:
    """
    environment variables manager, ensures that all the required variables exist and allows the retrieval of them
    """

    _all_vars_checked = False
    _env_mappings_not_checked_error_message = "cannot get environment variable without checking that all env variables are set first. Please run EnvManager.check_env_mappings_exist() during project startup to check all mappings."

    @staticmethod
    def check_env_mappings_exist(env_mappings: Type[Enum]) -> None:
        """
        checks if all the environment variables are defined in the local environment
        """
        for env_mapping in env_mappings:
            EnvManager._check_env_mapping_exists(env_mapping)
        EnvManager._all_vars_checked = True

    @staticmethod
    def _check_env_mapping_exists(env_mapping: Enum) -> None:
        """
        checks if the input environment mapping exists

        Args:
            env_mapping (Enum): environment mapping to test
        """
        assert isinstance(env_mapping, Enum)
        assert (
            env_mapping.name in os.environ
        ), f"variable {env_mapping.name} doesn't exist in environment"

    @staticmethod
    def get_string(env_mapping: Enum, can_be_empty: bool = False) -> str:
        """
        returns the string associated with the input environment mapping

        Args:
            env_mapping (Enum): environment mapping to fetch
            can_be_empty (bool, optional): whether the retrieved value can be the empty string. Defaults to False.

        Returns:
            str: string associated with the environment mapping
        """
        if not EnvManager._all_vars_checked:
            raise ValueError(EnvManager._env_mappings_not_checked_error_message)
        assert isinstance(env_mapping, Enum)

        EnvManager._check_env_mapping_exists(env_mapping)

        value = os.environ[env_mapping.name]

        if not can_be_empty:
            assert (
                len(value) > 0
            ), f"expected env var {env_mapping} to have content, got empty string"

        return value

    @staticmethod
    def get_bool(env_mapping: Enum) -> bool:
        """
        returns the boolean associated with the input environment mapping

        Args:
            env_mapping (Enum): environment mapping to fetch

        Returns:
            bool: bool associated with the environment mapping
        """
        if not EnvManager._all_vars_checked:
            raise ValueError(EnvManager._env_mappings_not_checked_error_message)
        assert isinstance(env_mapping, Enum)

        EnvManager._check_env_mapping_exists(env_mapping)

        return env_flag(env_mapping.name)
