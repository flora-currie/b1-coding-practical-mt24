class PDController:
    def __init__(self, KP = 0.15, KD=0.6):
        self.KP = KP
        self.KD = KD 
        self.prev_error = 0 

    def control_action(self, error, dt) -> float:
        derivative = (error - self.prev_error) / dt
        #Compute the control action as given by the tester formula 
        control_act = self.KP*error + self.KD*derivative

        #Store the current error for the next step
        self.prev_error = error 

        return control_act

