=====================
Check Parameters Type
=====================

Decorate your own function with @checktype decorator to check parameters type

.. code-block:: python
   :linenos:

    from decoratorutilities import checktype

    @checktype
    def my_functon(a: int, b: int):
        return 1

    # Correct invoke
    my_functon(5, 6)

    # Throws TypeError Exception
    my_functon("5", "6")
    my_functon("invalid", b="Invalid")
    my_functon(a="invalid", b="Invalid")
