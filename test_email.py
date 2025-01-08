from scripts.christmas_friends import ChristmasFriend
from scripts.outputs import christmas_message, send_email
from scripts.config import CONFIG

TRY_SENDING = False

to_me = ChristmasFriend(**{
        "Name": "Your Name",
        "Email": "receiver_address@awesome.com",
        "Exclusions": "",
        "Gifts ideas": "I would like an orange for Christmas."
    })

if __name__ == "__main__":
    message = christmas_message(to_me, to_me)
    
    if TRY_SENDING:
        if (CONFIG["sending address"] == "your-python-email@gmail.com"
            or to_me.mail == "receiver_address@awesome.com"):
            raise ValueError("You need to put valid email in 'config.json'" \
                " and for the 'to_me' ChristmasFriend")
        
        send_email(message, to_me)
