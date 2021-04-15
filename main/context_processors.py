from main.models import Report
from django.contrib.auth.models import User
from collections import OrderedDict
from operator import getitem

def global_user_stats(request):
    allowed_urls = ['/', '/overview/', '/profile/']
    if request.user.is_authenticated and request.get_full_path() in allowed_urls:

        leader_board_obj = []
        users = User.objects.all()

        # only select reports that have points assigned to them
        reports = Report.objects.filter()

        # could potentially add a leader board model to mitigate this. this is o(n^2) might want to consider changing
        # this with scalability test

        for user in users:
            points = submitted_reports = verified_reports = system_points = 0

            # iterate over the reports and increment accordingly
            for report in reports:
                system_points += report.points
                if report.author == user.profile:
                    submitted_reports += 1
                    points += report.points
                    print(points)
                    if report.status == 'accepted':
                        verified_reports += 1

            # construct the user object and append to the context
            user_obj = {
                'author': {
                    'name': str(user.profile.username),
                    'submitted_reports': submitted_reports,
                    'verified_reports': verified_reports,
                    'points': points,
                    'profile_id': user.profile.id
                }
            }
            if user_obj['author']['points'] != 0:
                leader_board_obj.append(user_obj)
            if request.user == user:
                user_stat = user_obj

        rank = 0
        # sort the leaderboard and compute the users rank
        res = sorted(leader_board_obj, key = lambda i: (i['author']['points']), reverse=True)
        for value in res:
            rank += 1
            if value['author']['name'] == request.user.profile.username:
                break
        return {
            'reports': Report.objects.order_by('-date_submitted'),
            'leaderboard': leader_board_obj,
            'system_points': system_points,
            'user_stats': user_stat,
            'user_rank': rank
        }

    else:
        return {'null': 'null context'}
