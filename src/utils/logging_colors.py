import logging
import yaml
from rich.console import Console
from rich.logging import RichHandler
from rich.pretty import install as pretty_install
from rich.theme import Theme
from rich.traceback import install as traceback_install

logger = logging.getLogger('my_inventory_manager')

def setup_logging(config_file='src/resources/logging_config.yaml'):
    """
    Set up the logging system using a configuration file.
    """

    # Load configuration from the YAML file
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    class RingBuffer(logging.StreamHandler):
        """
        A logging handler that stores the last n log entries in memory.
        """
        def __init__(self, capacity):
            """
            Initialize the ring buffer with a capacity.

            Args:
                capacity (int): The maximum number of log entries to store.
            """
            super().__init__()
            self.capacity = capacity
            self.buffer = []
            self.formatter = logging.Formatter(
                '{ "asctime":"%(asctime)s", "created":%(created)f, "facility":"%(name)s", "pid":%(process)d, "tid":%(thread)d, "level":"%(levelname)s", "module":"%(module)s", "func":"%(funcName)s", "msg":"%(message)s" }'
            )

        def emit(self, record):
            """
            Store the log record in the ring buffer.

            Args:
                record (logging.LogRecord): The log record to store.
            """
            msg = self.format(record)
            self.buffer.append(msg)
            if len(self.buffer) > self.capacity:
                self.buffer.pop(0)

        def get(self):
            """
            Return the list of log entries stored in the ring buffer.
            """
            return self.buffer

    # Load configuration from the YAML file
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    level = getattr(logging, config['logging']['level'].upper(), logging.DEBUG)
    ring_buffer_capacity = config['logging']['ring_buffer_capacity']

    logger.setLevel(level)
    console = Console(log_time=True, log_time_format='%H:%M:%S-%f', theme=Theme({
        "traceback.border": "black",
        "traceback.border.syntax_error": "black",
        "inspect.value.border": "black",
    }))
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s | %(name)s | %(levelname)s | %(module)s | %(message)s', handlers=[logging.NullHandler()])
    pretty_install(console=console)
    traceback_install(console=console, extra_lines=1, max_frames=10, width=console.width, word_wrap=False, indent_guides=False, suppress=[])

    while logger.hasHandlers() and len(logger.handlers) > 0:
        logger.removeHandler(logger.handlers[0])

    rh = RichHandler(show_time=True, omit_repeated_times=False, show_level=True, show_path=False, markup=False, rich_tracebacks=True, log_time_format='%H:%M:%S-%f', level=level, console=console)
    rh.setLevel(level)
    logger.addHandler(rh)

    rb = RingBuffer(ring_buffer_capacity)
    rb.setLevel(level)
    logger.addHandler(rb)
    logger.buffer = rb.buffer

    logging.getLogger("urllib3").setLevel(logging.ERROR)
    logging.getLogger("httpx").setLevel(logging.ERROR)
    logging.getLogger("diffusers").setLevel(logging.ERROR)
    logging.getLogger("torch").setLevel(logging.ERROR)
    logging.getLogger("lycoris").handlers = logger.handlers

# Call setup_logging to initialize the logging system
setup_logging()