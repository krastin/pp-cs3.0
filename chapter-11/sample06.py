bird_to_observations = {'canada goose': 5, 'northern fulmar': 1, 'long-tailed jaeger': 2, 'snow goose': 1}
# Invert the dictionary
observations_to_birds_list = {}
for bird, observations in bird_to_observations.items():
    if observations in observations_to_birds_list:
        observations_to_birds_list[observations].append(bird)
    else:
        observations_to_birds_list[observations] = [bird]

print(observations_to_birds_list)

observations_sorted = sorted(observations_to_birds_list.keys())
for observations in observations_sorted:
    print(observations, ':', end=" ")
    for bird in observations_to_birds_list[observations]:
        print(' ', bird, end=" ")
    print()
