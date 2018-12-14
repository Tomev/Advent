def count_number_of_recipes_until_input_occurrence(n):
    n = [int(i) for i in n]
    scores = [3, 7]
    elves_positions = [0, 1]
    last_scores = scores[:]
    position = 0

    while True:

        # Check if we got input
        if last_scores == n:
            break

        # Check if we got input
        if last_scores == n:
            break

        # Count new score
        new_choco_score = 0

        for elf_pos in elves_positions:
            new_choco_score += scores[elf_pos]

        # Add this score to board
        new_choco_score = str(new_choco_score)

        for char in new_choco_score:
            scores.append(int(char))
            last_scores.append(int(char))

        # Move elves
        for j in range(len(elves_positions)):
            elves_positions[j] = (elves_positions[j] + 1 + scores[elves_positions[j]]) % len(scores)

        # Trim last_scores
        while len(last_scores) > len(n):
            position += 1
            last_scores = last_scores[1:]

            if last_scores[:-1] == n:
                return position

            if last_scores == n:
                return position

    return position


assert count_number_of_recipes_until_input_occurrence('51589') == 9
assert count_number_of_recipes_until_input_occurrence('01245') == 5
assert count_number_of_recipes_until_input_occurrence('92510') == 18
assert count_number_of_recipes_until_input_occurrence('59414') == 2018

print(f'The scores of the ten recipes immediately after the number of recipes in your puzzle input is \
{count_number_of_recipes_until_input_occurrence("793061")}.')
