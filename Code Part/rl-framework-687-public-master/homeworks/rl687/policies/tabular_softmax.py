import numpy as np
from .skeleton import Policy
from typing import Union

class TabularSoftmax(Policy):
    """
    A Tabular Softmax Policy (bs)


    Parameters
    ----------
    numStates (int): the number of states the tabular softmax policy has
    numActions (int): the number of actions the tabular softmax policy has
    """

    def __init__(self, numStates:int, numActions: int):
        
        #The internal policy parameters must be stored as a matrix of size
        #(numStates x numActions)
        self._theta = np.zeros((numStates, numActions))
        
        #TODO
        self._numStates = numStates
        self._numActions = numActions

    @property
    def parameters(self)->np.ndarray:
        """
        Return the policy parameters as a numpy vector (1D array).
        This should be a vector of length |S|x|A|
        """
        return self._theta.flatten()
    
    @parameters.setter
    def parameters(self, p:np.ndarray):
        """
        Update the policy parameters. Input is a 1D numpy array of size |S|x|A|.
        """
        self._theta = p.reshape(self._theta.shape)

    def __call__(self, state:int, action=None)->Union[float, np.ndarray]:
        
        #TODO
        if action is not None:
            return self.getActionProbabilities(state)[action]
        else:
            return self.getActionProbabilities(state)

    def samplAction(self, state:int)->int:
        """
        Samples an action to take given the state provided. 
        
        output:
            action -- the sampled action
        """
        
        #TODO
        
        return np.random.choice(np.arange(self._numActions), p = self.getActionProbabilities(state))

    def getActionProbabilities(self, state:int)->np.ndarray:
        """
        Compute the softmax action probabilities for the state provided. 
        
        output:
            distribution -- a 1D numpy array representing a probability 
                            distribution over the actions. The first element
                            should be the probability of taking action 0 in 
                            the state provided.
        """

        #TODO
        
        state_row = self._theta[state, :]
        
        exp_state_row = np.exp(state_row)
        
        probabilities = exp_state_row / np.sum(exp_state_row)
        
        return probabilities
