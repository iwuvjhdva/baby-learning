/// <reference path="../../typings/angular2/angular2.d.ts" />

import {Component, View, bootstrap} from 'angular2/angular2';

@Component({
    selector: 'bit-of-intelligence'
})
@View({
    templateUrl: 'bit-of-intelligence.html'
})
export class BitOfIntelligence {
  name: string;

  constructor() {
    this.name = 'Alice';
  }
}

bootstrap(BitOfIntelligence);
