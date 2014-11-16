
var daphneServices = angular.module('daphneServices', ['ngResource']);

daphneServices.factory('People', ['$resource',
  function($resource){
    return $resource('people.json', {}, {
      query: {method:'GET', isArray:true}
    });
  }]);


var daphne = angular.module('daphne', ['daphneServices']);

console.log("loaded")

daphne.controller('DaphneController', ['$scope', 'People', function($scope, People) {
  $scope.people = People.query();
}]);
