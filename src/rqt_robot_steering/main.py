import sys

from rqt_gui.main import Main


def main():
    main = Main()
    sys.exit(main.main(sys.argv, standalone='rqt_robot_steering.robot_steering.RobotSteering'))


if __name__ == '__main__':
    main()
