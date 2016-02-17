
##__________________________________________________________________||
class LambdaStr(object):
    """select events to which a lambda returns True.

    A lambda should be given as a string to __init__ and will be
    evaluated in begin(). This is because a lambda is not picklable.

    In the multiprocessing mode, __init__() is called in the main
    process. Then, the instance will be pickled and sent to
    subprocesses. begin() will be called in the subprocesses.

    """
    def __init__(self, lambda_str, name = None):
        if name is not None: self.name = name
        self.lambda_str = lambda_str

    def begin(self, event):
        self.func = eval('lambda ' + self.lambda_str)

    def __call__(self, event):
        try:
            return self.func(event)
        except:
            print self.lambda_str
            raise

    def end(self):
        self.func = None

##__________________________________________________________________||
