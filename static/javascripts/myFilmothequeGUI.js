var app = angular.module("myFilmothequeGUI", []);

app.controller("myFilmothequeController", function($scope, $http) {
//	var objectListFilms = [{"path":"/media/BIGDATA/Video/Films","title":"101dalmatiens.mp4","size":308934568,"adddate":"2015-07-12T06:59:05.700Z"},{"path":"/media/BIGDATA/Video/Films","title":"2_AUTOMNES_3_HIVERS.mp4","size":965959059,"adddate":"2015-09-08T19:46:13.774Z"}];
//	$scope.objectListFilms = objectListFilms;

//	$http.get("http://192.168.1.10:8080/listfilms")
	$http.get("http://127.0.0.1:5000/listfilms")
	.success(function(data, status, headers, config) {
    	$scope.objectListFilms = data;
//	console.log(data);
	}).error(function(data, status, headers, config) {
    	$scope.status = status;
//	console.log(status);
	});


        $scope.getNFO = function(filename) { 
//           $scope.filmnfo = film + " NFO text";
//             $http.get("http://192.168.1.10:8080/filmnfo/"+filename)
             $http.get("http://127.0.0.1:5000/filmnfo/"+filename)
             .success(function(data, status, headers, config) {
             $scope.filmnfo = data;
//	     console.log(data);
             }).error(function(data, status, headers, config) {
             $scope.status = status;
//	     console.log(status);
	     });
        }
});


// Will no longer be useful because I will move it to the server side
// I had to do it after Search was enable 
app.filter("filmFilter", function() {
	return function(input) 	{
	  return input.split('_').join(' ').toUpperCase();
	};
});
