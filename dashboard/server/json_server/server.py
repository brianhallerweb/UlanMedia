from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

from functions.data_acquisition_functions.create_p_widgets_for_all_campaigns_dataset import create_p_widgets_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_campaigns_for_one_p_widget_dataset import create_campaigns_for_one_p_widget_dataset
from functions.data_acquisition_functions.create_p_widgets_for_one_campaign_dataset import create_p_widgets_for_one_campaign_dataset
from functions.data_acquisition_functions.create_c_widgets_for_all_campaigns_dataset import create_c_widgets_for_all_campaigns_dataset
from functions.data_acquisition_functions.create_campaigns_for_one_c_widget_dataset import create_campaigns_for_one_c_widget_dataset

from functions.data_analysis_functions.create_campaigns_for_all_campaigns_report import create_campaigns_for_all_campaigns_report
from functions.data_analysis_functions.create_p_widgets_for_all_campaigns_report import create_p_widgets_for_all_campaigns_report
from functions.data_analysis_functions.create_campaigns_for_one_p_widget_report import create_campaigns_for_one_p_widget_report
from functions.data_analysis_functions.create_p_widgets_for_one_campaign_report import create_p_widgets_for_one_campaign_report
from functions.data_analysis_functions.create_c_widgets_for_all_campaigns_report import create_c_widgets_for_all_campaigns_report
from functions.data_analysis_functions.create_campaigns_for_one_c_widget_report import create_campaigns_for_one_c_widget_report

app = Flask(__name__)

@app.route("/jsonapi/createCampaignsForAllCampaignsReport", methods=["POST"])
def createCampaignsForAllCampaignsReport():
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c5 = request.json["c5"]
    c6 = request.json["c6"]
    c6Value = request.json["c6Value"]
    c7 = request.json["c7"]
    c7Value = request.json["c7Value"]
    c8 = request.json["c8"]
    c8Value = request.json["c8Value"]
    c9 = request.json["c9"]
    c9Value = request.json["c9Value"]
    c10 = request.json["c10"]
    c10Value = request.json["c10Value"]
    c11 = request.json["c11"]
    c11Value = request.json["c11Value"]
    c12 = request.json["c12"]
    c12Value = request.json["c12Value"]
    c13 = request.json["c13"]
    c13Value = request.json["c13Value"]
    c14 = request.json["c14"]
    c14Value = request.json["c14Value"]
    c15 = request.json["c15"]
    c15Value = request.json["c15Value"]
    c16 = request.json["c16"]
    c16Value = request.json["c16Value"]
    c17 = request.json["c17"]
    c17Value = request.json["c17Value"]
    c18 = request.json["c18"]
    c18Value = request.json["c18Value"]
    c19 = request.json["c19"]
    c19Value = request.json["c19Value"]
    c20 = request.json["c20"]
    c20Value = request.json["c20Value"]
    c21 = request.json["c21"]
    c21Value = request.json["c21Value"]
    c22 = request.json["c22"]
    c22Value = request.json["c22Value"]
    c23 = request.json["c23"]
    c23Value = request.json["c23Value"]
    c24 = request.json["c24"]
    c24Value = request.json["c24Value"]
    c25 = request.json["c25"]
    c25Value = request.json["c25Value"]
    c26 = request.json["c26"]
    c26Value = request.json["c26Value"]
    c27 = request.json["c27"]
    c27Value = request.json["c27Value"]
    return create_campaigns_for_all_campaigns_report(date_range, c1, c1Value, c2, c2Value, c3, c3Value, c4, c5, c6, c6Value, c7, c7Value, c8, c8Value, c9, c9Value, c10, c10Value, c11, c11Value, c12, c12Value, c13, c13Value, c14, c14Value, c15, c15Value, c16, c16Value, c17, c17Value, c18, c18Value, c19, c19Value, c20, c20Value, c21, c21Value, c22, c22Value, c23, c23Value, c24, c24Value, c25, c25Value, c26, c26Value, c27, c27Value)

@app.route("/jsonapi/createPWidgetsForAllCampaignsDataset", methods=["POST"])
def createPWidgetsForAllCampaignsDataset():
    date_range = request.json["dateRange"]
    return create_p_widgets_for_all_campaigns_dataset(date_range)

