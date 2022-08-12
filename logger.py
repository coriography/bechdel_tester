import logging
from rich.logging import RichHandler
from rich.console import Console

# Logging should be for system only
FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

LOGGER = logging.getLogger("rich")

# Configure rich console – for human users
console = Console()
