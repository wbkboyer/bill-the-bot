from tictactoe.board import Board
from tictactoe.simulation import simulate

if __name__ == "__main__":

    # Train two agents against each other
    agent1, agent2 = simulate(exploration=True)
    agent1, agent2 = simulate(agent1=agent1, exploration=False)

