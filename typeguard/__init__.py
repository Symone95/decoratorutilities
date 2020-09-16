
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
    Funzione per il controllo del tipo di dato passato come parametro e del return in base alla firma del metodo
    :param fn:
    :return:
    """
    #print("Annotations: ", fn.__annotations__)

    def wrapper(*args, **kwargs):

        # Controllo parametri posizionali (args)
        if len(args) > 0:
            for value, (_key, _type) in zip(args, fn.__annotations__.items()):
                print('=> ', value, _key, _type)
                if not isinstance(value, _type):
                    raise TypeError(f"Got: \'{value}\' of {_key}={type(value)} instance, expected {_type} instance for \"{_type}\" parameter")

        # Controllo parametri nominali (kwargs)
        if len(kwargs) > 0:
            #print("Stampo tutti i kwargs", fn.__annotations__, kwargs)
            for k in kwargs:
                if type(kwargs[k]) != fn.__annotations__[k]:
                    raise TypeError(f"Got: \'{kwargs[k]}\' of {type(kwargs[k])} instance, expected {fn.__annotations__[k]} instance for \"{k}\" parameter")

        # Controllo il tipo di dato del return
        fn_return = type(fn(*args, **kwargs))
        if "return" in fn.__annotations__ and fn_return != fn.__annotations__["return"]:
            raise TypeError(
                f"Got: \'{fn_return}\' return type, expected {fn.__annotations__['return']} return type for \"{fn.__name__}\" function")

        return fn(*args, **kwargs)

    return wrapper

#@args_printer
@checktype
def test(a:int, b:str) -> int:
    #print("Prova")
    return "1"


if __name__ == "__main__":
    test(1, b="1")
