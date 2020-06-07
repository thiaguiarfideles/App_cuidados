$(function() {
    randomEvent();    
});

function randomEvent(){
    sTimeline.createNewEvent("Testevent", new Date().toLocaleString(), loremIpsum, "star", "success", false, true); 
}

function generateExportJson(){
    var jsonString = sTimeline.exportJSON();
    $("#export-json").val(jsonString);
}   

function getValsAndCreateNewEvent(){
    var title = $("#title").val();
    var time = $("#time").val();
    var content = $("#content").val();
    var glyphicon = $("#glyphicon").val();
    var category = $("#category").val();
    var inverted = $("#inverted").prop( "checked" );
    var initToggled = $("#initToggled").prop( "checked" );
    var img =$("#img").val();

    sTimeline.createNewEvent(title, time, content, glyphicon, category, inverted, initToggled, img);
};    