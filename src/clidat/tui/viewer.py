from rich.json import JSON
from textual.app import App as TUIApp
from textual.app import ComposeResult
from textual.widgets import Static


class Viewer(TUIApp):
    def __init__(self, data: str):
        super().__init__()
        self.data = data

    def compose(self) -> ComposeResult:
        yield Static(JSON(self.data))

    def on_button_pressed(self) -> None:
        self.exit()
