from christmas_friends import load_friends_from_tsv
from attribution_solver import find_solution
from outputs import christmas_message, create_txt_files, send_email
from config import CONFIG

if __name__ == "__main__":
    friends = load_friends_from_tsv()
    attributions, nb_iters = find_solution(friends)
    
    if CONFIG["print attributions"]:
        print(f"Found in {nb_iters} iterations")
        print(f"Total loops = {len(attributions)-len(friends)}")
        print(attributions)
    
    for gifter, receiver in zip(attributions[:-1], attributions[1:]):
        message = christmas_message(gifter, receiver)
        
        if CONFIG["create .txt"]:
            create_txt_files(message, gifter)
        
        if CONFIG["send mails"]:
            send_email(message, gifter)
