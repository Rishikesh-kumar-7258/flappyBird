class StateMachine:

    def __init__(self, states={}):
        """
        The state machine will handle all the state changes in the game
        """

        self.current = {}
        self.states = states

    def change(self, state):
        
        """
        This function will be transitioning states
        """
        assert state in self.states

        self.current.Exit()
        self.current = states[state]
        self.current.enter()

    
    def update(self, params=None):
        
        self.current.update(params)