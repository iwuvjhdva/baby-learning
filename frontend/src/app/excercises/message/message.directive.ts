module babyLearning {
  'use strict';

  /** @ngInject */
  export function messageExcercise(): ng.IDirective {

    return {
      restrict: 'E',
      scope: {
        bits: '=',
        onOver: '&'
      },
      templateUrl: 'app/excercises/message/message.html',
      controller: MessageExcerciseController,
      controllerAs: 'vm',
      bindToController: true
    };

  }

  /** @ngInject */
  class MathExcerciseController {
    public bits: any[];
    public message: string;

    constructor() {
      this.message = bits[0].message;
      this.comment = bits[0].comment;
    }
  }
}
