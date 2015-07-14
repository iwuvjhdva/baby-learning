module babyLearning {
  'use strict';

  export class MainController {
    public excercise: Object[];

    /* @ngInject */
    constructor () {
      this.excercise = [
        {
          course: 'math',
          kind: 'quantity',
          quantity: 2
        },
        {
          course: 'math',
          kind: 'quantity',
          quantity: 10
        }
      ];

      this.activate();
    }

    activate() {
      var self = this;
    }
  }
}
