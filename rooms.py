class DungeonRunner(object):
    '''Run the dungeon.
    
    Go through it room by room and make sure the hero dies where...
    Erm, make sure the hero saves the day without dying!
    '''
    
    def __init__(self, run_room):
        self.run_room = run_room
        
    def run(self):
        '''Run the room
        
        Room should be a class all by itself. This is what the exercise calls
        for at http://learnpythonthehardway.org/book/ex45.html
        '''

        # when we split out DungeonRunner from the rest of the rooms,
        # maybe a import rooms followed by a getattr(rooms, self.run_room)
        # would make more sense than grabbing the class from the globals()
        # dict! oh my!
        current_room = globals()[self.run_room]()
        room_runner = getattr(current_room, 'run')
        turn = room_runner()
        
    def death(self):
        '''You're dead.'''
        pass
        
class Room(object):
    '''The base room
    
    Sets up common things for all rooms'''
    
    #def __init__(self):
    #    self.narrate()
    
    def narrate(self):
        print self.__doc__
        
    def get_action(self, prompt):
        self.action = raw_input(prompt)
        return self.action

class StartAdventure(Room):
    '''Gitzold's Tale
    
    You sit back in your chair in the tavern staring at Gitzold's messy beard 
    as he tells his pitiful story of being a great arcanist researching
    alchemical advances for His Majesty, but having his tower overrun by a
    band of dirty, filthy trolls. What's a "great arcanist" without his tower
    anyway? Through his ramblings, you gather that he left the scrolls with
    all of the discoveries he has made in this tower of his, but that the new
    residents of the tower are far too powerful to even consider taking it
    back by force.
    
    "That's why you're here," the disheveled old mage sternly points out. "You
    must go in there without being discovered and find my scrolls!"
    '''
    
    def __init__(self):
        # sorry, no treasures in the tavern
        self.treasures = []
        
    def run(self):
        next = self.get_action('Do you have any questions for Gitzold?')
        if 'run away' in next:
            print "you run away like a sissy"
            exit(-1)
            
class TowerLevelOne(object):
    '''
    '''
    
    pass
    
class TowerLevelTwo(object):
    '''
    '''
    
    pass
    
class TowerLevelThree(object):
    '''
    '''
    
    pass
    
class TowerLevelFour(object):
    '''
    '''
    
    pass
    
class TowerLevelFour(object):
    '''
    '''
    
    pass
    
class TowerLevelFive(object):
    '''
    '''
    
    pass