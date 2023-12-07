class Sports:
    def __init__(self, name):
        self._name = name
        
    @property
    def sports_name(self):
        return self._name
        
    @sports_name.setter
    def sports_name(self, value):
        self._name = value
            
    def practice(self):
        return "Doing Sports practice"
            
class Landsports(Sports):
    def __init__(self, name, field):
        super().__init__(name)
        self.field = field
        
    @property
    def landsports_field(self):
        return self.field
    
    # 覆寫父類別的 practice 方法
    def practice(self):
        return "Doing Land Sports practice"
    
class Watersports(Sports):
    def __init__(self, name, activity):
        super().__init__(name)
        self._activity = activity
        
    @property
    def watersports_activity(self):
        return self._activity
    
    # 覆寫父類別的 practice 方法
    def practice(self):
        return "Doing Water Sports practice"
    
if __name__ == "__main__":
    baseball = Landsports("Baseball", "Baseball field")
    print(baseball.sports_name)
    print(baseball.landsports_field)
    print(baseball.practice())
    
    waterskiing = Watersports("Water Skiing", "Strap on your skis and ski on water")
    print(waterskiing.sports_name)
    print(waterskiing.watersports_activity)
    print(waterskiing.practice())
