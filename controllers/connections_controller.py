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


@connections_blueprint.route("/accounts/<account_id>/connections/google-sheets")
def google_sheets(account_id):
    account = account_repository.select(account_id)
    return render_template("accounts/connections/gs_data.html", spreadsheet_id=account.spreadsheet_id, account=account) # type: ignore


@connections_blueprint.route("/accounts/<account_id>/connections/google-sheets/import")
def import_data(account_id):
    account = account_repository.select(account_id)
    google_ads = platform_repository.select(1)
    run_gs_api(google_ads, "read", account)
    return redirect(f"/accounts/{account_id}/connections/google-sheets")


@connections_blueprint.route("/accounts/<account_id>/connections/google-sheets/export")
def export_data(account_id):
    account = account_repository.select(account_id)
    google_ads = platform_repository.select(1)
    run_gs_api(google_ads, "write", account)
    return redirect(f"/accounts/{account_id}/connections/google-sheets")