@app.route("/jsonapi/createPWidgetsForAllCampaignsReport", methods=["POST"])
def createPWidgetsForAllCampaignsReport():
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    c6 = request.json["c6"]
    c6Value = request.json["c6Value"]
    c7 = request.json["c7"]
    c8 = request.json["c8"]
    return create_p_widgets_for_all_campaigns_report(date_range, c1, c2, c3,
            c4, c5, c6, c7, c8, c1Value, c2Value, c3Value, c4Value, c5Value, c6Value)

@app.route("/jsonapi/createCampaignsForOnePWidgetDataset", methods=["POST"])
def createCampaignsForOnePWidgetDataset():
    date_range = request.json["dateRange"]
    p_widget_id = request.json["pWidgetID"]
    max_rec_bid = request.json["maxRecBid"]
    return create_campaigns_for_one_p_widget_dataset(p_widget_id, date_range, max_rec_bid)

@app.route("/jsonapi/createCampaignsForOnePWidgetReport", methods=["POST"])
def createCampaignsForOnePWidgetReport():
    date_range = request.json["dateRange"]
    p_widget_id = request.json["pWidgetID"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    c6 = request.json["c6"]
    c6Value = request.json["c6Value"]
    return create_campaigns_for_one_p_widget_report(date_range, p_widget_id, c1, c2, c3,
            c4, c5, c6, c1Value, c2Value, c3Value, c4Value, c5Value, c6Value)

@app.route("/jsonapi/createPWidgetsForOneCampaignDataset", methods=["POST"])
def createPWidgetsForOneCampaign():
    date_range = request.json["dateRange"]
    vol_id = request.json["volID"]
    max_rec_bid = request.json["maxRecBid"]
    return create_p_widgets_for_one_campaign_dataset(vol_id, date_range, max_rec_bid)

@app.route("/jsonapi/createPWidgetsForOneCampaignReport", methods=["POST"])
def createPWidgetsForOneCampaignReport():
    date_range = request.json["dateRange"]
    vol_id = request.json["volID"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    c6 = request.json["c6"]
    c6Value = request.json["c6Value"]
    c7 = request.json["c7"]
    c7Value = request.json["c7Value"]
    c8 = request.json["c8"]
    return create_p_widgets_for_one_campaign_report(date_range, vol_id, c1, c2, c3,
            c4, c5, c6, c7, c8, c1Value, c2Value, c3Value, c4Value, c5Value, c6Value, c7Value)

@app.route("/jsonapi/createCWidgetsForAllCampaignsDataset", methods=["POST"])
def createCWidgetsForAllCampaignsDataset():
    date_range = request.json["dateRange"]
    return create_c_widgets_for_all_campaigns_dataset(date_range)

@app.route("/jsonapi/createCWidgetsForAllCampaignsReport", methods=["POST"])
def createCWidgetsForAllCampaignsReport():
    date_range = request.json["dateRange"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    c6 = request.json["c6"]
    c6Value = request.json["c6Value"]
    c7 = request.json["c7"]
    c8 = request.json["c8"]
    return create_c_widgets_for_all_campaigns_report(date_range, c1, c2, c3,
            c4, c5, c6, c7, c8, c1Value, c2Value, c3Value, c4Value, c5Value, c6Value)

@app.route("/jsonapi/createCampaignsForOneCWidgetDataset", methods=["POST"])
def createCampaignsForOneCWidgetDataset():
    date_range = request.json["dateRange"]
    c_widget_id = request.json["widgetID"]
    max_rec_bid = request.json["maxRecBid"]
    return create_campaigns_for_one_c_widget_dataset(c_widget_id, date_range, max_rec_bid)

@app.route("/jsonapi/createCampaignsForOneCWidgetReport", methods=["POST"])
def createCampaignsForOneCWidgetReport():
    date_range = request.json["dateRange"]
    c_widget_id = request.json["widgetID"]
    c1 = request.json["c1"]
    c1Value = request.json["c1Value"]
    c2 = request.json["c2"]
    c2Value = request.json["c2Value"]
    c3 = request.json["c3"]
    c3Value = request.json["c3Value"]
    c4 = request.json["c4"]
    c4Value = request.json["c4Value"]
    c5 = request.json["c5"]
    c5Value = request.json["c5Value"]
    return create_campaigns_for_one_c_widget_report(date_range, c_widget_id, c1, c2, c3,
            c4, c5, c1Value, c2Value, c3Value, c4Value, c5Value)

if __name__ == "__main__":
    app.run(debug=True)
