# AUTHOR : RITIK RANJAN

''' VISUALISATION  OF THE  HAPPIEST DAY .'''


from typing import List
import justpy as jp
from justpy.chartcomponents import HighCharts
import os
import pandas
import matplotlib.pyplot as plt
from datetime import datetime  # for using dates and time
from pytz import utc  # as time zone or system used in 'Timestamps' is utc.so for setting timesystem, it is imported.

data = pandas.read_csv("reviews.csv" , parse_dates = ['Timestamp'])

data["Weekday"] = data['Timestamp'].dt.strftime("%A")
data["daynum"] = data["Timestamp"].dt.strftime('%w') # we added this as sorting would have been alphabetical due to str

weekday_avg1 = data.groupby(['Weekday','daynum']).mean()
weekday_avg1 = weekday_avg1.sort_values('daynum')# sorts the data on daynumber basis


plot_def ='''{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: ' Happiest Day in week (2018-2021)'
    },
    subtitle: {
        text: 'Udemy >- Ardit Sulce'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'WEEKDAY'
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
            text: ' Avg. Ratings'
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

    p1 = jp.QDiv(a = qp , text = "Happiest Day here is calculated on the basis of highest rating done on the day of the week." ,classes = "text-body1 text-weight-regular text-center " )

    p2 = jp.QDiv(a = qp , text = "The plot below depicts that people are happiest on FRIDAY as highest avg, ratings are on fridays." ,classes = "text-body1 text-weight-regular text-center " )

    hc = jp.HighCharts(a= qp , options= plot_def )
    
    hc.options.xAxis.categories = list(weekday_avg1.index.get_level_values(0))
    hc.options.series[0].data = list(weekday_avg1['Rating'])

    return qp

jp.justpy(simpleapp)