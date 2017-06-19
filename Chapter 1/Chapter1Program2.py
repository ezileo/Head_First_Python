word = "bottles"
for beer_num in range(99, 0, -1):
        print(beer_num, word, "of beers on the wall.")
        print(beer_num, word, "of beer.")
        print("Take one down...")
        print("Pass it around...")
        if beer_num == 1:
            print("No more bottles on the wall.")
        else:
            now_num = beer_num - 1
            if now_num == 1:
                word = "bottle"
                print(now_num, word, "of beer on the wall.")
        print()
