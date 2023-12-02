from collections import defaultdict
from functools import reduce


def parse_game(game):
    game_information, rest = game.split(":")
    game_number = game_information.split()[1]

    game_turns = [turn.strip() for turn in rest.split(";")]
    turn_moves = [[move.strip() for move in turn.split(",")] for turn in game_turns]
    game_list = []
    for turn in turn_moves:
        game_sum = {
            move.split()[1].strip(): int(move.split()[0].strip()) for move in turn
        }
        game_list.append(game_sum)

    return {"game_nr": int(game_number), "turns": game_list}


def one():
    max_conf = dict(red=12, green=13, blue=14)

    with open("input/input.txt") as file:
        games = [line for line in file.readlines()]

    invalid_games = set()
    parsed_games = [parse_game(game) for game in games]
    for parsed_game in parsed_games:
        for turn in parsed_game["turns"]:
            for move, value in turn.items():
                if value > max_conf[move]:
                    invalid_games.add(parsed_game["game_nr"])
                    break

    print(
        sum(
            [
                game["game_nr"]
                for game in parsed_games
                if game["game_nr"] not in invalid_games
            ]
        )
    )


def two():
    with open("input/input.txt") as file:
        games = [line for line in file.readlines()]

    parsed_games = [parse_game(game) for game in games]
    all_results = []

    for parsed_game in parsed_games:
        game_set = defaultdict(list)
        for turn in parsed_game["turns"]:
            for move, value in turn.items():
                game_set[move].append(value)
        game_result = reduce(lambda x, y: x * y, [max(v) for v in game_set.values()])
        all_results.append(game_result)

    print(sum(all_results))


if __name__ == "__main__":
    two()
