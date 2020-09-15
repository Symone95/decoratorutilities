import pytest
from typeguard import checktype
print("HELLO")

def test_base_param():

    @checktype
    def a(b: int):
        pass

    with pytest.raises(TypeError):
        a("ciao")
