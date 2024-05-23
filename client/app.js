
  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var mileage = document.getElementById("uiMileage");
    var year = document.getElementById("uiYear")
    var make = document.getElementById("uiMake")
    var offer = document.getElementById("uiOffer");
    var model = document.getElementById("uiModel");
    var fuel = document.getElementById("uiFuel");
    var transmission = document.getElementById("uiTransmission");

    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:8000/predict"; //Use this if you are NOT using nginx which is first 7 tutorials
   // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    console.log(mileage.value)
    console.log(year.value)
    console.log(model.value)
    console.log(make.value)
    console.log(fuel.value)
    console.log(transmission.value)
    console.log(offer.value)
    $.ajaxSetup({
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
});
    $.post(url, JSON.stringify({
        mileage : parseInt(mileage.value),
        year : parseInt(year.value),
        model : String(model.value),
        make : make.value,
        fuel : fuel.value,
        gear : transmission.value,
        offerType : offer.value

    }),function(response, status) {
        console.log(response);
        estPrice.innerHTML = "<h2>" + response.data.price.toString() + " Euros</h2>";
        console.log(status);
    });
  }
  
  function onPageLoad() {
    console.log( "document loaded" );
     var url = "http://127.0.0.1:8000/get_all"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(response, status) {
        console.log("got response for get_all request");
        console.log(response)
        if(response) {
            var models = response.data.models;
            var makers = response.data.makers;
            var fuelTypes = response.data.fuelTypes;
            var offerTypes = response.data.offerTypes;
            var transmission = response.data.transmissions;
            var uiMake = document.getElementById("uiMake");
            var uiOffer = document.getElementById("uiOffer");
            $('#uiMake').empty();
            for(var i in makers) {
                var opt = new Option(makers[i]);
                $('#uiMake').append(opt);
            }
            $('#uiOffer').empty();
            for(var i in offerTypes) {
                var opt = new Option(offerTypes[i]);
                $('#uiOffer').append(opt);
            }
            $('#uiModel').empty();
            for(var i in models) {
                var opt = new Option(models[i]);
                $('#uiModel').append(opt);
            }
            $('#uiFuel').empty();
            for(var i in fuelTypes) {
                var opt = new Option(fuelTypes[i]);
                $('#uiFuel').append(opt);
            }
            $('#uiTransmission').empty();
            for(var i in transmission) {
                var opt = new Option(transmission[i]);
                $('#uiTransmission').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;