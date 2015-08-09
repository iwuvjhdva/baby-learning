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

      this.$http.get('http://192.168.0.107:8080/exercises/next')
        .success(function (response: any) {
          self.bits = response.bits;
        });
    }
  }
}
