#!/usr/bin/env bash

TWITPOLL=`dirname $0`/..

python $TWITPOLL/bin/get_parties.py > $TWITPOLL/www/data/parties.json
python $TWITPOLL/bin/get_leaders.py > $TWITPOLL/www/data/leaders.json
python $TWITPOLL/bin/get_youth.py > $TWITPOLL/www/data/youth.json

python $TWITPOLL/bin/get_parties_cymru.py > $TWITPOLL/www/data/parties_cymru.json
python $TWITPOLL/bin/get_parties_scot.py > $TWITPOLL/www/data/parties_scot.json
python $TWITPOLL/bin/get_parties_ni.py > $TWITPOLL/www/data/parties_ni.json

python $TWITPOLL/bin/get_blue_red.py > $TWITPOLL/www/data/blue_red.json
python $TWITPOLL/bin/get_yellow_green.py > $TWITPOLL/www/data/yellow_green.json

python $TWITPOLL/bin/get_purple_parody.py > $TWITPOLL/www/data/purple_parody.json

