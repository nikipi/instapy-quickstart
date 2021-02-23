import random
from instapy import InstaPy
from instapy import smart_run


# get a session!
session = InstaPy(username='yuluniki', password='',
                  headless_browser=True,
                  multi_logs=True)

# let's go! :>
with smart_run(session):
    # general settings
    session.set_quota_supervisor(enabled=True,
                                                              sleep_after=["server_calls_h"],
                                                              sleepyhead=True,
                                                              stochastic_flow=True,
                                                              notify_me=True,
                                                              peak_likes_hourly=106,
                                                              peak_likes_daily=585,
                                                              peak_follows_hourly=48,
                                                              peak_follows_daily=None,
                                                              peak_unfollows_hourly=35,
                                                              peak_unfollows_daily=403,
                                                              peak_server_calls_hourly=None,
                                                              peak_server_calls_daily=4700)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=3000,
                                    min_followers=30,
                                    min_following=30)
    session.set_user_interact(amount=2, randomize=True, percentage=50,
                              media='Photo')
    session.set_do_like(enabled=True, percentage=90)
    session.set_do_comment(enabled=True, percentage=60)
    session.set_comments(
        ['Nice shot! @{}', 'I love your profile! @{}', '@{} Love it!',
        '@{} :heart::heart:',
        'Love your posts @{}',
        'Looks awesome @{}','What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:'
        'Getting inspired by you @{}','Wonderful','Like it','Such a kill look','Nice wear',
        ':raised_hands: Yes!',
         'ohohoh, Nice','Love ur style'
         '@{}:revolving_hearts::revolving_hearts:', '@{}:fire::fire::fire:'],
        media='Photo')

    hashtags = [ 'stayandwander', 'beautifuldestinations',
                'moodygrams','zarafashion','springfashion2021','stylingin2021'
                 'visiting', 'ilovetravel','minimalstyle','stylinginspo','dailyfashionpo','styletrends'
                ]
    random.shuffle(hashtags)
    my_hashtags = hashtags[:5]

    # unfollow activity


    # follow activity
    ammount_number = 500
    session.like_by_tags(my_hashtags, amount=100)


    """ Joining Engagement Pods...
    """
    session.join_pods(topic='entertainment', engagement_mode='no_comments')
