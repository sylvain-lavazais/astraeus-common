import structlog


def logit(method):
    """
    Decorator to log method calls and their results using structlog.

    :param method: The method/function to be decorated.
    :return: The decorated method/function.
    """
    def logged(*args, **kw):
        """
        :param method: The method to be logged.
        :param args: The arguments passed to the method.
        :param kw: The keyword arguments passed to the method.
        :return: The result returned by the method.

        """
        func_name = method.__name__
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kw.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        structlog.get_logger().debug(f'{func_name} start')
        structlog.get_logger().debug(f'with args {signature}')
        result = method(*args, **kw)
        structlog.get_logger().debug(f'{func_name} end')
        structlog.get_logger().debug(f'with result {result}')
        return result

    return logged
