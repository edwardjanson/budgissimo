from flask import Blueprint, redirect, render_template, request, session
import os

import repositories.account_repository as account_repository
import repositories.platform_repository as platform_repository
import repositories.tag_repository as tag_repository
import repositories.currency_repository as currency_repository
import repositories.budget_repository as budget_repository
from models.account import Account
from models.budget import Budget

from api_connections.gs_main import run_gs_api

connections_blueprint = Blueprint("connections", __name__)

SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]


@connections_blueprint.route("/account/connections/google-sheets")
def google_sheets():
    return render_template("accounts/connections/gs_data.html", spreadsheet_id=SPREADSHEET_ID)


@connections_blueprint.route("/account/connections/google-sheets/import")
def import_data():
    google_ads = platform_repository.select(1)
    run_gs_api(google_ads, "read")
    return redirect("/account/connections/google-sheets")


@connections_blueprint.route("/account/connections/google-sheets/export")
def export_data():
    google_ads = platform_repository.select(1)
    run_gs_api(google_ads, "write")
    return redirect("/account/connections/google-sheets")


