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
    //App.secondRegion.show(linkView);

    var linksView = new App.LinksView({collection:c});
    App.firstRegion.show(linksView);

    Backbone.history.start();
});

App.LinkView = Marionette.ItemView.extend({
    template: "#link-template",
    tagName : "li",
    attributes: {
        "role": "presentation"
    },
    modelEvents: {
	"change":function(){
	    this.render();
	}}
});

App.LinksView = Marionette.CollectionView.extend({
    childView: App.LinkView,
    tagName: "ul",
    className: "nav nav-pills nav-stacked"

});

var Link = Backbone.Model.extend();
var Links = Backbone.Collection.extend({
    model:Link,
    comparator:"name"
});

var l1 = new Link({title:"first article",date:"11/07/97",url:"meow.com"});
var l2 = new Link({title:"second article",date:"11/08/98",url:"woof.com"});

var c = new Links([l1,l2]);

App.start();
