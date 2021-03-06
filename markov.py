from random import choice


def open_and_read_file(file_path):
    contents = open(file_path).read().replace("\n", " ")

    return contents


def make_chains(text_string):
    chains = {}

    words = text_string.split()
    for i in range(len(words) - 2):
        if (words[i], words[i + 1]) not in chains:
            chains[(words[i], words[i + 1])] = [words[i + 2]]
        else:
            chains[(words[i], words[i + 1])].append(words[i + 2])
    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = [list(chains)[0][0], list(chains)[0][1]]

    i = 0
    while '.' not in words[-1]:
        words.append(choice(chains[(words[i], words[i + 1])]))
        i += 1

    print(' '.join(words))


input_path = 'beemovie.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)
