
from robocorp.tasks import task
from robocorp import browser


@task
def order_robots_from_RobotSpareBin():
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
    browser.configure(slowmo=1000)
    open_robot_order_wbesite()


def open_robot_order_wbesite():
    """Navegate to order page"""
    browser.goto('https://robotsparebinindustries.com/#/robot-order')
