    # YOUR PROJECT TITLE
    #### Video Demo:  <URL HERE>
    #### Description:


    ###########################
    #
    #   Word json file prep
    #
    ###########################
    Directory data_prep/

    get_word_file.py
        Retrived list of no swear words
        from https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-no-swears.txt

    create_word_complexity_json.py
        Loops through google-10000-english-no-swears.txt to create json file
        Performs API call to get definition of word from https://api.dictionaryapi.dev/api/v2/entries/en/{word}
        letter_count #
        syllable_count #
        phonetic_complexity True/False
        morphological_complexity True/False
