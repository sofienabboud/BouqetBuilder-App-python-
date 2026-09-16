

##Flower Bouqet App

##Read Me

"""
Workflow for the Game class:

START SCREEN:
    1. Open app
    2. Show welcome screen
    3. Ask user:
        - New Game
        - Load Saved Game

IF NEW GAME:
    1. Ask for pot color
    2. Ask for flower seed choice
    3. Give user $500
    4. Start game screen

GAME SCREEN:
    1. Show current flower, pot, money, and water level
    2. Let user choose an action:
        - Water flower
        - Check inventory
        - Go to shop
        - Quit/save game

WATER FLOWER:
    1. User chooses how much water to pour
    2. Increase flower water level
    3. Show updated water level
    4. If water level is perfect:
        - Flower blooms
        - Add flower to inventory
        - Let user plant a new seed
    5. If water level is too high:
        - Flower dies
        - User must plant a new seed

INVENTORY:
    1. Show how many bloomed flowers the user has
    2. If user has 12 flowers:
        - Allow ribbon purchase from shop

SHOP:
    1. Show shop items
    2. If user has enough flowers/money:
        - Buy ribbon
    3. Otherwise:
        - Tell user they need more flowers or money

-These are the methods that the game class would need:
    start()
    show_welcome_screen()
    new_game()
    load_game()
    game_screen()
    water_flower()
    check_inventory()
    open_shop()
    plant_new_seed()
    save_game()
    quit_game()

    """

