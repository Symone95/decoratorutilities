from functools import wraps

implemented_functions = {}

#FIXME: scoped overload
#FIXME: parameter named ored


def overload(fn):
    """
    Funzione per poter eseguire l'overload di una funzione
    :param fn:
    :return:
    """
    # Funzione chiamata per ogni funzione che la implementa
    if fn.__name__ not in implemented_functions:
        implemented_functions[fn.__name__] = []

    # Aggiungo la funzione alla chiave con lo stesso valore del nome di tale funzione, ad esempio se ci sono più funzioni nominate "a" le aggiunge nel vettore definito nella chiave "a"
    implemented_functions[fn.__name__].append(fn)

    @wraps(fn)
    def wrapper(*args, **kwargs):

        available_function_list = []

        # Filtro tra le funzioni implementate con il nome della funzione corrente
        if fn.__name__ in implemented_functions:
            available_function_list = implemented_functions[fn.__name__]

        # Istanzio una lista in cui metterò in ordine tutti i tipi degli args e dei kwargs passati
        fn_params = []

        # Controllo per gli args
        if len(args) > 0:
            for arg in args:
                fn_params.append(type(arg))

        # Controllo per gli kwargs
        if len(kwargs) > 0:
            for key, val in kwargs.items():
                fn_params.append(type(val))

        #print("current fn_params: ", fn_params)

        # Ora filtro nelle "available_function_list" e controllo i parametri delle funzioni disponibili filtrate prima in base al nome
        for av_fn in available_function_list:

            # Rimuovo eventuale chiave "return"
            if "return" in av_fn.__annotations__:
                av_fn.__annotations__.pop("return", None)

            current_fn_params = []

            # Cerco tra tutti i parametri di ogni funzione e ne estraggo il type del parametro
            for key, val in av_fn.__annotations__.items():
                current_fn_params.append(val)

            # Infine paragono i parametri cercati con quelli passati, se corrispondono allora ne ritorno la relativa funzione
            if fn_params == current_fn_params:
                #print("Trovata corrispondenza: ", av_fn.__annotations__)
                return av_fn(*args, **kwargs)

    return wrapper
