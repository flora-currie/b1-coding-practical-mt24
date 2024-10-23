from .dynamic import Mission

# Test function to check if the class reads the CSV file correctly
def test_mission():
    mission_instance = Mission.from_csv('data/mission.csv')  
    print(mission_instance)

test_mission()