module babyLearning {
  'use strict';

  export class MainController {
    public bit: Object;

    /* @ngInject */
    constructor () {
      this.bit = {
        course: 'math',
        kind: 'quantity',
        quantity: 10
      };

      this.activate();
    }

    activate() {
      var self = this;
    }
  }
}
