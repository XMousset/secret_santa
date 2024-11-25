import yagmail
import keyring

from christmas_friends import ChristmasFriend
from outputs import christmas_message, send_email
from christmas_friends import load_config

CONFIG_NAME = "config.json"
TRY_SENDING = False

config = load_config(CONFIG_NAME)

# to register your email address and password
# yagmail.register(config["sending address"], "yourpassword")
# to delete your email address and password
# keyring.delete_password("yagmail", config["sending address"])

to_me = ChristmasFriend(**{
    "Name": "Your Name",
    "Email": "receiver_address@awesome.com",
    "Exclusions": "",
    "Gifts ideas": "I would like an orange for Christmas."
})

message = christmas_message(to_me, to_me)
if TRY_SENDING:
    send_email(message, to_me, **config)
