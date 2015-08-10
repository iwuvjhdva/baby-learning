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

  interface IDot {
    x: number;
    y: number;
  }

  /** @ngInject */
  class MathExcerciseController {
    public radius: number;
    public bits: any[];
    public onOver: { (): void; };
    public currentBitIndex: number;
    public dots: IDot[];
    public label: string;
    public showEndScreen: boolean = false;

    constructor() {
      this.radius = 5;
      this.currentBitIndex = 0;
      this.drawDots();
    }

    drawDots() {
      this.dots = [];
      var currentBit = this.bits[this.currentBitIndex];

      this.label = currentBit.label;

      for (var index = 0; index < currentBit.quantity; index++) {
        do {
          var dot: IDot = {
            x: this.getRandomCoord(),
            y: this.getRandomCoord()
          };
        } while (this.overlapsOthers(dot));

        this.dots.push(dot);
      }
    }

    getRandomCoord() {
      return this.radius + Math.random() * (100 - this.radius * 2);
    }

    overlapsOthers(dot: IDot): boolean {
      var self = this;

      return this.dots.some(overlapsOther);

      ////

      function overlapsOther(otherDot: IDot) {
        var distance = Math.sqrt(
            Math.pow(otherDot.x - dot.x, 2) +
            Math.pow(otherDot.y - dot.y, 2)
          );

        return (distance <= self.radius * 2);
      }
    }

    nextBit() {
      this.currentBitIndex++;

      if (this.currentBitIndex == this.bits.length) {
        this.showEndScreen = true;
      } else if (this.currentBitIndex > this.bits.length) {
        this.showEndScreen = false;
        this.currentBitIndex = 0;
        this.onOver();
      } else {
        this.drawDots();
      }
    }
  }
}
