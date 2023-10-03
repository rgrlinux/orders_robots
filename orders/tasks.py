import os
from robocorp.tasks import task
from robocorp import browser
from RPA.HTTP import HTTP


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
    open_robot_order_website()
    close_annoying_modal()
    download_csv_file()


def open_robot_order_website():
    """Navegate to order page"""
    browser.goto('https://robotsparebinindustries.com/#/robot-order')


def close_annoying_modal():
    page = browser.page()
    page.click('text=OK')


def download_csv_file():
    """Dowload csv file from http"""
    http = HTTP()
    http.download('https://robotsparebinindustries.com/orders.csv',
                  os.getcwd(), overwrite=True)
