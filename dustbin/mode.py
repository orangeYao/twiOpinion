def mode():
    mode = raw_input(
            "The three available classification mode you can select:\n"
            + "1. set all grabed tweets as category 1 and grab category 2 by new (opposite) tag \n"
            + "2. classify grabed tweets by selecting key words \n"
            + "3. classify grabed tweets one by one manually \n"
            + "select the mode you want by typing corresponding number: "
            )  or "2"

    if (mode == "1"):
        file_name2, pw2 = grabSetting()

    if (mode == "2"):
        words_category1 = raw_input("Type in the key words requirements for a tweet to be classified as category 1:"
                            + "seperate alternative words by \"or\"") or "good"
        words_category2 = raw_input("Type in the key words requirements for a tweet to be classified as category 2:"
                            + "seperate alternative words by \"or\"") or "bad"
        mode2(file_name, words_category1, words_category2)

    if (mode == "3"):
        judge = raw_input("For each tweet displayed, type \"1\" for category 1 and \"2\" for category 2, \"0\" to skip and \"q\" to stop labeling")
