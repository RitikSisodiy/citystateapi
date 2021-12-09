$(document).ready(function () {
    url = "http://api.cyberflax.tk/"
    stateurl = `${url}api/state/`
    countryurl = `${url}api/country/`
    cityurl = `${url}api/city/`
    locationsurl = `${url}api/locations/`
    stateselect = $('#state')
    countryselect = $('#country')
    cityselect = $('#city')
    pinselect = $("#pincode")
    iframe = $("#loctioniframe")
    locationsselect = $('#locations')
    makerequest(countryurl, "?data=name,id", countryselect)
    countryselect.on('change', function () {
        makerequest(stateurl, `?country=${this.value}&data=name,id`, stateselect)
        setMaplocation(countryurl,this.value)
    })
    stateselect.on('change', function () {

        makerequest(cityurl, `?state=${this.value}&data=name,id`, cityselect)
        setMaplocation(stateurl,this.value)
    })
    cityselect.on('change', function () {
        makerequest(locationsurl, `?city=${this.value}&data=name,id`, locationsselect)
        setMaplocation(cityurl,this.value)
    })
    locationsselect.on('change', async function () {
        var pin = await makerequest(locationsurl, `?id=${this.value}&data=pincode&pagesize=1`, locationsselect,responce=true)
        pinselect.val(pin[0].pincode)
        setMaplocation(locationsurl,this.value)
    })
    pinselect.focusout( async function(){
        data = await makerequest(locationsurl,`?pincode=${this.value}&pagesize=1&data=id,city_id`,pinselect,responce=true)
        if (data.length>0){
            cityid = await data[0].city_id
            statedata = await makerequest(cityurl,`?id=${cityid}`,pinselect,responce=true)
            stateid = statedata[0].state_id
            countryid = statedata[0].country_id
            countryselect.val(countryid)
            await  makerequest(stateurl, `?country=${countryid}&data=name,id`, stateselect)
            stateselect.val(stateid)
            await makerequest(cityurl, `?state=${stateid}&data=name,id`, cityselect)
            cityselect.val(cityid)
            await makerequest(locationsurl, `?pincode=${this.value}`, locationsselect)
            locationsselect.val(data[0].id)
        }
    });

});

function getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2) {
    var R = 6371; // Radius of the earth in km
    var dLat = deg2rad(lat2-lat1);  // deg2rad below
    var dLon = deg2rad(lon2-lon1); 
    var a = 
      Math.sin(dLat/2) * Math.sin(dLat/2) +
      Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * 
      Math.sin(dLon/2) * Math.sin(dLon/2)
      ; 
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
    var d = R * c; // Distance in km
    return d;
  }
  
  function deg2rad(deg) {
    return deg * (Math.PI/180)
  }

function makerequest(url, query, appendopt, responce = false) {
    return new Promise((resolve, reject) => {
            var xhttp = new XMLHttpRequest()
            xhttp.open('GET', `${url}${query}`, true)
            xhttp.send()
            xhttp.onreadystatechange = function () {
                if (xhttp.readyState == 4 && xhttp.status == 200) {
                    data = JSON.parse(xhttp.response)
                    if (responce) {
                        resolve(data)
                    } else {
                        appendopt.html('<option value="">Select</option>')
                        for (i = 0; i < data.length; i++) {
                            appendopt.append(`<option value="${data[i].id}">${data[i].name}</option>`)
                        }
                        resolve("error1")
                    }
                }
            }
        });
    }

async function setMaplocation(url,id){
    data = await makerequest(url,`?id=${id}&data=latitude,longitude`,cityselect,responce=true)
    lat = data[0].latitude
    long = data[0].longitude
    locurl = `https://maps.google.com/maps?q=${lat},${long}&t=&z=15&ie=UTF8&iwloc=&output=embed`
    iframe.attr('src',locurl)
}