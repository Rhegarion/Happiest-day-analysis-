# AUTHOR : RITIK RANJAN

''' VISUALISATION OF DATA ANALYSIS .'''


from typing import List
import justpy as jp
from justpy.chartcomponents import HighCharts
import os
import pandas
import matplotlib.pyplot as plt
from datetime import datetime  # for using dates and time
from pytz import utc  # as time zone or system used in 'Timestamps' is utc.so for setting timesystem, it is imported.

data = pandas.read_csv("reviews.csv" , parse_dates = ['Timestamp'])

data["Month"] = data["Timestamp"].dt.strftime("%m-%Y")
mon_avg_crs = data.groupby(["Month" , "Course Name"]).count().unstack()

Chart_def =  '''{
    chart: {
        type: 'spline'
    },
    title: {
        text: ' MONTHLY no.of Rating course wise'
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'bottom',
        x: 200,
        y: 150,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Rating'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' Ratings'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}'''

def simpleapp() :
    qp = jp.QuasarPage()

    h1 = jp.QDiv( a = qp , text = "Course Analysis" , classes = "text-h2 text-weight-bolder text-center q-pa-md")

    p1 = jp.QDiv(a = qp , text = "This is the analysis of 10 courses based on the data collected through reviews of the students who have taken this course." ,classes = "text-body1 text-weight-regular text-center " )

    hc = jp.HighCharts(a= qp , options=Chart_def )
    
    
    hc.options.xAxis.categories = list(mon_avg_crs.index)
    hc_data = [{"name": v1 , "data":[v2 for v2 in mon_avg_crs[v1]]} for v1 in mon_avg_crs.columns]
    hc.options.series = hc_data

    return qp

jp.justpy(simpleapp)