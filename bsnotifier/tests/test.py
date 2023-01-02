"""Pytest test cases."""

import tempfile
import time
from multiprocessing import Process
from pathlib import Path

import psutil
from assertpy import assert_that
from click.testing import CliRunner

from bsnotifier.main import main


class ClickRunner(Process):
    """Click command line application runner."""

    def __init__(self, cli, arguments):
        """Constructor method.

        :param cli: Click command line application.
        :param arguments: List of command line application arguments.
        """
        super().__init__()

        self.cli = cli
        self.arguments = arguments

    def run(self):
        """Run the click command line application."""
        runner = CliRunner()
        runner.invoke(self.cli, self.arguments)


class TestCases:
    """Pytest test cases."""

    def setup_class(self):
        """Checks the environment preconditions."""
        battery = psutil.sensors_battery()
        assert_that(battery.power_plugged).described_as('The battery must be disconnected to run the tests').is_false()
        assert_that(battery.percent).described_as(
            'The battery percent must be less than 100 to run the tests.'
        ).is_less_than(100)

    def test_common_mode(self):
        """Verify that the application works correctly."""
        interval = 5
        battery_level = 100
        try:
            with tempfile.NamedTemporaryFile(suffix='.log') as tmpfile:
                path = Path(tmpfile.name)

                assert_that(path.read_text()).does_not_contain('starting bsnotifier')

                process = ClickRunner(
                    main, ['--interval', interval, '--level', battery_level, '--output', tmpfile.name]
                )
                process.start()

                time.sleep(interval + 1)

                assert_that(path.read_text()).contains('starting bsnotifier')
                assert_that(path.read_text()).contains('battery is getting low')
                assert_that(path.read_text()).contains('playing audio')
        finally:
            if process.is_alive():
                process.terminate()
