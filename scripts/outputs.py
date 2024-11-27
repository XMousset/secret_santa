from pathlib import Path

import yagmail

from scripts.config import CONFIG


def christmas_message(gifter, receiver):
    text = "GIFTER, you are the Secret Santa of RECEIVER.\n\n"
    
    if len(receiver.gifts_ideas) > 0:
        text = text + f"RECEIVER gave you a list of ideas :\nGIFTS_IDEAS"
    else:
        text = (text + "Unfortunately, RECEIVER did not gave you a list "
                + "of ideas...\n")
    
    text = text.replace("GIFTER", gifter.name)
    text = text.replace("RECEIVER", receiver.name)
    text = text.replace("GIFTS_IDEAS", receiver.gifts_ideas)
    return text


def create_txt_files(text, gifter):
    """Manage outputs either as mails or .txt files.

    Parameters
    ----------
    gifter : ChristmasFriend
        The friend who will offer a gift to the receiver.
    receiver : ChristmasFriend
        The friend who will receive a gift from the gifter.
    receiver : str
        The path of the folder where to save .txt files.
    """
    save_folder = CONFIG["outputs text folder"]
    txt_path = Path(save_folder, gifter.name + " - Your Secret Santa.txt")
    with open(txt_path, mode= "w") as f:
        f.write(text)


def send_email(text, friend):
    """Send email using yagmail.

    Parameters
    ----------
    text : str
        The message inside the email.
    gifter : ChristmasFriend
        The friend who will receive the email.
    """
    # mail = yagmail.SMTP(CONFIG["sending address"])
    # mail.send(friend.mail, CONFIG["mail subject"], text)
    # mail.close()
    print(f"Email sent to {friend.mail}")