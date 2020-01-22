// from data.js
var tableData = data;

// YOUR CODE HERE!
var tbody = d3.select("tbody");
console.log(tableData);
data.forEach((tableData) => {
    var row = tbody.append("tr");
    Object.entries(tableData).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });

  var date_time = d3.select("#datetime");
  function selectequal(date){
      return date.date
  };
var button = d3.select("#filter-btn");
button.on("click", function(){
  var table = d3.select("tbody");
  var inputElement = d3.select("#datetime");
  var inputValue = inputElement.property("value");
  console.log(inputValue);
  var filterData = tableData.filter(date_time => date_time.datetime == inputValue ||
    date_time.city == inputValue || 
    date_time.state == inputValue ||
    date_time.country == inputValue ||
    date_time.shape == inputValue);
  console.log(filterData);
  table.html("");
  var li = table.append(filterData);
  return (li)
});




//var table = d3.select(tbody);
//table.on("change", filterData)
  
