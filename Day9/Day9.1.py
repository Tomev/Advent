def play_the_game(players_num, last_marble_score):
    winning_score = 0
    current_marble = 1
    game = [0, 1]
    current_player = 1
    current_marble_index = 1

    players_score = []
    for i in range(0, players_num):
        players_score.append(0)

    while current_marble != last_marble_score:
        current_marble += 1
        current_player = (current_player + 1) % players_num

        if current_marble % 23 == 0:
            players_score[current_player] += current_marble
            additional_score_marble_index = current_marble_index - 7

            if additional_score_marble_index < 0:
                additional_score_marble_index = len(game) + additional_score_marble_index

            players_score[current_player] += game[additional_score_marble_index]
            game.remove(game[additional_score_marble_index])
            current_marble_index = additional_score_marble_index

            if players_score[current_player] > winning_score:
                winning_score = players_score[current_player]

        else:
            new_marble_position = (current_marble_index + 2)

            if new_marble_position == 0  % len(game):
                game.append(current_marble)
            else:
                new_marble_position = new_marble_position % len(game)
                game.insert(new_marble_position, current_marble)

            current_marble_index = new_marble_position

    return winning_score


file_read = open("input.txt", "r")
line = file_read.readline()

PLAYERS_NUM = int(line.split(' ')[0])
LAST_MARBLE_SCORE = int(line.split('worth ')[1].split(' ')[0])

assert play_the_game(9, 25) == 32, 'TEST'

# TESTS
assert play_the_game(10, 1618) == 8317, '1st assertion failed'
assert play_the_game(13, 7999) == 146373, '2nd assertion failed'
assert play_the_game(17, 1104) == 2764, '3rd assertion failed'
assert play_the_game(21, 6111) == 54718, '4th assertion failed'
assert play_the_game(30, 5807) == 37305, '5th assertion failed'

print(f'Winning elf score is {play_the_game(PLAYERS_NUM, LAST_MARBLE_SCORE)}.')






