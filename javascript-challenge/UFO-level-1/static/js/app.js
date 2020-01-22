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
  var inputElement = d3.select("#datetime");
  var inputValue = inputElement.property("value");
  console.log(inputValue);
  var filterData = tableData.filter(date_time => date_time.datetime == inputValue);
  console.log(filterData);

});
var table = d3.select(tbody);
table.on("change",filterData)
  
