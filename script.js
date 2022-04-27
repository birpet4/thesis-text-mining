document.body.addEventListener('mouseup', function () {
    if (typeof window.getSelection != 'undefined') {
        var sel = window.getSelection();
        var range = sel.getRangeAt(0);

        var startOffset = range.startOffset;
        var endOffset = startOffset + range.toString().length - 1;
        document.getElementById("start").innerHTML = startOffset;
        document.getElementById("end").innerHTML = endOffset;
        console.log("Selection starts at: " + startOffset);
        console.log("Selection ends at: " + endOffset);
    }
}, false);

const getValueInput = () =>{
  let inputValue = document.getElementById("name").value; 
  document.getElementById("valueInput").innerHTML = inputValue;
}

function loadJSON(callback) {   
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', './ner_logic.json', true);
    xobj.onreadystatechange = function () {
      if (xobj.readyState == 4 && xobj.status == "200") {
        callback(JSON.parse(xobj.responseText));
      }
    };
    xobj.send(null);  
  }

  loadJSON(function(json) {
    console.log(json); // this will log out the json object
  });

  addToJson(function() {
    start = document.getElementById("start").innerHTML;
    end = document.getElementById("end").innerHTML;
    text = document.getElementById("valueInput").innerHTML;
    let js = {}
    loadJSON(function(json) {
        js = json // this will log out the json object
    });
    js.push({
        text: text,
        conditionals: [
            {
                start: start,
                end: end
            }
        ]
    })
  })