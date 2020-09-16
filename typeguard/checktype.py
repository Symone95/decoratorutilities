def checktype(fn):
    """
    Funzione per il controllo del tipo di dato passato come parametro e del return in base alla firma del metodo
    :param fn:
    :return:
    """
    #print("Annotations: ", fn.__annotations__)

    def wrapper(*args, **kwargs):

        # Controllo parametri posizionali (args)
        if len(args) > 0:
            for value, (_key, _type) in zip(args, fn.__annotations__.items()):
                if not isinstance(value, _type):
                    raise TypeError(f"pot: \'{value}\' of {type(value)} instance, expected {_type} instance for \"{_key}\" parameter")

        # Controllo parametri nominali (kwargs)
        if len(kwargs) > 0:
            #print("Stampo tutti i kwargs", fn.__annotations__, kwargs)
            for kwarg in kwargs:
                if not isinstance(kwargs[kwarg], fn.__annotations__[kwarg]):
                    raise TypeError(f"Got: \'{kwargs[kwarg]}\' of {type(kwargs[kwarg])} instance, expected {fn.__annotations__[kwarg]} instance for \"{kwarg}\" parameter")


        # Controllo il tipo di dato del return
        fn_return = fn(*args, **kwargs)
        if "return" in fn.__annotations__ and not isinstance(fn_return, fn.__annotations__["return"]):
            raise TypeError(
                f"Got: \'{type(fn_return)}\' return type, expected {fn.__annotations__['return']} return type for \"{fn.__name__}\" function")

        return fn_return

    return wrapper