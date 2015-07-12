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
    public circles: Object[];

    constructor() {
      this.circles = [];
      for (var index = 0; index < this.config.quantity; index++) {
        var circle = {
          x: Math.random() * 100,
          y: Math.random() * 100,
        };
        console.log(circle);

        this.circles.push(circle);
      }
    }
  }
}
