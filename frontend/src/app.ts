/// <reference path="../typings/angular2/angular2.d.ts" />

import {Component, View, bootstrap} from 'angular2/angular2';

// Annotation section
@Component({
    selector: 'baby-learning'
})
@View({
    template: '<h1>Hello {{ name }}</h1>'
})

class BabyLearningComponent {
  name: string;

  constructor() {
    this.name = 'Alice';
  }
}

bootstrap(BabyLearningComponent);
