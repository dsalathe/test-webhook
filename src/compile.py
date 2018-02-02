import glob
import os
import py_compile

def compileFile(filename):
    """
    Takes a filename 'app.py' and tries to compile it to 'app.pyc'. If the compilation
    fails, the tuple (False, ErrorMsg) is returned, else (True, None) is returned.
    :param filename: Name of file to compile.
    :return: (False, ErrorMsg) if compilation fails, else (True, None).
    """
    try:
        py_compile.compile(
                filename,
                cfile=os.path.splitext(filename)[0] + '.pyc',
                doraise=True)
    except py_compile.PyCompileError as e:
        return (False, str(e))
    return (True, None)

def compileDir(dirname):
    """
    Compiles every Python source file in 'dirname' and its subdirectories (recursively).
    :param dirname: The root directory of the repo under testing.
    :return: True if compilation of all files succeeded, false otherwise.
    """
    for filename in glob.iglob(dirname + '/**/*.py', recursive=True):
        if compileFile(filename)[0] is False:
            return False
    return True
