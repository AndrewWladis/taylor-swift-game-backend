from flask import Flask, jsonify
from datetime import datetime
import json
import math
import random

app = Flask(__name__)

@app.route('/today-challenge', methods=['GET'])
def random_quote():
    now = datetime.now()
    num = ((now.weekday() + 3) * (now.day + now.month + 1) * 2)

    # Load the JSON data from the file
    with open('lyrics_array.json', 'r') as f:
        data = json.load(f)

    all_songs = ['22 (Taylor’s Version)', 'All Too Well (10 Minute Version) (Taylor’s Version) [From The Vault]',
                 'Babe (Taylor’s Version) [From The Vault]', 'Begin Again (Taylor’s Version)',
                 'Better Man (Taylor’s Version) [From The Vault]', 'Come Back...Be Here (Taylor’s Version)',
                 'Everything Has Changed (Taylor’s Version)', 'Forever Winter (Taylor’s Version) [From The Vault]',
                 'Girl At Home (Taylor’s Version)', 'Holy Ground (Taylor’s Version)', 'I Almost Do (Taylor’s Version)',
                 'I Bet You Think About Me (Taylor’s Version) [From the Vault]',
                 'I Knew You Were Trouble (Taylor’s Version)',
                 'Message In A Bottle (Taylor’s Version) [From The Vault]',
                 'Nothing New (Taylor’s Version) [From The Vault]', 'Red (Taylor’s Version)',
                 'Ronan (Taylor’s Version)', 'Run (Taylor’s Version) [From The Vault]',
                 'Sad Beautiful Tragic (Taylor’s Version)', 'Starlight (Taylor’s Version)',
                 'State of Grace (Taylor’s Version)', 'Stay Stay Stay (Taylor’s Version)',
                 'The Last Time (Taylor’s Version)', 'The Lucky One (Taylor’s Version)',
                 'The Moment I Knew (Taylor’s Version)', 'The Very First Night (Taylor’s Version) [From The Vault]',
                 'Treacherous (Taylor’s Version)', 'We Are Never Ever Getting Back Together (Taylor’s Version)',
                 'Afterglow', 'Cornelia Street', 'Cruel Summer', 'Daylight', 'Death By A Thousand Cuts', 'False God',
                 'I Forgot That You Existed', 'I Think He Knows', 'It’s Nice To Have A Friend', 'London Boy', 'Lover',
                 'ME!', 'Miss Americana & The Heartbreak Prince', 'Paper Rings', 'Soon You’ll Get Better', 'The Archer',
                 'The Man', 'You Need To Calm Down', 'All Of The Girls You Loved Before',
                 'All You Had To Do Was Stay (Taylor’s Version)', 'Bad Blood (Taylor’s Version)',
                 'Blank Space (Taylor’s Version)', 'Clean (Taylor’s Version)',
                 'How You Get The Girl (Taylor’s Version)', 'I Know Places (Taylor’s Version)',
                 'Is It Over Now? (Taylor’s Version) [From The Vault]', 'I Wish You Would (Taylor’s Version)',
                 'New Romantics (Taylor’s Version)', 'Now That We Don’t Talk (Taylor’s Version) [From The Vault]',
                 'Out Of The Woods (Taylor’s Version)', 'Say Don’t Go (Taylor’s Version) [From The Vault]',
                 'Shake It Off (Taylor’s Version)', '“Slut!” (Taylor’s Version) [From The Vault]',
                 'Style (Taylor’s Version)', 'Suburban Legends (Taylor’s Version) [From The Vault]',
                 'Sweeter Than Fiction (Taylor’s Version)', 'This Love (Taylor’s Version)',
                 'Welcome To New York (Taylor’s Version)', 'Wildest Dreams (Taylor’s Version)',
                 'Wonderland (Taylor’s Version)', 'You Are In Love (Taylor’s Version)', 'Anti-Hero', 'Bejeweled',
                 'Bigger Than The Whole Sky', 'Dear Reader', 'Glitch', 'High Infidelity', 'Karma', 'Labyrinth',
                 'Lavender Haze', 'Maroon', 'Mastermind', 'Midnight Rain', 'Paris', 'Question...?', 'Snow On The Beach',
                 'Sweet Nothing', 'The Great War', 'Vigilante Shit', 'Would’ve, Could’ve, Should’ve',
                 'You’re On Your Own, Kid', 'Back To December (Taylor’s Version)',
                 'Better Than Revenge (Taylor’s Version)', 'Castles Crumbling (Taylor’s Version) [From The Vault]',
                 'Dear John (Taylor’s Version)', 'Electric Touch (Taylor’s Version) [From The Vault]',
                 'Enchanted (Taylor’s Version)', 'Foolish One (Taylor’s Version) [From The Vault]',
                 'Haunted (Taylor’s Version)', 'I Can See You (Taylor’s Version) [From The Vault]',
                 'Innocent (Taylor’s Version)', 'Last Kiss (Taylor’s Version)', 'Long Live (Taylor’s Version)',
                 'Mean (Taylor’s Version)', 'Mine (Taylor’s Version)', 'Never Grow Up (Taylor’s Version)',
                 'Ours (Taylor’s Version)', 'Sparks Fly (Taylor’s Version)', 'Speak Now (Taylor’s Version)',
                 'Superman (Taylor’s Version)', 'The Story Of Us (Taylor’s Version)',
                 'Timeless (Taylor’s Version) [From The Vault]',
                 'When Emma Falls in Love (Taylor’s Version) [From The Vault]', 'Bad Blood (Remix) (Taylor’s Version)',
                 'Breathe (Taylor’s Version)', 'Bye Bye Baby (Taylor’s Version) [From the Vault]',
                 'Change (Taylor’s Version)', 'Come In With The Rain (Taylor’s Version)',
                 'Don’t You (Taylor’s Version) [From the Vault]', 'Fearless (Taylor’s Version)',
                 'Fifteen (Taylor’s Version)', 'Forever & Always (Taylor’s Version)', 'Hey Stephen (Taylor’s Version)',
                 'Jump Then Fall (Taylor’s Version)', 'Love Story (Taylor’s Version)',
                 'Mr. Perfectly Fine (Taylor’s Version) [From the Vault]', 'Superstar (Taylor’s Version)',
                 'Tell Me Why (Taylor’s Version)', 'That’s When (Taylor’s Version) [From the Vault]',
                 'The Best Day (Taylor’s Version)', 'The Other Side of the Door (Taylor’s Version)',
                 'The Way I Loved You (Taylor’s Version)', 'Today Was a Fairytale (Taylor’s Version)',
                 'Untouchable (Taylor’s Version)', 'We Were Happy (Taylor’s Version) [From the Vault]',
                 'White Horse (Taylor’s Version)', 'You All Over Me (Taylor’s Version) [From the Vault]',
                 'You Belong With Me (Taylor’s Version)', 'You’re Not Sorry (Taylor’s Version)',
                 'Call It What You Want', 'Dancing With Our Hands Tied', 'Delicate', 'Don’t Blame Me', 'Dress',
                 'End Game', 'Getaway Car', 'Gorgeous', 'I Did Something Bad', 'King of My Heart',
                 'Look What You Made Me Do', 'New Year’s Day', 'So It Goes...', 'This Is Why We Can’t Have Nice Things',
                 '...Ready for It?', 'Hits Different', 'If This Was a Movie (Taylor’s Version)',
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
            item = lyrics_array[i]
            supporting_songs = []
            while len(supporting_songs) < 3:
                if math.ceil((num / 40)) > len(all_songs):
                    supporting_songs = ['22 (Taylor’s Version)',
                                        'All Too Well (10 Minute Version) (Taylor’s Version) [From The Vault]',
                                        'All Too Well (Taylor’s Version)']

                if j >= len(all_songs):
                    j = math.ceil((num / 40))

                supporting_songs.append(all_songs[j])
                j += math.ceil((num / 40))

            supporting_songs.insert((j % 4), item[1])
            item.append(supporting_songs)

            quiz_list.append(item)

    return jsonify({'quote': quiz_list})

if __name__ == '__main__':
    app.run(debug=True)

