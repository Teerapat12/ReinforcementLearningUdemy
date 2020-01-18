from rl.tictactoe.player import Player
from rl.tictactoe.env import TicTacToeEnv
from rl.tictactoe.agent import Agent
from collections import Counter
def main():
    player = Player(2)
    agent_1 = Agent(1)
    agent_1.load_state("agent_model/iteration_3_a1.npy")
    agent_3 = Agent(3)
    agent_3.load_state("agent_model/iteration_2_a3.npy")
    game = TicTacToeEnv()

    def play_game(p1, p2, env, max_mistake_move = 50):
        current_player = None
        while env.check_is_end() < 0:
            if current_player == p1:
                current_player = p2
            else:
                current_player = p1

            while max_mistake_move > 0:
                if not current_player.play_game(env):
                    max_mistake_move-=1
                else:
                    break
            p1.update_state_history(env)
            p2.update_state_history(env)

            # print(env.get_board())

        p1.update_state_value_maps(game)
        p2.update_state_value_maps(game)
        game_result = env.check_is_end()
        # print_game_result(game_result)
        return game_result

    def print_game_result(game_result):
        if game_result == 0:
            print("Draw")
        else:
            print("Game End! - %d win!" % game_result)

    def print_dash_line():
        print("=" * 50)

    game_iterations = 1000000
    winner_counts = []
    for i in range(game_iterations):
        winner = play_game(agent_1, agent_3, game)
        winner_counts.append(winner)
        if i % 5000 == 0 : print(i)
        # print(agent_1.state_value_map)
        # print(game.calculate_reward(3))
        game.reset_board()
    print(Counter(winner_counts))

    # play_game(agent_1, player, game)
    agent_1.save_state("agent_model/iteration_4_a1")
    agent_3.save_state("agent_model/iteration_4_a3")

if __name__ == '__main__':
    main()

# main()