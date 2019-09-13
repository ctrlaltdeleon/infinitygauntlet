class CapturePoint():

    def __init__(self, team="Neutral", radius=5, x=0, y=0, z=0, timer=0, cooldown=0, damage=0, damageTimer=0, buff=None, buffTimer=0):
        # `CapturePoint` is "Neutral" until claimed by a team.
        self.team = team
        # `CapturePoint` has a specific range (sphere shape).
        self.radius = radius
        # `CapturePoint`  has a specific location depending on the map's coordinates.
        # w/ this you can also attach the `CapturePoint` to another object's coordinates.
        self.x = x  # self.x = someObject.x
        self.y = y  # self.y = someObject.y
        self.z = z  # self.z = someObject.z
        # `CapturePoint` has a timer associated with it for earning rewards.
        self.timer = timer
        # `CapturePoint` has a cooldown timer associated with it for locking mechanisms for game modes.
        self.cooldown = cooldown
        # `CapturePoint` has a damage amount associated with it for burning mechanisms for game modes.
        self.damage = damage
        self.damageTimer = damageTimer
        # `CapturePoint` has a buff giver associated with it for buff mechanisms for game modes.
        self.buff = buff
        self.buffTimer = buffTimer
        print("Constructor called.")

    def __del__(self):
        print("Destructor called.")

    def claimed(self, team):
        # If at least one team member of only one team is occupying the zone, it is "claimed".
        # Unless that one team memember is in "stealth", it may not be claimed.
        self.team = team
        print("Claimed by", self.team, "!")
        # If the team who "claimed" previously "claimed" before the "contested", the timer does not reset to 0.
        # Else restart the time back to 0.
        # Once the timer reaches a time goal, that respective team scores.
        # The `CapturePoint` "claimed" team returns to neutral.

    def contested(self, *amountOfTeams):
        # If at least one team member of both teams (or more) is occupying the zone, it is "contested".
        # The timer is paused.
        print("Contested by", amountOfTeams, "!")

    def score(self, team):
        # If the timer reaches a certain threshold, the team who is claiming the point scores!
        # Scoring points is attached to the team class itself, this function distributes who gets what amount of score.
        self.team = team
        print(team, "scores !")

    def moving(self, x, y, z):
        # Update the `CapturePoint` if it's moving attached to another object or on it's own course.
        self.x = x
        self.y = y
        self.z = z
        print("Point's current location now is:", x, y, z)

    def data(self):
        return self.team, self.radius, self.x, self.y, self.z, self.timer, self.cooldown, self.damage, self.damageTimer, self.buff, self.buffTimer


# Testing area.
team1 = "UNSC"
team2 = "COVENANT"
team3 = "FLOOD"
team4 = "POWER RANGERS"

# Create `someRandomPoint` in the map we're playing.
someRandomPoint = CapturePoint()

# Find out data about out `CapturePoint` object.
print(someRandomPoint.data())

# The `team1` claimed `someRandomPoint`.
someRandomPoint.claimed(team1)

# The `team1`, `team2`, and `team3` are contesting `someRandomPoint` together.
someRandomPoint.contested(team1, team2, team3)

# The `team1` regains back `someRandomPoint`.
someRandomPoint.claimed(team1)

# The `team1` scores.
someRandomPoint.score(team1)
