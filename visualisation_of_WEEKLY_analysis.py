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
data["Week"] = data["Timestamp"].dt.strftime("%Y-%U")
week_avg = data.groupby(["Week"]).mean() 

Chart_def='''{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Weekly Average Rating Analysis (2018-2021)'
    },
    subtitle: {
        text: 'Udemy >- Ardit Sulce'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Year - Week'
        },
        labels: {
            format: '{value} '
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km .'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Ratings'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Ratings',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}

'''

def simpleapp() :
    qp = jp.QuasarPage()

    h1 = jp.QDiv( a = qp , text = "Course Analysis" , classes = "text-h2 text-weight-bolder text-center q-pa-md")

    p1 = jp.QDiv(a = qp , text = "This is the analysis of 10 courses based on the data collected through reviews of the students who have taken this course." ,classes = "text-body1 text-weight-regular text-center " )

    hc = jp.HighCharts(a= qp , options=Chart_def )
    
    
    hc.options.xAxis.categories = list(week_avg.index)
    hc.options.series[0].data = list(week_avg['Rating'])

    return qp

jp.justpy(simpleapp)