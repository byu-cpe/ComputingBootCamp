var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var accessToken = "B5DnzMKUnkyeZr37hYVIaRek187cGR";
var refreshToken = "alRomkBdnUI6A9oQcNjenfTECIyQOA";
var computingBootCampId = '0YOSWoQPQO-ehX8P3o7ZFw';

function issueBadge(badgeEntityID, userEmail) {
    console.log(issueAssertionToTestUser(computingBootCampId, badgeEntityID, userEmail));
}

//THis function can be used to get an authentication token to make requests with the server for the Computing Boot Camp
function getAuthenticationToken() {
    var url = "https://api.badgr.io/o/token";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, false);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(xhr.status);
            console.log(xhr.responseText);
    }};

    var data = "username=danielcbutter@gmail.com&password=BootCampBadges";

    xhr.send(data);

    return JSON.parse(xhr.responseText).access_token;
}

//This function uses a refresh Token to make a certain authToken reusable again to make requests with the server.
//If you have a refresh token but not the corresponding authToken that goes with it, you'll have to get a new
//authentication token.
function refreshStoredAuthToken() {
    var url = "https://api.badgr.io/o/token";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, false);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(xhr.status);
            console.log(xhr.responseText);
    }};

    var data = "grant_type=refresh_token&refresh_token=" + refreshToken;

    xhr.send(data);
    return JSON.parse(xhr.responseText);
}

//This function will take an authToken and get the issuerInformation tied to that account
function getIssuerInformation (authToken) {
    var url = "https://api.badgr.io/v2/issuers";

    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, false);

    xhr.setRequestHeader("Authorization", "Bearer " + authToken);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
           console.log(xhr.status);
           console.log(xhr.responseText);
        }};
     
     xhr.send();

     while(xhr.status == 403) {
        refreshStoredAuthToken();
        xhr.send();
     }

     return JSON.parse(xhr.responseText);
}

//This function will take an authToken and issuerID and return the badgeClass information for that Issuer
function getBadgeClassInformation(issuerEntityID) {
    var url = "https://api.badgr.io/v2/issuers/" + issuerEntityID + "/badgeclasses";
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, false);

    xhr.setRequestHeader("Authorization", "Bearer " + accessToken);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
           console.log(xhr.status);
           console.log(xhr.responseText);
        }};
     
     xhr.send();

     while(xhr.status == 403) {
        refreshStoredAuthToken();
        xhr.send();
     }

     return JSON.parse(xhr.responseText);
}

//This function will take an authToken, issuerId and badgeID and issue a badge to the person with the information provided.
function issueAssertionToTestUser(issuerEntityID, badgeEntityID, userEmail) { //Assertion is another name for Badge
    //Issue the Assertion that we want to
    var url = "https://api.badgr.io/v2/issuers/" + issuerEntityID + "/assertions";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, false);

    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("Authorization", "Bearer " + accessToken);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(xhr.status);
            console.log(xhr.responseText);
    }};

    var data = {"badgeclass": badgeEntityID,
        "recipient":{
        "identity": userEmail,
        "hashed":false,
        "type":"email",
        },
        "notify":true,};
    var dataString = JSON.stringify(data);

    xhr.send(dataString);

    while(xhr.status == 403) {
        refreshStoredAuthToken();
        xhr.send();
    }

    return JSON.parse(xhr.responseText);
}