
def args_printer(fn):
    """
    Semplice funzione per il print dei parametri posizionali o nominali
    :param fn:
    :return:
    """

    print(f"fn = {fn} - {fn.__annotations__}")

    def wrapper(*args, **kwargs):

        if len(args) > 0:
            print(f"Args: {args}")

        if len(kwargs) > 0:
            print(f"Kwargs: {kwargs}")

        return fn(*args, **kwargs)

    return wrapper


def checktype(fn):
    """
    Funzione per il controllo del tipo di dato passato come parametro in base alla firma del metodo
    :param fn:
    :return:
    """

    def wrapper(*args, **kwargs):

        # Controllo parametri posizionali (args)
        if len(args) > 0:
            if len(fn.__annotations__) == len(args): #FIXME 1) tipo di ritorno no, 2) non hai considerato i kwargs
                for index, k in enumerate(fn.__annotations__):
                    if fn.__annotations__[k] != type(args[index]):
                        raise TypeError(
                            f"got: \'{args[index]}\' of {type(args[index])} instance, expected {type(k)} instance for \"{k}\" parameter")
            else:
                print(f"Missing parameter: got {len(args)} expected {len(fn.__annotations__)} parameter in {fn.__name__} function")

        # Controllo parametri nominali (kwargs)
        if len(kwargs) > 0:
            #print("Stampo tutti i kwargs", fn.__annotations__, kwargs)
            for k in fn.__annotations__:
                if type(kwargs[k]) != fn.__annotations__[k]:
                    raise TypeError(f"Got: \'{kwargs[k]}\' of {type(kwargs[k])} instance, expected {fn.__annotations__[k]} instance for \"{k}\" parameter")

        return fn(*args, **kwargs)

    return wrapper
