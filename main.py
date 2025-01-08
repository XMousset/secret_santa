from scripts.christmas_friends import load_friends_from_tsv, saving, loading
from scripts.attribution_solver import find_solution
from scripts.outputs import christmas_message, create_txt_files, send_email
from scripts.config import CONFIG

FROM_SAVE = False

if __name__ == "__main__":
    
    # attributions
    if FROM_SAVE:
        attributions = loading()
    
    else:
        friends = load_friends_from_tsv()
        attributions, nb_iters = find_solution(friends)
        
        if CONFIG["print attributions"]:
            print(f"Found in {nb_iters} iterations")
            print(f"Total loops = {len(attributions)-len(friends)}")
            print(attributions)
        
        saving(attributions)
    
    # outputs
    for gifter, receiver in zip(attributions[:-1], attributions[1:]):
        message = christmas_message(gifter, receiver)
        
        if CONFIG["create .txt"]:
            create_txt_files(message, gifter)
        
        if CONFIG["send mails"]:
            send_email(message, gifter)
