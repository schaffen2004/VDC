from rich.console import Console

console = Console()

class Logger:
    def __init__(self):
        self.config = {
            "Error": "red",
            "Warning": "yellow",
            "Info": "green",
            "Debug": "blue"
        }
    def log(self, message: str, mode:str) -> None:
        """
        Pretty print the notification as plain text with custom color and borders using rich.
        Args:
            notification: The notification to print
            color: Color for text and border
            title: Title for the border
        """
        color = self.config.get(mode, "white")
        console.rule(f"[bold {color}]{mode}[/bold {color}]")
        if isinstance(message, list):
            for item in message:
                console.print(str(item), style=color)
        else:
            console.print(str(message), style=color)
        console.rule(f"[bold {color}]{mode}[/bold {color}]")
        console.print("\n")