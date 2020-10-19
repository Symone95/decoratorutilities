import pytest
from decoratorutilities import singleton


def test_singleton_class_no_params():

    @singleton()
    class A(object):
        def __init__(self):
            self.x = 10

        def print_hello(self):
            return "Hello World"

    assert A.x == 10
    assert A.print_hello() == "Hello World"

    with pytest.raises(TypeError):
        @singleton
        class B(object):
            def __init__(self):
                self.x = 10

        B()  # Raises TypeError Exception


def test_singleton_class_with_kwargs():

    @singleton(x=10, message="Message to send", email=["simone.scalamandre95@gmail.com"])
    class A(object):
        pass

    assert A.x == 10
    assert A.message == "Message to send"
    assert len(A.email) == 1
    assert A.email == ["simone.scalamandre95@gmail.com"]


def test_singleton_instantiation_fails():

    @singleton()
    class A(object):
        def __init__(self):
            pass

    @singleton(x=10)
    class B(object):
        def __init__(self):
            pass

    with pytest.raises(TypeError) as e:
        A()

    with pytest.raises(TypeError):
        B()


def test_singleton_array_access():

    @singleton()
    class A:
        #def __getitem__(self, item):
        #    return item
        pass

    with pytest.raises(KeyError):
        assert A['ciao'] == 'ciao'

    A['ciao'] = 'ciao'
    assert A['ciao'] == 'ciao'


def test_accessing_property_str():

    @singleton()
    class A:

        def __str__(self):
            return 'A'

    assert str(A) == 'A'


def test_accessing_property_repr():

    @singleton()
    class A:
        def __repr__(self):
            return 'A()'

    assert repr(A) == "<class 'decoratorutilities._singleton.Singleton'>({'args': {}, 'klass_name': ""'A'})" #'A()'


def test_decorating_function_must_fails():

    with pytest.raises(TypeError):
        @singleton()
        def A():
            pass


def test_with_open_file():
    @singleton()
    class A:
        def __init__(self):
            self.file_name = "filename.txt"  # set file name

    # Open and read file
    with A as f:
        f.write("New test")
        file_lines = f.readlines()
    f.close()  # Close file

    for line in file_lines:
        print(line)



def test_index_error_args_not_in_class():

    @singleton(24, 1, 5, name='Simone', email='simone.scalamandre95@gmail.com')
    class A:
        pass

    del A[0]

    with pytest.raises(KeyError):
        A[0]  # Raises KeyError because not find attribute at index 0

    with pytest.raises(KeyError):
        A["0"]  # Raises KeyError because not find attribute with key "0"

    with pytest.raises(IndexError):
        A[5]  # Raises IndexError because not find attribute at index 5

"""
def test_args_and_kwargs():

    @singleton(0, 1, 2, a='a', b='b')
    class A:
        def __init__(self, para_0, param_1, param_2, a,  b):
            self.para_0 = para_0
            self.param_1 = param_1
            self.param_2 = param_2
            self.a = a
            self.b = b

    assert A.para_0 == 0
    assert A.param_1 == 1
    assert A.param_2 == 2
    assert A.a == 'a'
    assert A.b == 'b'
"""


def test_args_and_kwargs_simone():

    @singleton(24, 1, 5, name='Simone', email='simone.scalamandre95@gmail.com')
    class A:
        def __init__(self):
            print("SONO NELL'INIT DELLA ClASSE A")
            print("PRIMO PARAM: ", self)
            print("DIR PRIMO PARAM: ", dir(self))

    assert A[0] == 24
    assert A["1"] == 1
    assert A["2"] == 5
    assert A.name == "Simone"
    assert A.email == "simone.scalamandre95@gmail.com"

