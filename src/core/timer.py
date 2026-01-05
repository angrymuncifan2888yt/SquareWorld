class Timer:
    def __init__(self, time: float):
        self.duration = time
        self.__time_left = time
        self.__paused = False
        self.__finished = False

    @property
    def finished(self) -> bool:
        return self.__finished

    @property
    def time_left(self) -> float:
        return self.__time_left

    def update(self, delta: float = 1.0):
        if self.__paused or self.__finished:
            return

        self.__time_left -= delta

        if self.__time_left <= 0:
            self.__time_left = 0
            self.__finished = True

    def pause(self):
        self.__paused = True

    def resume(self):
        if not self.__finished:
            self.__paused = False

    def reset(self):
        self.__time_left = self.duration
        self.__paused = False
        self.__finished = False