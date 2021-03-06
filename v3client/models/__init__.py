# coding: utf-8

# flake8: noqa
"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    OpenAPI spec version: 3.04.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from v3client.models.api_status import APIStatus
from v3client.models.api_status_app_version import APIStatusAppVersion
from v3client.models.award import Award
from v3client.models.award_recipient import AwardRecipient
from v3client.models.district_list import DistrictList
from v3client.models.district_ranking import DistrictRanking
from v3client.models.district_ranking_event_points import DistrictRankingEventPoints
from v3client.models.elimination_alliance import EliminationAlliance
from v3client.models.elimination_alliance_backup import EliminationAllianceBackup
from v3client.models.elimination_alliance_status import EliminationAllianceStatus
from v3client.models.event import Event
from v3client.models.event_district_points import EventDistrictPoints
from v3client.models.event_district_points_points import EventDistrictPointsPoints
from v3client.models.event_district_points_tiebreakers import EventDistrictPointsTiebreakers
from v3client.models.event_insights import EventInsights
from v3client.models.event_insights_2016 import EventInsights2016
from v3client.models.event_insights_2017 import EventInsights2017
from v3client.models.event_insights_2018 import EventInsights2018
from v3client.models.event_op_rs import EventOPRs
from v3client.models.event_predictions import EventPredictions
from v3client.models.event_ranking import EventRanking
from v3client.models.event_ranking_extra_stats_info import EventRankingExtraStatsInfo
from v3client.models.event_ranking_rankings import EventRankingRankings
from v3client.models.event_ranking_sort_order_info import EventRankingSortOrderInfo
from v3client.models.event_simple import EventSimple
from v3client.models.match import Match
from v3client.models.match_alliance import MatchAlliance
from v3client.models.match_simple import MatchSimple
from v3client.models.match_simple_alliances import MatchSimpleAlliances
from v3client.models.match_timeseries_2018 import MatchTimeseries2018
from v3client.models.match_videos import MatchVideos
from v3client.models.media import Media
from v3client.models.team import Team
from v3client.models.team_event_status import TeamEventStatus
from v3client.models.team_event_status_alliance import TeamEventStatusAlliance
from v3client.models.team_event_status_alliance_backup import TeamEventStatusAllianceBackup
from v3client.models.team_event_status_playoff import TeamEventStatusPlayoff
from v3client.models.team_event_status_rank import TeamEventStatusRank
from v3client.models.team_event_status_rank_ranking import TeamEventStatusRankRanking
from v3client.models.team_event_status_rank_sort_order_info import TeamEventStatusRankSortOrderInfo
from v3client.models.team_robot import TeamRobot
from v3client.models.team_simple import TeamSimple
from v3client.models.wlt_record import WLTRecord
from v3client.models.webcast import Webcast
