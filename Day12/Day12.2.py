# After noticing (using step one) that after 130 iterations the sum grows linearly I can write explicitly
iterations_num = 50000000000
iterations_skipped = 130
positions_sum = 8632  # Sum at step 130.
sum_growth_during_iteration = 52
positions_sum += sum_growth_during_iteration * (iterations_num - iterations_skipped)

print(positions_sum)
