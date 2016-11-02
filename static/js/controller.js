'use strict'
/* Controllers */
var ToDoList = angular.module('ToDoList', ['ngRoute']);

/* Config */
ToDoList.config([
  '$routeProvider', '$locationProvider', '$httpProvider',
  function($routeProvide, $locationProvider, $httpProvider){
    $httpProvider.defaults.headers.common["X-CSRFToken"] = window.csrf_token;
    $routeProvide
        .when('/',{
          templateUrl:'static/templates/index.html',
          controller:'ToDoListCtrl'
        })
        .when('/create', {
          templateUrl:'static/templates/create.html',
        })
        .when('/update/:id', {
          templateUrl:'static/templates/update.html',
        })
  }
]);


ToDoList.controller('ToDoListCtrl',[
    '$scope','$http', '$location', '$routeParams', '$filter',
    function($scope, $http, $location, $routeParams, $filter) {
        //  Get data from json file
        $http.get('/index').success(function (data, status, headers, config) {
            $scope.result = data;
        });
        $scope.createTask = function () {
            $http.post('/create/', $scope.example).success(function (data, status, headers, config) {
                if(data.succses == true){
                    $location.path('/')
                }
            });
        };
        $scope.updateTask = function () {
            $http.post('/change/'+$routeParams.id+'/', $scope.example).success(function (data, status, headers, config) {
                if(data.succses == true){
                    $location.path('/')
                }
            });
        };
        $scope.redirectUrl = function (){$location.path('/create')};
        $scope.example = {
            name: 'guest',
            checked: false,
            textarea:'description',
        };
        $scope.delete = function (prop) {
            $http.post('/delete/'+prop.id+'/').success(function (data, status, headers, config) {
                if(data.succses == true){
                    window.location.reload();
                }
            });
        };
    }
]);
