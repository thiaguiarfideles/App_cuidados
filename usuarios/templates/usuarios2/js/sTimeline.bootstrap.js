/* 
    Project    : sTimeline
    Author     : Sascha Mander
    Website    : http://sascha-mander.de
    File       : sTimeline.bootstrap.js
*/
var DEBUG_MODE = false;

var INFO_CREATE_EVENT = "Created event with id: ";
var INFO_REMOVE_EVENT = "Removed event with id: ";
var ERROR_REMOVE_LAST_EVENT = "Error removing last element.";
var ERROR_GET_EVENT_BY_ID = "Error retrieving an event with id: ";
var ERROR_GET_EVENT_BY_TITLE = "Error retrieving an event with title: ";
var ERROR_GET_EVENT_BY_CATEGORY = "Error retrieving an event with category: ";
var ERROR_GET_EVENT_BY_ICON = "Error retrieving an event with icon: ";
var ERROR_REFRESH = "Error at rendering!";
var ERROR_SORT = "Error at sorting the events!";
var ERROR_AUTO_ALIGN = "Error at auto aligning the events!";
var FADE_SPEED = "slow";

var EVENT_ID_PREFIX = "eventId-";

var categories = ["default", "primary", "success", "warning", "danger"];
var glyphicons = [   "asterisk",
                    "plus",
                    "euro",
                    "minus",
                    "cloud",
                    "envelope",
                    "pencil",
                    "glass",
                    "music",
                    "search",
                    "heart",
                    "star",
                    "star-empty",
                    "user",
                    "film",
                    "th-large",
                    "th",
                    "th-list",
                    "ok",
                    "zoom-in",
                    "zoom-out",
                    "off",
                    "signal",
                    "time",
                    "road",
                    "download-alt",
                    "download",
                    "upload",
                    "inbox",
                    "play-circle",
                    "repeat",
                    "refresh",
                    "list-alt",
                    "lock",
                    "flag",
                    "headphones"
];


