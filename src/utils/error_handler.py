# src/utils/error_handler.py

from typing import Any, Callable, TypeVar, Dict, Tuple, Optional, Type
from functools import wraps
import traceback
from utils.custom_logging import logger

T = TypeVar('T')

class ErrorHandler:
    @staticmethod
    def handle_errors(
        default_value: Any = None,
        reraise: bool = False,
        ignore_exceptions: Tuple[Type[Exception], ...] = (),
        log_exceptions: Optional[Tuple[Type[Exception], ...]] = None,
        log_level: str = "ERROR"
    ) -> Callable[[Callable[..., T]], Callable[..., Dict[str, Any]]]:
        
        def log_and_handle_exception(func_name: str, e: Exception, log_exceptions: Optional[Tuple[Type[Exception], ...]], log_level: str):
            stack_trace = traceback.format_exc()
            if log_exceptions is None or isinstance(e, log_exceptions):
                ErrorHandler.log_error(func_name, str(e), stack_trace, log_level)
            return stack_trace

        def wrapper(func: Callable[..., T]) -> Callable[..., Dict[str, Any]]:
            @wraps(func)
            def wrapped(*args: Any, **kwargs: Any) -> Dict[str, Any]:
                try:
                    result = func(*args, **kwargs)
                    return {"success": True, "data": result, "is_default": False, "error": None}
                except ignore_exceptions:
                    return {"success": False, "data": default_value, "is_default": True, "error": "Ignored exception", "exception_type": "Ignored", "stack_trace": None}
                except Exception as e:
                    stack_trace = log_and_handle_exception(func.__name__, e, log_exceptions, log_level)
                    if reraise:
                        raise
                    return {"success": False, "data": default_value, "is_default": True, "error": str(e), "exception_type": type(e).__name__, "stack_trace": stack_trace}

            return wrapped

        return wrapper

    @staticmethod
    def log_error(
        function_name: str,
        error_message: str,
        stack_trace: str = "",
        log_level: str = "ERROR"
    ) -> None:
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if log_level.upper() not in valid_levels:
            raise ValueError(f"Invalid log level. Must be one of: {', '.join(valid_levels)}")

        level = getattr(logger, log_level.upper(), logger.ERROR)
        error_details = f"Function: {function_name}, Message: {error_message}"
        if stack_trace:
            error_details += f"\nStack Trace:\n{stack_trace}"
        
        logger.log(level, error_details)