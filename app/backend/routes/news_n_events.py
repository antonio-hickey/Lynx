from flask import Blueprint, request

from app.backend.repositories import events as events_repo
from app.backend.repositories import newsfeed as news_repo

blueprint = Blueprint("news_n_events", __name__)

@blueprint.route('/News')
def News():
    data = news_repo.get_feed()

    return data


@blueprint.route('/EconEvents', methods=['POST'])
def EconEvents():
    regions = (request.data).decode("utf-8")
    data = events_repo.get_events(regions)

    return data
