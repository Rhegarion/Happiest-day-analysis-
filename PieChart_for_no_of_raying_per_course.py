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

nor = data.groupby(['Course Name'])['Rating'].count()



plot_def ='''
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'No.of ratings per course'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.y} ratings</b>'
    },
    accessibility: {
        point: {
            valueSuffix: 'ratings'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.y} ratings '
            }
        }
    },
    series: [{
        name: 'Courses',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
'''

def simpleapp() :
    qp = jp.QuasarPage()

    h1 = jp.QDiv( a = qp , text = "Course Analysis" , classes = "text-h2 text-weight-bolder text-center q-pa-md")

    p1 = jp.QDiv(a = qp , text = "This piechart shows : " ,classes = "text-body1 text-weight-regular text-center " )

    hc = jp.HighCharts(a= qp , options=plot_def )
    
    

    hc_data = [{"name": v1 , "y": v2 } for (v1,v2) in zip(nor.index , nor)]
    hc.options.series[0].data = hc_data

    return qp

jp.justpy(simpleapp)