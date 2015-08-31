module babyLearning {
  'use strict';

  export class MainController {
    public type: string;
    public bits: Object[];

    private $http: ng.IHttpService;
    private $scope: ng.IScope;

    /* @ngInject */
    constructor ($scope: ng.IScope, $http: ng.IHttpService) {
      this.$scope = $scope;
      this.$http = $http;
      this.nextExercise();
    }

    nextBit() {
      this.$scope.$broadcast('nextBit', {});
    }

    nextExercise() {
      this.$http.get('http://127.0.0.1:8080/exercises/next')
        .success((response: any) => {
          this.type = response.type;
          this.bits = response.bits;
        });
    }
  }
}
