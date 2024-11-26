from christmas_friends import load_config, tsv2friends
from attribution_solver import find_solution
from outputs import christmas_message, create_txt_files, send_email

CONFIG_NAME = "config.json"

if __name__ == "__main__":
    """The main function, must be run."""
    config = load_config(CONFIG_NAME)
    friends = tsv2friends(config["tsv name"])
    attributions, nb_iters = find_solution(friends, **config)
    
    if config["print attributions"]:
        print(f"Found in {nb_iters} iterations")
        print(f"Total loops = {len(attributions)-len(friends)}")
        print(attributions)
    
    for gifter, receiver in zip(attributions[:-1], attributions[1:]):
        message = christmas_message(gifter, receiver)
        
        if config["create .txt"]:
            create_txt_files(message, gifter, config["outputs text folder"])
        
        if config["send mails"]:
            send_email(message, gifter, **config)
