from instapy import InstaPy
from instapy import smart_run

class Insta:
    def __init__(self,password ,username):
        self.password = password
        self.username = username

    def instagram_action(self):
            session = InstaPy(username=self.username,
                              password=self.password,
                              headless_browser=False)

            with smart_run(session):
                # general settings
                print("connexion reussite")
                # first params
                session.set_relationship_bounds(enabled=True,
                                                delimit_by_numbers=True,
                                                max_followers=4590,
                                                min_followers=45,
                                                min_following=77)

                # activity
                session.set_quota_supervisor(enabled=True,
                                             sleep_after=["likes", "comments_d", "follows", "unfollows",
                                                          "server_calls_h"],
                                             sleepyhead=True,
                                             stochastic_flow=True,
                                             notify_me=True,
                                             peak_likes_hourly=500,
                                             peak_likes_daily=5000,
                                             peak_comments_hourly=21,
                                             peak_comments_daily=182,
                                             peak_follows_hourly=48,
                                             peak_follows_daily=None,
                                             peak_unfollows_hourly=35,
                                             peak_unfollows_daily=402,
                                             peak_server_calls_hourly=None,
                                             peak_server_calls_daily=8000)
                session.follow_user_followers(['louis118712'], amount=150, sleep_delay=30, randomize=False, interact=False)


                #choose publication by tags
                session.like_by_tags(
                    ["programming", "developer", "javascript", "computerscience", "linux",
                     "codinglife", "softwareengineer", "programminglife"],
                    amount=100
                )

                session.set_do_follow(enabled=True, percentage=60)
                session.set_do_like(True, percentage=100)
                session.set_do_comment(enabled=True, percentage=50)
                #set comments
                session.set_comments(

                    ['Nice!', 'Sweet!', 'Beautiful :heart_eyes:', 'i love it :heart:', 'Nice shot! @{}', 'Awesome! @{}',
                     'Cool :thumbsup:', 'Just incredible :open_mouth:', 'What camera did you use @{}?',
                     'Love your posts @{}',
                     'Looks awesome @{}', 'Nice @{}', ':raised_hands: Yes!', 'I can feel your passion @{} :muscle:'],
                    media='Photo'

                )

