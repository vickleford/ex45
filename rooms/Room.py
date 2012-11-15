class Room(object):
    '''The base room
    
    Sets up common things for all rooms'''
    
    def __init__(self):
        self.narrate()
    
    def narrate(self):
        print self.__doc__
        
    def get_action(self, prompt):
        self.action = raw_input(prompt)
        return self.action