module babyLearning {
  'use strict';

  export class MainController {
    public bits: Object[];

    private $http: ng.IHttpService;

    /* @ngInject */
    constructor ($http: ng.IHttpService) {
      this.$http = $http;

      this.bits = [
        {
          course: 'math',
          kind: 'quantity',
          quantity: 100
        },
        {
          course: 'math',
          kind: 'quantity',
          quantity: 200
        }
      ];

    }

    loadNext() {
      return;
      // this.$http.get('http://localhost:5000/excercises/next')
      //   .success(function () {
      //   });
    }
  }
}
