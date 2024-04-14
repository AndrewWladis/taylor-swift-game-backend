from flask import Flask, jsonify
from datetime import datetime
import json
import math
import random

app = Flask(__name__)

@app.route('/today-challenge', methods=['GET'])
def random_quote():
    now = datetime.now()
    num = (((now.weekday() + 3) * (now.day + now.month + 1)) + now.month) * 3

    # Load the JSON data from the file
    with open('lyrics_array.json', 'r') as f:
        data = json.load(f)

    all_songs = ['22', 'All Too Well (10 Minute Version) [From The Vault]',
                 'Babe [From The Vault]', 'Begin Again',
                 'Better Man [From The Vault]', 'Come Back...Be Here',
                 'Everything Has Changed', 'Forever Winter [From The Vault]',
                 'Girl At Home', 'Holy Ground', 'I Almost Do',
                 'I Bet You Think About Me [From the Vault]',
                 'I Knew You Were Trouble',
                 'Message In A Bottle [From The Vault]',
                 'Nothing New [From The Vault]', 'Red',
                 'Ronan', 'Run [From The Vault]',
                 'Sad Beautiful Tragic', 'Starlight',
                 'State of Grace', 'Stay Stay Stay',
                 'The Last Time', 'The Lucky One',
                 'The Moment I Knew', 'The Very First Night [From The Vault]',
                 'Treacherous', 'We Are Never Ever Getting Back Together',
                 'Afterglow', 'Cornelia Street', 'Cruel Summer', 'Daylight', 'Death By A Thousand Cuts', 'False God',
                 'I Forgot That You Existed', 'I Think He Knows', 'It’s Nice To Have A Friend', 'London Boy', 'Lover',
                 'ME!', 'Miss Americana & The Heartbreak Prince', 'Paper Rings', "Soon You'll Get Better", 'The Archer',
                 'The Man', 'You Need To Calm Down', 'All Of The Girls You Loved Before',
                 'All You Had To Do Was Stay', 'Bad Blood',
                 'Blank Space', 'Clean',
                 'How You Get The Girl', 'I Know Places',
                 'Is It Over Now? [From The Vault]', 'I Wish You Would',
                 'New Romantics', 'Now That We Don’t Talk [From The Vault]',
                 'Out Of The Woods', 'Say Don’t Go [From The Vault]',
                 'Shake It Off', '“Slut!” [From The Vault]',
                 'Style', 'Suburban Legends [From The Vault]',
                 'Sweeter Than Fiction', 'This Love',
                 'Welcome To New York', 'Wildest Dreams',
                 'Wonderland', 'You Are In Love', 'Anti-Hero', 'Bejeweled',
                 'Bigger Than The Whole Sky', 'Dear Reader', 'Glitch', 'High Infidelity', 'Karma', 'Labyrinth',
                 'Lavender Haze', 'Maroon', 'Mastermind', 'Midnight Rain', 'Paris', 'Question...?', 'Snow On The Beach',
                 'Sweet Nothing', 'The Great War', 'Vigilante Shit', 'Would’ve, Could’ve, Should’ve',
                 'You’re On Your Own, Kid', 'Back To December',
                 'Better Than Revenge', 'Castles Crumbling [From The Vault]',
                 'Dear John', 'Electric Touch [From The Vault]',
                 'Enchanted', 'Foolish One [From The Vault]',
                 'Haunted', 'I Can See You [From The Vault]',
                 'Innocent', 'Last Kiss', 'Long Live',
                 'Mean', 'Mine', 'Never Grow Up',
                 'Ours', 'Sparks Fly', 'Speak Now',
                 'Superman', 'The Story Of Us',
                 'Timeless [From The Vault]',
                 'When Emma Falls in Love [From The Vault]', 'Bad Blood (Remix)',
                 'Breathe', 'Bye Bye Baby [From the Vault]',
                 'Change', 'Come In With The Rain',
                 'Don’t You [From the Vault]', 'Fearless',
                 'Fifteen', 'Forever & Always', 'Hey Stephen',
                 'Jump Then Fall', 'Love Story',
                 'Mr. Perfectly Fine [From the Vault]', 'Superstar',
                 'Tell Me Why', 'That’s When [From the Vault]',
                 'The Best Day', 'The Other Side of the Door',
                 'The Way I Loved You', 'Today Was a Fairytale',
                 'Untouchable', 'We Were Happy [From the Vault]',
                 'White Horse', 'You All Over Me [From the Vault]',
                 'You Belong With Me', 'You’re Not Sorry',
                 'Call It What You Want', 'Dancing With Our Hands Tied', 'Delicate', 'Don’t Blame Me', 'Dress',
                 'End Game', 'Getaway Car', 'Gorgeous', 'I Did Something Bad', 'King of My Heart',
                 'Look What You Made Me Do', 'New Year’s Day', 'So It Goes...', 'This Is Why We Can’t Have Nice Things',
                 '...Ready for It?', 'Hits Different', 'If This Was a Movie',
                 'You’re Losing Me (From The Vault)', 'august', 'betty', 'cardigan', 'epiphany', 'exile', 'hoax',
                 'illicit affairs', 'invisible string', 'mad woman', 'mirrorball', 'my tears ricochet', 'peace',
                 'seven', 'the 1', 'the last great american dynasty', 'this is me trying', 'champagne problems',
                 'closure', 'coney island', 'cowboy like me', 'dorothea', 'evermore', 'gold rush', 'happiness', 'ivy',
                 'long story short', 'marjorie', 'no body, no crime', '’tis the damn season', 'tolerate it', 'willow',
                 'the lakes']
    lyrics_array = []
    quiz_list = []

    # Iterate through each song and its lyrics
    for album_data in data:
        songs = album_data['songs']
        for song_data in songs:
            lyrics = song_data['lyrics']
            for lyric in lyrics:
                lyrics_array.append([lyric, song_data['song']])

    while len(quiz_list) < 11:
        j = math.ceil((num / 40))

        for i in range(num, len(lyrics_array), num):
            item = {
                "quote": {
                    "quote": lyrics_array[i][0],
                    "author": lyrics_array[i][1]
                },
                "options": []
            }
            supporting_songs = []
            while len(supporting_songs) < 3:
                if math.ceil((num / 13)) > len(all_songs):
                    supporting_songs = ['22',
                                        'All Too Well (10 Minute Version) [From The Vault]',
                                        'no body, no crime']

                if j >= len(all_songs):
                    j = math.ceil((num / 22))

                supporting_songs.append(all_songs[j])
                j += math.ceil((num / 22))

            supporting_songs.insert((len(lyrics_array[i][0]) % 4), item["quote"]["author"])
            item["options"] = supporting_songs

            quiz_list.append(item)



    return jsonify(quiz_list[::-1])

if __name__ == '__main__':
    app.run(debug=True)
