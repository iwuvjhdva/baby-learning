/// <reference path="../typings/angular2/angular2.d.ts" />

import {Component, View, bootstrap} from 'angular2/angular2';
import {BitOfIntelligence} from 'bit-of-intelligence/bit-of-intelligence';

// Annotation section
@Component({
  selector: 'baby-learning'
})
@View({
  template: '<bit-of-intelligence></bit-of-intelligence>',
  directives: [BitOfIntelligence]
})

class BabyLearningComponent {
}

bootstrap(BabyLearningComponent);
