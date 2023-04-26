import json

from rich.json import JSON
from rich.text import Text
from textual.app import App as TUIApp
from textual.app import ComposeResult
from textual.widgets import Footer, Header, Static, TextLog, Tree
from textual.widgets.tree import TreeNode


class ViewerDispatcher:
    def __init__(self, data: str, data_type: str, json_flag: bool = False):
        self.data = data
        self.json = json_flag
        self.data_type = data_type

    def __call__(self, *args, **kwargs):
        if self.json:
            return JSONViewer(self.data).run()
        else:
            return TreeViewer(self.data, self.data_type).run()


class JSONViewer(TUIApp):
    def __init__(self, data: str):
        super().__init__()
        self.data = data

    def compose(self) -> ComposeResult:
        yield Header()
        yield TextLog(highlight=True, markup=True)

    def on_ready(self) -> None:
        text_log = self.query_one(TextLog)
        text_log.write(JSON(self.data))


class TreeViewer(TUIApp):
    # This has been altered very little from the Textual 'JSON tree' Example:
    # https: // github.com / Textualize / textual / blob / main / examples / json_tree.py

    def __init__(self, data: str, data_type: str):
        super().__init__()
        self.data = json.loads(data)
        self.data_type = data_type

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Tree("Codat API Response")

    @classmethod
    def add_json(cls, node: TreeNode, json_data: object, data_type: str) -> None:
        """Adds JSON data to a node.
        Args:
            node (TreeNode): A Tree node.
            json_data (object): An object decoded from JSON.
        """

        from rich.highlighter import ReprHighlighter

        highlighter = ReprHighlighter()

        def add_node(name: str, node: TreeNode, data: object) -> None:
            """Adds a node to the tree.
            Args:
                name (str): Name of the node.
                node (TreeNode): Parent node.
                data (object): Data associated with the node.
            """
            if isinstance(data, dict):
                node.set_label(Text(f"{{}} {name}"))
                for key, value in data.items():
                    new_node = node.add("")
                    add_node(key, new_node, value)
            elif isinstance(data, list):
                node.set_label(Text(f"[] {name}"))
                for index, value in enumerate(data):
                    new_node = node.add("")
                    add_node(str(index), new_node, value)
            else:
                node.allow_expand = False
                if name:
                    label = Text.assemble(
                        Text.from_markup(f"[b]{name}[/b]="), highlighter(repr(data))
                    )
                else:
                    label = Text(repr(data))
                node.set_label(label)

        add_node(data_type, node, json_data)

    def on_mount(self) -> None:
        tree = self.query_one(Tree)
        json_node = tree.root.add("JSON")
        self.add_json(json_node, self.data, self.data_type)
        tree.root.expand()
