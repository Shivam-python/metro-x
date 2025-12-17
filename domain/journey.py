from config.constants import FORWARD, RETURN

class Journey:
    @staticmethod
    def detect(last_route, current_route, journey_type=None):
        if last_route and last_route[::-1] == current_route and journey_type == FORWARD:
            return RETURN
        return FORWARD
