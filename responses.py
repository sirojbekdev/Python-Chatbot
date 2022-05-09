import random
def fun_fact():
    facts = [
        'More presidents, eight in all, have been from Virginia than any other state. These presidents include George Washington, Thomas Jefferson, James Madison, James Monroe, William Henry Harrison, Zachary Taylor, John Tyler, and Woodrow Wilson. However, Virginia hasn\'t been the birthplace of a president in over 100 years.',
        "Long before the 25th Amendment determined the transition of power between presidents and vice presidents, several presidents passed away while serving in office. \nWilliam Henry Harrison died of pneumonia. \nZachary Taylor died of inflammation of the stomach and intestines. \nWarren G. Harding died of a heart attack. \nFranklin D. Roosevelt died of a stroke. \nAbraham Lincoln, James A. Garfield, William McKinley, and John F. Kennedy were assassinated.",
        "Five Presidents Won Without the Popular Vote: \nJohn Quincy Adams, Rutherford B. Hayes, Benjamin Harrison, George W. Bush, and Donald Trump all won the presidency without winning the popular vote. Adams, Harrison and Trump were one-term presidents who went on to lose both the popular and electoral votes in their bids for reelection. Hayes did not run for reelection, and Bush was reelected after winning both the popular and electoral votes in his second election.",
        "Franklin D. Roosevelt won four elections: 1932, 1936, 1940, and 1944. He died of a stroke in April 1945, just a few months into his final term, leaving Vice President Harry Truman to oversee the end of World War II. In 1947, Congress passed the 22nd Amendment, which limited future presidents' terms to a maximum of two.",
        "The U.S. Had An Unelected President For Two Years: \nThere was a two-year span when the president leading the country was not elected. After Spiro T. Agnew resigned as vice president in 1973, Richard Nixon appointed Gerald Ford as vice president. When Nixon resigned the next year, Ford became president and Nelson Rockefeller was appointed vice president."
    ][random.randrange(5)]
    return facts

# short responses for user message
shorts = [
    {
        "bot_response": 'Hello!',
        "list_of_words": ['hello', 'hi', 'hey', 'sup', 'heyo'],
        "required_words": []
    },
    {
        "bot_response": 'See you!!',
        "list_of_words":  ['bye', 'goodbye'],
        "required_words": []
    },
    {
        "bot_response": 'I\'m doing fine, and you?',
        "list_of_words":   ['how', 'are', 'you', 'doing'],
        "required_words": ['how']
    },
    {
        "bot_response": 'You\'re welcome!',
        "list_of_words":   ['how', 'are', 'you', 'doing'],
        "required_words": ['how']
    },
]


# longer responses for user message
longs = [
    {
        "bot_response": fun_fact(),
        "list_of_words":   ['tell', 'fun', 'fact', 'facts', 'usa'],
        "required_words": ['fun', 'fact']
    },
    {
        "bot_response": "Joseph Robinette Biden Jr. is an American politician who is the 46th and current president of the United States. A member of the Democratic Party, he served as the 47th vice president from 2009 to 2017 under Barack Obama and represented Delaware in the United States Senate from 1973 to 2009.",
        "list_of_words":   ['who', 'is', 'current', 'president', 'usa'],
        "required_words": ['current', 'president', 'who']
    },
    {
        "bot_response": "On April 30, 1789, George Washington, standing on the balcony of Federal Hall on Wall Street in New York, took his oath of office as the first President of the United States.",
        "list_of_words":   ['who', 'is', 'was', 'first', 'president', 'usa'],
        "required_words": ['president', 'first', 'who']
    },
    {
        "bot_response": "In 2008, Barack Obama became the first African American president in U.S. history. Obama's father was a Kenyan economist and his mother was a white anthropologist. Obama's legacy continued when Kamala Harris became the first Black woman elected to be vice president.",
        "list_of_words":   ['who', 'is', 'was', 'first', 'president', 'usa'],
        "required_words": ['president', 'first', 'who', 'black']
    },
    {
        "bot_response": "The youngest elected president so far was John F. Kennedy, who became president when he was 43.  The youngest president to serve was Theodore Roosevelt, who became president at 42 after Mc Kinley was assassinated.",
        "list_of_words":   ['who', 'is', 'was', 'youngest', 'president', 'usa'],
        "required_words": ['youngest', 'president', 'who']
    },
    {
        "bot_response": "So far, the oldest president was Joe Biden, who was 78 when he was sworn in. ",
        "list_of_words":   ['who', 'is', 'was', 'youngest', 'president', 'usa'],
        "required_words": ['oldest', 'president', 'who']
    },
    {
        "bot_response": "In other U.S. elections, candidates are elected directly by popular vote. But the president and vice president are not elected directly by citizens. Instead, they're chosen by “electors” through a process called the Electoral College. The process of using electors comes from the Constitution.",
        "list_of_words":   ['how', 'president', 'is', 'elected'],
        "required_words": ['how', 'elected', 'president']
    },
    {
        "bot_response": "The president is elected indirectly through the Electoral College to a four-year term, along with the vice president.",
        "list_of_words":   ['how', 'long', 'president', 'is', 'term'],
        "required_words": ['how', 'elected', 'long']
    }
]



# default response if there is no match
def no_response_wiki_advice():
    response = ["Could you please re-phrase that? ",
                "..., You could search it on wikipedia",
                "What does that mean?,\nTry to search it on wikipedia",
                "I do not get it!!!"][
        random.randrange(4)]
    return response
