class MacPackage(object):

    class FileCollection(object):
        pass
    
    class Scripts(FileCollection):
        pass

    class Payload(FileCollection):
        pass

    def __init__(self):
        self._scripts = Scripts()
        self._payload = Payload()

    def build():
        pass
