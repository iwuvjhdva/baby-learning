module babyLearning {
  'use strict';

  export class MainController {
    public bits: Object[];

    private $http: ng.IHttpService;

    /* @ngInject */
    constructor ($http: ng.IHttpService) {
      this.$http = $http;
      this.loadNext();
    }

    loadNext() {
      var self = this;

      this.$http.get('http://localhost:8080/exercises/next')
        .success(function (response: any) {
          self.bits = response.bits;
        });
    }
  }
}
