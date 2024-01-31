"""
Hatch CLI Plugin Hooks
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from hatch.cli.build import build
from hatch.cli.clean import clean
from hatch.cli.config import config
from hatch.cli.dep import dep
from hatch.cli.env import env
from hatch.cli.fmt import fmt
from hatch.cli.new import new
from hatch.cli.plugin.interface import CommandLinePluginInterface
from hatch.cli.project import project
from hatch.cli.publish import publish
from hatch.cli.python import python
from hatch.cli.run import run
from hatch.cli.shell import shell
from hatch.cli.status import status
from hatch.cli.version import version
from hatchling.plugin import hookimpl

if TYPE_CHECKING:
    from click import Command, Group


class HatchBuiltinCli(CommandLinePluginInterface):
    """
    Hatch built-in CLI plugin
    """

    PLUGIN_NAME = "hatch.cli"

    @classmethod
    def cli(cls) -> list[Command | Group]:
        """
        Return a list of click.Command or click.Group objects to be added to the CLI
        """
        return [
            build,
            clean,
            config,
            dep,
            env,
            fmt,
            new,
            project,
            publish,
            python,
            run,
            shell,
            status,
            version,
        ]


@hookimpl
def hatch_register_command_line() -> list[type[CommandLinePluginInterface]]:
    return [
        HatchBuiltinCli,
    ]