var Timeline = function(selectorId){
        var allEvents = [];
        this.selectorId = selectorId;
        this.animate = true;                
        
        /**
         * @returns {Array<Events>} AllEvents as array
         */
        this.getAllEvents = function(){
            return allEvents;
        };
        
        /**
         * 
         * @param {Array<Events>} allEvents Array with Events
         * @param {function} callbackFn Callback function
         */
        this.setAllEvents = function(allEvents, callbackFn){
            this.allEvents = allEvents;
            try{
                callbackFn();
            }catch (e){
                // no callback defined
            }
        };
        
        /**
         * @param {String} selectorId Id of div
         */
        this.setSelectorId = function(selectorId){
            this.selectorId = selectorId;
        };
        
        /**
         * Returns event with specific event id.
         * 
         * @param {int} id Id of event that shall be returned
         * @returns {Event} Returns event with specific given id.
         */
        this.getEventById = function(id){
            var result = [];
            try{
                for(var i = 0; i < allEvents.length; i++){                    
                    if(allEvents[i].getId() === id){
                        result = allEvents[i];
                    }
                }
            }catch(e){
                result = ERROR_GET_EVENT_BY_ID + id;
            }
            
            return result;
        };
        
        /**
         * Returns an array of events that have the given title.
         * 
         * @param {String} title Title of event(s) that shall be returned.
         * @returns {Array<Events>} An array of events with given title.
         */
        this.getEventByTitle = function(title){
            var result = [];
            try{
                for(var i = 0; i < allEvents.length; i++){                    
                    if(allEvents[i].getTitle().toLowerCase() === title.toLowerCase()){
                        result.push(allEvents[i]);
                    }
                }
            }catch(e){
                result = ERROR_GET_EVENT_BY_TITLE + title;
            }
            
            return result;
        };
        
        /**
         * Returns an array of events that have the given category.
         * 
         * @param {String} category Category of event(s) that shall be returned.
         * @returns {Array<Events>} An array of events with given category.
         */
        this.getEventsByCategory = function(category){
            var result = [];
            try{
                for(var i = 0; i < allEvents.length; i++){                    
                    if(allEvents[i].getCategory().toLowerCase() === category.toLowerCase()){
                        result.push(allEvents[i]);
                    }
                }
            }catch(e){
                result = ERROR_GET_EVENT_BY_CATEGORY + category;
            }
            
            return result;
        };
        
        /**
         * Returns an array of events that have the given icon.
         * 
         * @param {String} icon Icon of event(s) that shall be returned.
         * @returns {Array<Events>} An array of events with given icon.
         */
        this.getEventsByIcon = function(icon){
            var result = [];
            try{
                for(var i = 0; i < allEvents.length; i++){                    
                    if(allEvents[i].getGlyphicon().toLowerCase() === icon.toLowerCase()){
                        result.push(allEvents[i]);
                    }
                }
            }catch(e){
                if(DEBUG_MODE){
                    console.log(e);
                }
                result = ERROR_GET_EVENT_BY_ICON + icon;
            }
            
            return result;
        };
        
        /*
         * 
         * @param {Event} event Adds event to list.
         */
        this.addEvent = function(event){
            allEvents.push(event);
            this.refresh();
        };                
        
        /**
         * Creates a new event and adds it to the timeline. After that the timeline is refreshed.
         * 
         * @param {String} title Title of the new event
         * @param {String} time Time of the new event as string.
         * @param {String} content Content of the new event.
         * @param {String} glyphicon Glyphicon of the new event.
         * @param {String} category Category of the new event.
         * @param {boolean} inverted Indicates if event content shall be on the right or left.
         * @param {boolean} initToggled Indicates if event shall be toggled onPageLoad
         * @param {function} callbackFn Callback function that will be triggered after the creation of the new Event. The new event is handed to this function.
         */
        this.createNewEvent = function(title, time, content, glyphicon, category, inverted, initToggled, callbackFn){
            var eventId;
            try{
                eventId = allEvents.length;
            }catch(e){
                eventId = 0;
            }
            
            var event = new Event(eventId, title, time, content, glyphicon, category, inverted, initToggled);
            allEvents.push(event);
            if(DEBUG_MODE){
            console.log(INFO_CREATE_EVENT + event.id);
        }
            this.refresh();
            try{
                callbackFn(event);
            }catch(e){
                // no callback defined
            }            
        };
        
        /**
         * Creates a new random event and adds it to the timeline. After that the timeline is refreshed.
         * 
         * @param {function} callbackFn Callback function that will be triggered after the creation of the new Event. The new event is handed to this function.
         */
        this.createRandomEvent = function(callbackFn){
            var title = "Random Event";
            var time = Date.now() / 1000;
            var content = loremIpsum;
            var glyphicon = glyphicons[Math.floor(Math.random() * (glyphicons.length))];
            var category = categories[Math.floor(Math.random() * (categories.length))];
            var inverted = false;
            if(Math.random()<=0.5){
                inverted = true;
            }
            var initToggled = false;
            this.createNewEvent(title, time, content, glyphicon, category, inverted, initToggled, function (event){
//                sTimeline.autoAlign();
                try{
                    callbackFn(event);
                }catch (e){
                    // no callback defined
                }
                
            });
        };
        
        /**
         * Removes an event from the timeline with specific id.
         * 
         * @param {int} id Id of event that shall be removed from the timeline.
         */
        this.removeEventById = function (id){
            var event = this.getEventById(id);            
            var index = allEvents.indexOf(event);
            if(index != -1) {
                allEvents.splice(index, 1);
                if(DEBUG_MODE){
                console.log(INFO_REMOVE_EVENT + id);
            }
            }            
            this.refresh();
        };
        
        /**
         * Removes the last event of the timeline.
         */
        this.removeLastEvent = function (){
            var lastEventIndex = allEvents.length - 1;
            var id;
            try{
                id = allEvents[lastEventIndex].getId();
                this.removeEventById(id);            
            }catch(e){
                if(DEBUG_MODE){
                console.log(ERROR_REMOVE_LAST_EVENT);
            }
            }            
        };
        
        /**
         * Changes the order from all timeline events from ascending to descending and backwards.
         * 
         * @param {function} callbackFn Callback function that is called when the timeline events are reversed.
         */
        this.reverse = function (callbackFn){
            allEvents.reverse();
            this.refresh();
            try {
                callbackFn();
            } catch (e) {
                // no callback defined
            }
        };
        
        /**
         * Sorts all timeline events by ids and refreshes the timeline.
         * 
         * @param {function} callbackFn Callback function that is called when the timeline events are sorted.
         */
        this.sortById = function (callbackFn){
            try {
                allEvents.sort(function(event1, event2){
                    return event1.getId() - event2.getId();
                });
            } catch (e) {
                if(DEBUG_MODE){
                console.log(ERROR_SORT);
            }
            }
            this.refresh();
            try {
                callbackFn();
            } catch (e) {
                // no callback defined
            }
        };
        
        /**
         * Sorts all timeline events by time and refreshes the timeline.
         * 
         * @param {function} callbackFn Callback function that is called when the timeline events are sorted.
         */
        this.sortByTime = function (callbackFn) {
            try {
                allEvents.sort(function(event1, event2){
                    return event1.getTime() - event2.getTime();
                });
            } catch (e) {
                if(DEBUG_MODE){
                console.log(ERROR_SORT);
            }
            }
            this.refresh();
            try {
                callbackFn();
            } catch (e) {
                // no callback defined
            }
        };
        
        /**
         * Sorts all timeline events by icons and refreshes the timeline.
         * 
         * @param {function} callbackFn Callback function that is called when the timeline events are sorted.
         */
        this.sortByIcon = function (callbackFn) {
            try {
                allEvents.sort(function(event1, event2){
                    if(event1.getGlyphicon() < event2.getGlyphicon()) return -1;
                    if(event1.getGlyphicon() > event2.getGlyphicon()) return 1;
                    return 0;
                });
            } catch (e) {
                if(DEBUG_MODE){
                console.log(ERROR_SORT + e);
            }
            }
            this.refresh();
            try {
                callbackFn(event);
            } catch (e) {
                // no callback defined
            }
        };
        
        /**
         * Sorts all timeline events by categories and refreshes the timeline.
         * 
         * @param {function} callbackFn Callback function that is called when the timeline events are sorted.
         */
        this.sortByCategory = function (callbackFn) {
            try {
                allEvents.sort(function(event1, event2){
                    if(event1.getCategory() < event2.getCategory()) return -1;
                    if(event1.getCategory() > event2.getCategory()) return 1;
                    return 0;
                });
            } catch (e) {
                if(DEBUG_MODE){
                console.log(ERROR_SORT + e);
            }
            }
            this.refresh();
            try {
                callbackFn(event);
            } catch (e) {
                // no callback defined
            }
        };
        
        /**
         * Alignes all events left(even) or right(odd).         
         */
        this.autoAlign = function (){
            var even = true;
            try{
                for(var i = 0; i < allEvents.length; i++){
                    allEvents[i].setInverted(!even);
                    even = !even;
                }
                this.refresh();
            }catch(e){
                if(DEBUG_MODE){
                console.log(ERROR_AUTO_ALIGN);
            }
            }
        };
        
        /**
         * Redraws timeline in the current rendering div.
         */
        this.refresh = function (){
            var markup;
            try{
                markup = this.createMarkup();
            }catch(e){
                if(DEBUG_MODE){
                console.log(e);
            }
                markup = '<div class="alert alert-dismissible alert-danger">An error occured during the markup creation!</div>';
            }
            try{
                $(this.selectorId).html(markup);
                this.registerClickListener();
                $(".timeline > li.not-toggled .timeline-panel").css("display", "none");
            }catch (e){
                if(DEBUG_MODE){
                console.log(ERROR_REFRESH);
            }
            }                        
        };
        
        /**
         * Exports all events as json string
         * 
         *@returns {String} Returns a JSON-String of all elemts in the timeline.
         */
        this.exportJSON = function (){
            var result = "";
            result = JSON.stringify(allEvents);
            return result;
        };
        
        /**
         * Imports a json string and converts it to timeline events.
         * 
         * @param {String} jsonString Json String that shall be importetd
         * @param {boolean} append Decides wether the json string shall overwrite or append to the existing data.
         * @param {function} callbackFn Callback that is triggered after the import. All imported events are passed to the callback function.
         */
        this.importJSON = function(jsonString, append, callbackFn){            
            try{
                var parsed = JSON.parse(jsonString);
                if(!append) allEvents = [];
                for(var event in parsed){
                    var id, title, time, content, glyphicon, category, inverted, initToggled;
                    var newObject = parsed[event];
                    for(var key in newObject) {
                        switch (key){
                            case "id": id = newObject[key]; break;
                            case "title": title = newObject[key]; break;
                            case "time": time = newObject[key]; break;
                            case "content": content = newObject[key]; break;
                            case "glyphicon": glyphicon = newObject[key]; break;
                            case "category": category = newObject[key]; break;
                            case "inverted": inverted = newObject[key]; break;
                            case "initToggled": initToggled = newObject[key]; break;
                        }                        
                    }
                    
                    this.createNewEvent(title, time, content, glyphicon, category, inverted, initToggled);                                        
                }
            }catch (e){
                if(DEBUG_MODE){
                console.log(e);
            }
            }
            try{
                callbackFn(allEvents);
            }catch(e){
                // no callback defined
            }
        };
        
        
        /**
         * Renders the timeline to html element with given id and refreshes the timeline
         * 
         * @param {int} id Id of the new rendering div
         */
        this.renderTo = function (id){
            this.selectorId = id;
            this.refresh();
        };
        
        /**
         * Creates a new html timeline markup with all events.
         * 
         * @returns {String} Html markup for the timeline
         */
        this.createMarkup = function (){
            var markup = '';
            markup += '<ul class="timeline">';
            for(var i = 0; i < allEvents.length; i++){
                markup += allEvents[i].createMarkup();
            } 
            markup += '</ul>';
            return markup;            
        };                       
        
        /**
         * Registers all click listener for toggle functions.
         */
        this.registerClickListener = function () {
            $('.timeline .timeline-badge').click(function () {
                var eventElement = $(this).parent();
                var elementId;
                try{
                    elementId = parseInt(eventElement.attr("id").replace(EVENT_ID_PREFIX,""));
                }catch (e){
                    
                }
                sTimeline.getEventById(elementId).toggle();                
            });
        };
    
    return this;
};
    
    var Event = function(id, title, time, content, glyphicon, category, inverted, initToggled){
        this.id = id;
        this.title = title;
        this.time = time;
        this.content = content;
        this.glyphicon = glyphicon;
        this.category = category;
        this.inverted = inverted;
        this.initToggled = initToggled;
        
        /**        
         * @returns {int} Id of current event.
         */
        this.getId = function(){
            return this.id;
        };
        
        /**
         * Sets title of current event.
         * 
         * @param {String} title New title for event
         * @param {function} callbackFn Callback function that is triggered after the setting of the new title. The event will be passed to the callback funtion.
         */
        this.setTitle = function(title, callbackFn){
            this.title = title;
            try{
                callbackFn(event);
            }catch(e){
                // no callback defined
            }  
        };
        
        /**
         * @returns {String} Title of the current event.
         */
        this.getTitle = function(){
            return this.title;
        };
        
        /**
         * 
         * @param {String} time New time for current event
         * @param {function} callbackFn Callback function that is triggered after the setting of the new time. The event will be passed to the callback funtion.
         */
        this.setTime = function(time, callbackFn){
            this.time = time;
            try{
                callbackFn(event);
            }catch(e){
                // no callback defined
            }  
        };
        
        /**
         * @returns {String} Time of the current event
         */
        this.getTime = function(){
            return this.time;
        };        
        
        /**
         * 
         * @param {String} content New content for event
         * @param {function} callbackFn Callback function that is triggered after the setting of the new content. The event will be passed to the callback funtion.
         */
        this.setContent = function(content, callbackFn){
            this.content = content;
            try{
                callbackFn(event);
            }catch(e){
                // no callback defined
            }  
        };
        
        /**
         * 
         * @param {String} glyphicon New glyphicon for event(e.g.:"star")
         * @param {function} callbackFn Callback function that is triggered after the setting of the new glyphicon. The event will be passed to the callback funtion.
         */
        this.setGlyphicon = function(glyphicon, callbackFn){
            this.glyphicon = glyphicon;
            try{
                callbackFn(event);
            }catch(e){
                // no callback defined
            }  
        };
        
        /**
         * @returns {String} Returns the glyphicon of the current event.
         */
        this.getGlyphicon = function (){
            return this.glyphicon;
        };        
        
        /**
         * 
         * @param {String} category New category for event(e.g.:"primary","success","danger")
         * @param {function} callbackFn Callback function that is triggered after the setting of the new category. The event will be passed to the callback funtion.
         */
        this.setCategory = function(category, callbackFn){
            this.category = category;
            try{
                callbackFn(event);
            }catch(e){
                // no callback defined
            }  
        };
        
        /**
         * @returns {String} Returns the category of the current event.
         */
        this.getCategory = function (){
            return this.category;
        };
        
        /**
         * 
         * @param {boolean} inverted Indicates if event content shall be on the right or left.
         * @param {function} callbackFn Callback function that is triggered after the setting of the inveted parameter. The event will be passed to the callback funtion.
         */
        this.setInverted = function(inverted, callbackFn){
            this.inverted = inverted;
            try{
                callbackFn(event);
            }catch(e){
                // no callback defined
            }  
        };        
        
        /**
         * 
         * @returns {boolean} Returns init toggle.
         */
        this.getInitToggled = function(){
            return this.initToggled;
        };       
        
        /**
         * @returns {String} Creates new HTML markup for the current event
         */
        this.createMarkup = function () {
            var markup = '';      
            markup += '<li id="'+ EVENT_ID_PREFIX + this.id + '" class="event ';
            if(this.inverted) markup += 'timeline-inverted ';                       
            if(this.initToggled){ markup += 'toggled'; }else{ markup += 'not-toggled'; }
            markup += '">';// Open LI
            markup += '<div class="timeline-badge ' + this.category + '"><span class="glyphicon glyphicon-'+ this.glyphicon +'"></span></div>'; 
            markup += '<div class="timeline-panel">'; // Open Panel
            markup += '<div class="timeline-heading">'; //Open Timeline header
            markup += '<h4 class="timeline-title">' + this.title + '</h4>';                       
            markup += '<span><span class="glyphicon glyphicon-time"></span> ';
            if(this.time !== undefined && typeof this.time === 'string')  markup += this.time;
            markup += '</span>';
            markup += '</div>'; //Close Timeline header
            if(this.content != ""){
                markup += '<hr>';
                markup += '<div class="timeline-body">'; // Open content body
                markup += '<p>';
                markup += this.content;
                markup += '</p>';
                markup += '</div>'; // close content body
            }
            markup += '</div>'; // Close Panel
            markup += '</li>'; // Close LI
            
            return markup;
        };
        
        /**
         * Toggles content panel of the current event.
         */
        this.toggle = function(){
            var eventElement = $("#" + EVENT_ID_PREFIX + this.id);
            eventElement.toggleClass("toggled");
            eventElement.toggleClass("not-toggled");            
            eventElement.children('.timeline-panel').stop().slideToggle(FADE_SPEED); 
            this.initToggled = !this.initToggled;
        };
        
        /**
         * @returns {String} Current event as string
         */
        this.toString = function(){
            return "Event: " + this.title + " / " + this.time + " / " + this.content + " / " + this.glyphicon;
        };   
       
        return this;
    };

var sTimeline = new Timeline("#timeline-wrapper");    
var loremIpsum = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.";