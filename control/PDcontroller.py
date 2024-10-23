class PDController:
    def __init__(self, KP = 0.15, KD=0.6):
        self.KP = KP
        self.KD = KD 
        self.prev_error = 0 

    def control_action(self, reference: float, output: float):
        #Compute the control action using PD control

        #Calculate the error at time t:
        error = reference - output

        #Compute the control action as given by the tester formula 
        control_act = self.KP*error + self.KD*(error - self.prev_error)

        #Store the current error for the next step
        self.prev_error = error 

        return control_act

