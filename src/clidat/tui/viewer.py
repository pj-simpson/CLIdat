import json

from rich.text import Text
from rich.json import JSON

from textual.app import App as TUIApp, ComposeResult
from textual.widgets import Header, Footer, Tree, Static
from textual.widgets.tree import TreeNode


class JSONViewer(TUIApp):
    def __init__(self, data: str):
        super().__init__()
        self.data = data


    def compose(self) -> ComposeResult:
        yield Static(JSON(self.data))

    def on_button_pressed(self) -> None:
        self.exit()


class TreeViewer(TUIApp):

    # This has been altered very little from the Textual 'JSON tree' Example:
    # https: // github.com / Textualize / textual / blob / main / examples / json_tree.py

    def __init__(self, data: str):
        super().__init__()
        self.data = json.loads(data)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Tree("Root")

    @classmethod
    def add_json(cls, node: TreeNode, json_data: object) -> None:
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

        add_node("JSON", node, json_data)

    def on_mount(self) -> None:
        tree = self.query_one(Tree)
        json_node = tree.root.add("JSON")
        self.add_json(json_node,self.data)
        tree.root.expand()
