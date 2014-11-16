if(typeof angular == 'undefined') {
  console.log("no angular")
} else {
  console.log("angular")
}

var daphne = angular.module('daphne',[]);

console.log("loaded")

daphne.controller('DaphneController', ['$scope', function($scope) {
  $scope.greeting = 'Hola!';
}]);