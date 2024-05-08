import inspect

import pendulum
from rich.console import Console, Style


def terminal_grpc_server(url: str, name_server: str, time_interapt: int):
    restart_time = (
        pendulum.now().add(seconds=time_interapt).format("hh:mm (Do-MMMM-YYYY)")
    )
    console = Console(style=Style(bold=True, color="deep_pink4"), log_time=True)
    console.print(
        f"############## Start grpc: {name_server.upper()} 🚀 ###############",
        justify="center",
    )
    console.print(
        f"####################### Link port: [url][::]:{url}[/url] #######################",
        justify="center",
    )
    console.print(
        f"########## Time restart: {restart_time} ###########",
        justify="center",
    )


def _print(*messages: any):
    caller_frame = inspect.stack()[1]
    caller_filename = caller_frame.filename.split("core/")[1]
    console = Console(style=Style(bold=True, color="deep_pink4"), log_time=True)
    console.print(f"Location: {caller_filename}", justify="center")
    for message in messages:
        console.print(f"Message: {message}")

    console.print("_" * 200 + "\n", justify="full", no_wrap=True)
