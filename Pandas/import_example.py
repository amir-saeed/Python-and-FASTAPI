class RobotFactory:
    robot_count = 0  # Class attribute

    def __init__(self, name):
        self.name = name
        RobotFactory.robot_count += 1

    @staticmethod
    def make_tool(tool_name):
        print(f"Making a {tool_name} tool!")

    @classmethod
    def show_robot_count(cls):
        print(f"Total robots made: {cls.robot_count}")

# Using the factory
RobotFactory.make_tool("wrench")  # Toolmaker makes a tool
RobotFactory.show_robot_count()  # Blueprint reader shows robot count

robot1 = RobotFactory("Robo1")
robot2 = RobotFactory("Robo2")

RobotFactory.show_robot_count() # shows the updated robot count.