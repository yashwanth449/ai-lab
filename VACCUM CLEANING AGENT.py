class VacuumCleanerAgent:
    def __init__(self, rooms):
        # rooms is a dictionary such as:
        # {"A": "Dirty", "B": "Clean"}
        self.rooms = rooms
        self.position = "A"

    def perceive(self):
        """Return the current room's condition."""
        return self.rooms[self.position]

    def act(self):
        """Choose an action based on the current perception."""
        if self.perceive() == "Dirty":
            self.rooms[self.position] = "Clean"
            return "SUCK"

        # Move to the other room
        if self.position == "A":
            self.position = "B"
            return "RIGHT"
        else:
            self.position = "A"
            return "LEFT"

    def is_clean(self):
        """Check whether all rooms are clean."""
        return all(condition == "Clean" for condition in self.rooms.values())

    def run(self):
        """Run the agent until every room is clean."""
        actions = []

        while not self.is_clean():
            action = self.act()
            actions.append(action)

        return actions


# ---------------------------------------------------------
# TEST CASES
# ---------------------------------------------------------

def test_both_rooms_dirty():
    rooms = {
        "A": "Dirty",
        "B": "Dirty"
    }

    agent = VacuumCleanerAgent(rooms)
    actions = agent.run()

    print("Test 1: Both rooms dirty")
    print("Actions:", actions)
    print("Final state:", agent.rooms)
    print("Position:", agent.position)
    print()


def test_room_A_dirty():
    rooms = {
        "A": "Dirty",
        "B": "Clean"
    }

    agent = VacuumCleanerAgent(rooms)
    actions = agent.run()

    print("Test 2: Room A dirty, Room B clean")
    print("Actions:", actions)
    print("Final state:", agent.rooms)
    print("Position:", agent.position)
    print()


def test_room_B_dirty():
    rooms = {
        "A": "Clean",
        "B": "Dirty"
    }

    agent = VacuumCleanerAgent(rooms)
    actions = agent.run()

    print("Test 3: Room A clean, Room B dirty")
    print("Actions:", actions)
    print("Final state:", agent.rooms)
    print("Position:", agent.position)
    print()


def test_both_rooms_clean():
    rooms = {
        "A": "Clean",
        "B": "Clean"
    }

    agent = VacuumCleanerAgent(rooms)
    actions = agent.run()

    print("Test 4: Both rooms clean")
    print("Actions:", actions)
    print("Final state:", agent.rooms)
    print("Position:", agent.position)
    print()


# Run all test cases
if __name__ == "__main__":
    test_both_rooms_dirty()
    test_room_A_dirty()
    test_room_B_dirty()
    test_both_rooms_clean()
