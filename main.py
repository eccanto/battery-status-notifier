"""Package to show a popup window when the battery is low."""

import io
import time
import threading

import click
import psutil
import PySimpleGUI
from PIL import Image
from playsound import playsound


DEFAULT_INTERVAL = 2.5 * 60
DEFAULT_BATTERY_LOW_LEVEL = 10


def image_file_to_bytes(image_path, size) -> bytes:
    """Converts a image path to bytes.

    :param image_path: The image path.
    :param size: The size to which the image will be resized.

    :returns: The image in bytes.
    """
    image = Image.open(image_path)
    image.thumbnail(size, Image.Resampling.LANCZOS)
    bytes_io = io.BytesIO()
    image.save(bytes_io, format='PNG')
    return bytes_io.getvalue()


def show_popup() -> None:
    """Shows a popup window."""
    PySimpleGUI.theme('Black')
    PySimpleGUI.set_options(auto_size_buttons=True, border_width=0, button_color=PySimpleGUI.COLOR_SYSTEM_DEFAULT)

    status_layout = [
        [
            PySimpleGUI.Text('Battery is getting low!', size=(45, 1)),
            PySimpleGUI.Image(data=image_file_to_bytes('./media/images/low-battery.ico', (120, 60))),
        ],
        [
            PySimpleGUI.Button('Ok', button_color='white on green', key='-close-', pad=(20, 20)),
        ]
    ]

    layout = [
        [
            PySimpleGUI.Frame(
                'Battery Status',
                status_layout,
                element_justification='center',
                font=('any 18'),
                background_color='black',
                title_color='#2180DE',
            )
        ]
    ]

    window = PySimpleGUI.Window(
        'Warning',
        layout,
        no_titlebar=False,
        grab_anywhere=True,
        keep_on_top=True,
        use_default_focus=False,
        font='any 15',
        background_color='black',
        finalize=True,
    )

    while True:
        button, _ = window.read()
        if button == '-close-' or button is None:
            break

    window.close()


def playsound_wait(wait: float) -> None:
    """Plays an audio after waiting `wait` seconds.

    :param wait: Seconds to wait.
    """
    time.sleep(wait)
    playsound('./media/audio/alarm.wav')


@click.command()
@click.option(
    '-i',
    '--interval',
    help=(
        'The time interval in seconds that the script waits before checking the battery again '
        f'(default: {DEFAULT_INTERVAL} seconds).'
    ),
    type=int,
    default=DEFAULT_INTERVAL,
)
@click.option(
    '-l',
    '--level',
    help=f'The battery percentage at which the popup window is displayed (default: {DEFAULT_BATTERY_LOW_LEVEL}).',
    type=int,
    default=DEFAULT_BATTERY_LOW_LEVEL,
)
@click.option('-s', '--silent', help='Do not play the sound when popup window is displayed.', is_flag=True)
def main(interval: int, level: int, silent: bool) -> None:
    """Command line application that shows a popup window when the battery is low."""
    while True:
        battery = psutil.sensors_battery()
        if not battery.power_plugged and battery.percent <= level:
            if not silent:
                thread = threading.Thread(target=playsound_wait, args=(0.5,))
                thread.start()

            show_popup()

        time.sleep(interval)


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
