"""
CLI Plugin Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from click import Command, Group


class CommandLinePluginInterface(ABC):
    """
    Interface for CLI plugins
    """

    @classmethod
    @abstractmethod
    def cli(cls) -> list[Command | Group]:
        """
        Return a list of click.Command or click.Group objects to be added to the CLI
        """
