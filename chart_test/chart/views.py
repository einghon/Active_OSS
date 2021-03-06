from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from .fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):
    a=20000;
    # Create an object for the column2d chart using the FusionCharts class constructor
    pie3d = FusionCharts("pie3d", "ex2" , "100%", "400", "chart-1", "json",
        # The data is passed as a string in the `dataSource` as parameter.
                        """{
                            "chart": {
                                "caption": "Recommended Portfolio Split",
                                "subCaption" : "For a net-worth of $1M",
                                "showValues":"1",
                                "showPercentInTooltip" : "0",
                                "numberPrefix" : "$",
                                "enableMultiSlicing":"1",
                                "theme": "fusion"
                            },
                            "data": [{
                                "label": "Equity",
                                "value": "300000"
                            }, {
                                "label": "Debt",
                                "value": "230000"
                            }, {
                                "label": "Bullion",
                                "value": "180000"
                            }, {
                                "label": "Real-estate",
                                "value": "270000"
                            }, {
                                "label": "Insurance",
                                "value": "a"
                            }]
                           }""") 
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'index.html', {'output' : pie3d.render()})
