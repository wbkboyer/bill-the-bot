# bill-the-bot

Bill is an agent that learns to play the game of tic-tac-toe with self-play using Q-learning. Before he is able to master the game, he must play the game by random decisions to explore his options during the game. He remembers which moves that might expect to make him win, and then he uses this information to make intelligent choices in future games.

- Run **app.py** to start the graphical interface and challenge a pre-trained agent.
- Run **trainPlayerX.py** to start training an agent. 
- **tictactoe** contains the game environment of tictactoe, the agent definition and the code that simulates the training.
- Required packages are found in **requirements.txt**, install by typing *pip install -r requirements.txt*

[![Run on Repl.it](https://repl.it/badge/github/RickardKarl/bill-the-bot)](https://repl.it/github/RickardKarl/bill-the-bot)