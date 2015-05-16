console.log("HELLO");

var App = new Marionette.Application();

App.addRegions({
    firstRegion: "#first-region",
    secondRegion: "#second-region"
});

App.on("start", function(){
    console.log("STARTING");

    var linkView = new App.LinkView({model:l1});
    console.log(linkView);
    App.secondRegion.show(linkView);

    var linksView = new App.LinksView({collection:c});
    App.firstRegion.show(linksView);

    Backbone.history.start();
});

App.LinkView = Marionette.ItemView.extend({
    template: "#link-template",
    tagName : "li",
    modelEvents: {
	"change":function(){
	    this.render();
	}}
});

App.LinksView = Marionette.CollectionView.extend({
    childView: App.LinkView
});

var Link = Backbone.Model.extend();
var Links = Backbone.Collection.extend({
    model:Link,
    comparator:"name"
});

var l1 = new Link({name:"thing"});
var l2 = new Link({name:"thing2"});

var c = new Links([l1,l2]);


App.start();
