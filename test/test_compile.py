import os
import sys

sys.path.append('src')
import compile

def test_file_error():
    res = compile.compileFile('test/test_compile/error.py')
    assert(res[0] is False)
    assert(res[1] is not None)
    assert(isinstance(res[1], str))

def test_file_no_error():
    if os.path.exists('test/test_compile/no_error.pyc'):
        os.remove('test/test_compile/no_error.pyc')

    res = compile.compileFile('test/test_compile/no_error.py')
    assert(res[0] is True)
    assert(res[1] is None)

    assert(os.path.exists('test/test_compile/no_error.pyc'))

def test_dir_error():
    res = compile.compileDir('test/test_compile/error')
    assert(res is False)

def test_dir_no_error():
    res = compile.compileDir('test/test_compile/no_error')
    assert(res is True)
