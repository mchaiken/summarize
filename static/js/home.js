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
                                          modelEvents: {
                                          "change":function(){
                                          this.render();
                                          }}
                                          });

App.LinksView = Marionette.CollectionView.extend({
                                                 childView: App.LinkView
                                                 });

var Link = Backbone.Model.extend({
                                 url:"/link",
                                 idAttribute:'_id',
                                 });
var Links = Backbone.Collection.extend({
                                       model:Link,
                                       comparator:"name",
                                       url:"/links",
                                       initialize:function(){
                                       this.fetch(function(d){
                                                  console.log(d);
                                                  this.render();
                                                  });
                                       }
                                       });

var l1 = new Link({title:"first article",date:"11/07/97",url:"meow.com"});
var l2 = new Link({title:"second article",date:"11/08/98",url:"woof.com"});

var c = new Links([l1,l2]);

App.start();
