
var App = new Marionette.Application();

App.addRegions({
    firstRegion: "#first-region",
    secondRegion: "#second-region"
});

App.on("start", function(){
    var staticView = new App.StaticView();
    App.firstRegion.show(staticView);
}
