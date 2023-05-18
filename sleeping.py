import random
max_count = 1000

if __name__ == "__main__":
    awake_days = []
    coin_flip = []
    random.seed()
    for count in range(max_count):
        # if True, heads
        if random.choice([True, False]):
            # wakes only on Monday
            awake_days.append("Monday")
            coin_flip.append("heads")
        else:
            # wakes on both Monday and Tuesday
            awake_days.append("Monday")
            coin_flip.append("tails")
            awake_days.append("Tuesday")
            coin_flip.append("tails")
    mon_heads = 0
    mon_tails = 0
    tues_tails = 0
    for flip_count in range(len(awake_days)):
        if awake_days[flip_count] == "Tuesday":
            tues_tails += 1
        else:
            if coin_flip[flip_count] == "heads":
                mon_heads += 1
            else:
                mon_tails += 1
    print("Monday heads:", mon_heads)
    print("Monday tails:", mon_tails)
    print("Tuesday tails", tues_tails)
