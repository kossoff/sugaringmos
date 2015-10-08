$(function () {
    var previousPoint;
 
    var d1 = [];
    for (var i = 0; i <= 10; i += 1)
        d1.push([i, parseInt(Math.random() * 30)]);

 
    var ds = new Array();
 
     ds.push({
        data:d1,
        bars: {
            show: true, 
            barWidth: 0.3
        }
    });
                
    //tooltip function
    function showTooltip(x, y, contents, areAbsoluteXY) {
        var rootElt = 'body';
    
        $('<div id="tooltip" class="chart-tooltip">' + contents + '</div>').css( {
            top: y - 50,
            left: x - 6,
            opacity: 0.9
        }).prependTo(rootElt).show();
    };
                
    //Display graph
    $.plot($("#vertical_bars"), ds, {
        colors: ["#ee7951", "#6db6ee", "#95c832", "#993eb7", "#3ba3aa"],
        xaxis: {
				ticks: [
					[ 0, "2000" ], [ 1, "2001" ], [ 2, "2002" ], [ 3, "2003" ],
					[ 4, "2004" ], [ 5, "2005" ], [ 6, "2006" ], [ 7, "2007" ],
                    [ 8, "2008" ], [ 9, "2009" ], [ 10, "2010" ], [ 11, "2011" ]
				]
			},
        yaxis: {
				ticks: [
					[ 0, "5000" ], [ 5, "10000" ], [ 10, "20000" ], [ 15, "30000" ],
					[ 20, "40000" ], [ 25, "50000" ], [ 30, "60000" ], [ 35, "70000" ]
				]
			},
        grid:{
            hoverable:true
        }
    });

 
//add tooltip event
$("#vertical_bars").bind("plothover", function (event, pos, item) {
    if (item) {
        if (previousPoint != item.datapoint) {
            previousPoint = item.datapoint;
 
            //delete de prГ©cГ©dente tooltip
            $('.chart-tooltip').remove();
 
            var x = item.datapoint[0];
 
            //All the bars concerning a same x value must display a tooltip with this value and not the shifted value
            if(item.series.bars.order){
                for(var i=0; i < item.series.data.length; i++){
                    if(item.series.data[i][3] == item.datapoint[0])
                        x = item.series.data[i][0];
                }
            }
 
            var y = item.datapoint[1];
 
            showTooltip(item.pageX+5, item.pageY+5, parseInt(item.pageY * 100));
 
        }
    }
    else {
        $('.chart-tooltip').remove();
        previousPoint = null;
    }
 
});
 
    
});