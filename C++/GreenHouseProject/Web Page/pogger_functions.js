function jsonRetrieve(){
    $(document).ready(function() {
    // Variable to hold request
    var request;
   
    // Abort any pending request
    if (request) {
        request.abort();
    }

    
    request = $.ajax({
        url: "<PHP url>",
        type: "get",
        dataType: "json"
    });

    request.done(function (response, textStatus, jqXHR){
          drawChart(response);
          console.log("Hooray, it worked!");
      });

    request.fail(function (jqXHR, textStatus, errorThrown){
          console.error(textStatus, errorThrown);
      });
    });
}

function drawChart(data){
    var tempdata = data[0][0];
    var humdata = data[0][1];
    var voltdata = data[0][2];
    
    var mychart = Highcharts.stockChart(chart, {
        chart: {
            zoomType: 'x'
        },
        yAxis: {
            title: {
                    text: 'Greenhouse Statistics',
                    type: 'linear',
                    tickInterval: 1,
                    useHTML: true
                },
            opposite: false
        },
        xAxis: {
                type: 'datetime'
        },
        plotOptions: {
                series: {
                    turboThreshold: 0
                }
            },
        series: [{
            name: 'Temperature',
            data: tempdata,
            tooltip: {
                valueDecimals: 1,
                valueSuffix: "&#176C",
                useHTML: true
            }
        },
        {
            name: 'Humidity',
            data: humdata,
            tooltip: {
                valueSuffix: "%"
            }
        },
        {
            name: 'Voltage',
            data: voltdata,
            tooltip: {
                valueSuffix: "V"
            }
        }],
        rangeSelector: {
            allButtonsEnabled: true,
            enabled: true
        },
        tooltip: {
            useHTML: true
        }
        });
}

