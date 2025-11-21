# Entry point for the application.
from . import (
    app,
)  # pragma: no cover # For application discovery by the 'flask' command.
from . import views  # pragma: no cover # For import side-effects of setting up routes.

# Time-saver: output a URL to the VS Code terminal so you can easily Ctrl+click to open a browser
# print('http://127.0.0.1:5000/hello/VSCode')
