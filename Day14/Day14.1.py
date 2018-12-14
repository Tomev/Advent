def count_score_after_n_recipes(n):
    scores = [3, 7]
    elves_positions = [0, 1]

    while len(scores) < n + 10:
        new_choco_score = 0

        # Count new score
        for elf_pos in elves_positions:
                new_choco_score += scores[elf_pos]

        # Add this score to board
        new_choco_score = str(new_choco_score)

        for char in new_choco_score:
            scores.append(int(char))

        # Move elves
        for j in range(len(elves_positions)):
            elves_positions[j] = (elves_positions[j] + 1 + scores[elves_positions[j]]) % len(scores)

    score = ''

    for i in range(10):
        score += str(scores[n + i])

    return score


assert count_score_after_n_recipes(9) == '5158916779'
assert count_score_after_n_recipes(5) == '0124515891'
assert count_score_after_n_recipes(18) == '9251071085'
assert count_score_after_n_recipes(2018) == '5941429882'

print(f'The scores of the ten recipes immediately after the number of recipes in your puzzle input is \
{count_score_after_n_recipes(793061)}.')
