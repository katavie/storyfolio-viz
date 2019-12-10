import requests
from token import slack_token
from datetime import date, timedelta

start_date = date(2018, 11, 1)
end_date = date(2019, 12, 1)
delta = timedelta(days=30)

current_date = start_date
current_date_string = start_date.strftime('%Y-%m-%d')

output_file = open('total_messages_over_months.txt', 'a')

while current_date < end_date:
    search_query = 'from:UBVSEF7F1 before:{}'.format(current_date_string)

    response = requests.get(
        'https://slack.com/api/search.messages',
        params={
            'token': slack_token,
            'query': search_query,
        }
    )
    

    print(current_date_string, 'done')
    print(response.json()['messages']['total'])

    output_file.write(current_date_string + '\t' + str(response.json()['messages']['total']) + '\n')

    current_date += delta
    current_date_string = current_date.strftime('%Y-%m-%d')

output_file.close()