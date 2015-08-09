import cherrypy

from backend.exercises.take_a_break import TakeABreak
from backend.exercises.wait_for_tomorrow import WaitForTomorrow
from backend.exercises.math import Math
from backend.exercises.base import (TakeABreakException,
                                    WaitForTomorrowException)


class Exercises:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def next(self):
        try:
            bits = Math().perform()
        except TakeABreakException as e:
            bits = TakeABreak(e.time_passed).perform()
        except WaitForTomorrowException:
            bits = WaitForTomorrow().perform()

        return {
            'bits': bits
        }
