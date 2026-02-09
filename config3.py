import logging
import os

from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options

logging.basicConfig(
    level=logging.INFO,  # или logging.DEBUG для более детального вывода
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
import utils.file
load_dotenv()

context = os.getenv("CONTEXT")
if not context:
    raise RuntimeError("context is not set")

load_dotenv(f".env.{context}")

remote_url = os.getenv('REMOTE_URL', '').rstrip('/')  # Убираем слеш в конце
deviceName = os.getenv('DEVICE_NAME')  # Значение по умолчанию
platformName = os.getenv('PLATFORM_NAME', 'Android')
platformVersion = os.getenv('PLATFORM_VERSION', '13.0')
automationName = os.getenv('AUTOMATION_NAME', 'UiAutomator2')
appWaitActivity = 'org.wikipedia.*'
app = os.getenv('app', 'apps/app-alpha-universal-release.apk')



def to_driver_options():
    options = UiAutomator2Options()
    logger.info(context)
    logger.info(remote_url)

    if deviceName:
        options.set_capability('deviceName', deviceName)
    logger.info(deviceName)
    if appWaitActivity:
        options.set_capability('appWaitActivity', appWaitActivity)

    options.set_capability('appium:appPackage', 'org.wikipedia.alpha')
    options.set_capability('appium:appActivity', 'org.wikipedia.main.MainActivity')

    options.set_capability('app',
                           '/Users/alena/Documents/QA_GURU/qa_guru_homework_20/apps/app-alpha-universal-release.apk')


    return options
