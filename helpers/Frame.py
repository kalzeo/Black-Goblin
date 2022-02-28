class Frame:
    def __init__(self, **kwargs):
        self.next = None
        for k, v in kwargs.items():
            self.__setattr__(k, v)