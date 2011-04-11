init python:
    class TraitTracker(object):
        def __init__(self):
            self.traits = {}
            
        def ModifyTrait(self, trait, amt):
            if trait in self.traits:
                self.traits[trait] += amt
            else:
                self.traits[trait] = amt
            
            if self.traits[trait] <= 0:
                del self.traits[trait]
                
        def CheckTrait(self, trait, amt):
            if trait in self.traits:
                if self.traits[trait] >= amt:
                    return True
            return False
