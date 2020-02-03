d3Plot();
// @TODO: YOUR CODE HERE!
function d3Plot(){
    var svgWidth = window.innerWidth;
    var svgHeight = window.innerHeight;

    var chartMargin = {
    top: 50,
    right: 50,
    bottom: 50,
    left: 50
    };

    var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
    var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

    var svg = d3
    .select("body")
    .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth);


    var chartGroup = svg.append("g")
    .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);


    d3.csv("assets/data/data.csv").then(function(allData){
        console.log(allData);
        allData.forEach(function(element){
            element.poverty = +element.poverty;
            element.healthcare = +element.healthcare
        });

        var xLinearScale = d3.scaleLinear()
        .domain(d3.extent(allData, d => d.poverty-2))
        .range([0, chartWidth]);

        var yLinearScale = d3.scaleLinear()
            .domain(d3.extent(allData, d=>d.healthcare-2))
            .range([chartHeight, 0]);
        var bottomAxis = d3.axisBottom(xLinearScale);
        var leftAxis = d3.axisLeft(yLinearScale);
        chartGroup.append("g")
            .attr("transform", `translate(0, ${chartHeight})`)
            .call(bottomAxis);

        chartGroup.append("g")
            .call(leftAxis);

        svg.append("text")             
            .attr("transform",
                    "translate(" + (chartWidth/2) + " ," + 
                                (chartHeight + chartMargin.top+35) + ")")
            .style("text-anchor", "middle")
            .text("poverty");
        
        svg.append("text")
            .attr("text-anchor", "middle")  
            .attr("transform", "translate("+ ((chartMargin.left/2)-10) +","+(chartHeight/2)+")rotate(-90)")  
            .text("healthcare"); 

        var circles = chartGroup.selectAll("circle")
        .data(allData)
        .enter()
        .append("circle")
        .classed("scatter", true)
        .attr("cx", d => xLinearScale(d.poverty))
        .attr("cy", d => yLinearScale(d.healthcare))
        .attr("r", "5")
        .attr("fill", "red")
        .attr("opacity", "1");
    }).catch(function(error) {
        console.log(error);
    });
};

