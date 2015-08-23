module babyLearning {
  'use strict';

  export class MainController {
    public type: string;
    public bits: Object[];

    private $http: ng.IHttpService;

    /* @ngInject */
    constructor ($http: ng.IHttpService) {
      this.$http = $http;
      this.loadNext();
    }

    loadNext() {
      var self = this;

      this.$http.get('http://127.0.0.1:8080/exercises/next')
        .success(function (response: any) {
          self.type = response.type;
          self.bits = response.bits;
        });
    }
  }
}
