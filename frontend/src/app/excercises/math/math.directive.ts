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
    public radius: number;
    public bits: any[];
    public onOver: {(): void;};
    public currentBitIndex: number;
    public dots: {x: number; y: number}[];

    constructor() {
      this.radius = 2.75;
      this.currentBitIndex = 0;
      this.drawDots();
    }

    drawDots() {
      this.dots = [];
      var currentBit = this.bits[this.currentBitIndex];

      // var w = 0;
      for (var index = 0; index < currentBit.quantity; index++) {
        do {
          var dot = {
            x: this.getRandomCoord(),
            y: this.getRandomCoord()
          };
        } while (this.overlapsOthers(dot));

        // var dot = {
        //   x: w,
        //   y: this.radius
        // };
        //
        // w+=this.radius;
        this.dots.push(dot);
      }
    }

    getRandomCoord() {
      return this.radius + Math.random() * (100 - this.radius * 2);
    }

    overlapsOthers(dot) {
      var self = this;

      this.dots.forEach(function (otherDot) {
        var distance = Math.sqrt(
            Math.pow(otherDot.x - dot.x, 2) +
            Math.pow(otherDot.y - dot.y, 2)
          );

        if (distance <= self.radius * 140) {
          console.log('overlaps!');
          return true;
        } else {
          console.log(distance, self.radius * 140);
        }
      });

      console.log("doesn't overlap!", dot);

      return false;
    }

    nextBit() {
      this.currentBitIndex++;

      if (this.currentBitIndex >= this.bits.length) {
        this.currentBitIndex = 0;
        this.onOver();
      }
      this.drawDots();
    }
  }
}
