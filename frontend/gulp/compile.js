'use strict';

var gulp = require('gulp');
var typescript = require('gulp-tsc');

module.exports = function(options) {
  gulp.task('compile', function () {
    return gulp.src('src/**/*.ts')
    .pipe(typescript({
      target: 'ES5',
      emitError: false,
      sourceMap: true,
      mapRoot: './'
    }))
    .pipe(gulp.dest(options.tmp + '/serve'));
  });
};
