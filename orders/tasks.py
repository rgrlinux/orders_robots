import os
from robocorp.tasks import task
from robocorp import browser
from RPA.HTTP import HTTP
from RPA.Tables import Tables


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
    list_and_send_orders()


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


def get_orders():
    """Load csv into table"""
    tables = Tables()
    table_data = tables.read_table_from_csv('orders.csv')
    return table_data


def list_and_send_orders():
    """List orders ans send each to fill form"""
    orders = get_orders()
    for order in orders:
        fill_form_and_order(order)


def fill_form_and_order(order):
    """Receive one order and fill form"""
    page = browser.page()
    page.select_option('#head', str(order['Head']))
    body = f'#id-body-{str(order["Body"])}'
    page.set_checked(body, True)
    page.fill(selector='//input[@type="number"]', value=str(order['Legs']))
    page.fill('#address', order['Address'])
    page.click('text=Order')
