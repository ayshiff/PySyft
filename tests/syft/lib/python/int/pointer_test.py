import syft as sy

alice = sy.VirtualMachine(name="alice")
alice_client = alice.get_root_client()
remote_python = alice_client.syft.lib.python

remote_int = remote_python.Int(42)
local_int = 42
funcs = [
    "__abs__",
    "__add__",
    "__and__",
    "__bool__",
    "__ceil__",
    "__divmod__",
    "__eq__",
    "__float__",
    "__floor__",
    "__floordiv__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__gt__",
    "__hash__",
    "__invert__",
    "__le__",
    "__lshift__",
    "__lt__",
    "__mod__",
    "__mul__",
    "__ne__",
    "__neg__",
    "__new__",
    "__or__",
    "__pos__",
    "__pow__",
    "__radd__",
    "__rand__",
    "__rdivmod__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__rfloordiv__",
    "__rlshift__",
    "__rmod__",
    "__rmul__",
    "__ror__",
    "__round__",
    "__rpow__",
    "__rrshift__",
    "__rshift__",
    "__rsub__",
    "__rtruediv__",
    "__rxor__",
    "__setattr__",
    "__sizeof__",
    "__str__",
    "__sub__",
    "__truediv__",
    "__xor__",
    "as_integer_ratio",
    "bit_length",
    "conjugate",
    "denominator",
    "imag",
    "numerator",
    "real",
]


def test_sanity():
    for func in funcs:
        assert hasattr(remote_int, func)
        assert hasattr(local_int, func)
