d3.json("samples.json").then(function(theData){
    console.log(theData);
    var data = theData;
    var metadata = data.metadata;
    console.log(metadata);
    var samples = data.samples;
    console.log(samples);
    var demoTable = d3.select('#sample-metadata');
    metadata.forEach((Element) => {
        var testDropdown = d3.select('#selDataset');
        samples.forEach((Element) => {
            var row = testDropdown.append("option");
            row.attr("value", Element.id);
            row.text(Element.id);
        }); 
    });

    function init() {
        var dropdownMenu = d3.select("#selDataset");
        var dataset = dropdownMenu.node().value;
        console.log(dataset);
        
        function filterTestSubject(subject) {
            return subject.id == "940";
          }
        
        var filteredSubject = metadata.filter(filterTestSubject);
        console.log(filteredSubject);  
        
        var filteredValues = samples.filter(filterTestSubject);
        console.log(filteredValues);    
    
    
        sortedData = filteredValues.sort((a, b)=>
        b.sample_values - a.sample_values);
    
    
        demoTable.selectAll('p').html("")
    
        filteredSubject.forEach(subject =>{
        var textline = demoTable.append('p');
        textline.text(`ID: ${subject.id}`);
        var textline = demoTable.append('p');
        textline.text(`Ethnicity: ${subject.ethnicity}`);
        var textline = demoTable.append('p');
        textline.text(`Gender: ${subject.gender}`);
        var textline = demoTable.append('p');
        textline.text(`Age: ${subject.age}`);
        var textline = demoTable.append('p');
        textline.text(`Location: ${subject.location}`);
        var textline = demoTable.append('p');
        textline.text(`BB Type: ${subject.bbtype}`);
        var textline = demoTable.append('p');
        textline.text(`WFreq: ${subject.wfreq}`);
    
        var otus = [];
    
        for (i=0;i<10;i++){
            otus.push(`OTU ${sortedData["0"].otu_ids[i]}`)
        };
    
        console.log(otus);
    
        var trace1 = {
            x: sortedData["0"].sample_values.slice(0,10).reverse(),
            y: otus.reverse(),
            text: sortedData["0"].otu_labels.slice(0,10),
            name: "OTUs",
            type: "bar",
            orientation: "h",
            };
    
        var chartData = [trace1];
    
        var layout = {
        title: "Top 10",
        xaxis:{title:'OTU Value'},
        height: 600,
        width: 400
        };
    
        Plotly.newPlot("bar", chartData, layout);
     
    
        var trace1 = {
            x: sortedData["0"].otu_ids,
            y: sortedData["0"].sample_values,
            mode: 'markers',
            text: sortedData["0"].otu_labels,
            marker: {
              color: sortedData["0"].otu_ids,
              opacity: sortedData["0"].otu_ids,
              size: sortedData["0"].sample_values
            }
          };
          
          var data = [trace1];
          
          var layout = {
            title: 'OTU Data',
            showlegend: false,
            height: 600,
            width: 800,
            xaxis:{title:'OTU ID'},
            yaxis:{title:'OTU Sample Value'}
          };
          
          Plotly.newPlot('bubble', data, layout);
    
        });
    
      }
  
  
      init();  
});