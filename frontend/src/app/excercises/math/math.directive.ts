module babyLearning {
  'use strict';

  /** @ngInject */
  export function mathExcercise(): ng.IDirective {

    return {
      restrict: 'E',
      scope: {
        bits: '=',
        onOver: '&'
      },
      templateUrl: 'app/excercises/math/math.html',
      controller: MathExcerciseController,
      controllerAs: 'vm',
      bindToController: true
    };

  }

  /** @ngInject */
  class MathExcerciseController {
    public bits: any[];
    public onOver: {(): void;};
    public currentBitIndex: number;
    public dots: Object[];

    constructor() {
      this.currentBitIndex = 0;
      this.drawDots();
    }

    drawDots() {
      this.dots = [];
      var currentBit = this.bits[this.currentBitIndex];

      for (var index = 0; index < currentBit.quantity; index++) {
        var dot = {
          x: Math.random() * 100,
          y: Math.random() * 100
        };

        this.dots.push(dot);
      }
    }

    nextBit() {
      this.currentBitIndex += 1;

      if (this.currentBitIndex >= this.bits.length) {
        this.currentBitIndex = 0;
        this.onOver();
      } else {
        this.drawDots();
      }
    }
  }
}
