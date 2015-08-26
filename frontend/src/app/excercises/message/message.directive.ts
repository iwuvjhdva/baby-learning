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
  class MessageExcerciseController {
    public bits: any[];
    public onOver: { (): void; };
    public message: string;
    public comment: string;

    constructor($scope: ng.IScope) {
      this.message = this.bits[0].message;
      this.comment = this.bits[0].comment;

      $scope.$on('nextBit', () => {
        this.nextBit();
      });
    }

    nextBit() {
      this.onOver();
    }
  }
}
