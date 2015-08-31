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
            if cherrypy.request.method == 'GET':
                exercise = Math().perform()
            else:
                exercise = Math().save()
        except TakeABreakException as e:
            exercise = TakeABreak(e.time_passed).perform()
        except WaitForTomorrowException:
            exercise = WaitForTomorrow().perform()

        return exercise
