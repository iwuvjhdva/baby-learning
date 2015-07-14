module babyLearning {
  'use strict';

  /** @ngInject */
  export function mathBit(): ng.IDirective {

    return {
      restrict: 'E',
      scope: {
        config: '='
      },
      templateUrl: 'app/bits/math/math.html',
      controller: MathBitController,
      controllerAs: 'vm',
      bindToController: true
    };

  }

  /** @ngInject */
  class MathBitController {
    public config: any[];
    public currentBitIndex: number;
    public dots: Object[];

    constructor() {
      this.currentBitIndex = 0;
      this.drawDots();
    }

    drawDots() {
      this.dots = [];
      var currentBit = this.config[this.currentBitIndex];

      for (var index = 0; index < currentBit.quantity; index++) {
        var dot = {
          x: Math.random() * 100,
          y: Math.random() * 100
        };

        this.dots.push(dot);
      }
    }

    next() {
      this.currentBitIndex += 1;
      this.drawDots();
    }
  }
}
