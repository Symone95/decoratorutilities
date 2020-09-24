def extract_signature_function(fn):
    """
    Funzione per l'estrazione della firma della funzione passata come parametro

    :param fn:
    :return:
    """

    if not fn.__annotations__:
        raise TypeError(f'Missing annotation for {fn.__qualname__}')

    return fn.__annotations__


def is_matching_signature(args_tuple, signature, handler) -> bool:
    """
    Funzione per il controllo del match tra gli args/kwargs e la funzione passati

    :param args_tuple:
    :param signature:
    :param handler:
    :return:
    """
    args, kwargs = args_tuple

    if len(args) + len(kwargs) != len(handler.__code__.co_varnames):
        return False

    if len(args):
        for value, (_key, _type) in zip(args, signature.items()):
            if not isinstance(value, _type):
                return False

    if len(kwargs):
        for arg_name in kwargs:
            if arg_name not in signature:
                return False

            if not isinstance(kwargs[arg_name], signature[arg_name]):
                return False

    return True


def signature_already_exists(searching_signature, handlers_map):
    """
    Funzione per il controllo dell'esistenza della firma della funzione passata con quelle salvate nella mappa "handlers_map"

    :param searching_signature:
    :param handlers_map:
    :return:
    """
    for (signature, handler) in handlers_map:
        if searching_signature == signature:
            return True

    return False