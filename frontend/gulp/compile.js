'use strict';

var gulp = require('gulp');
var typescript = require('gulp-typescript');
var sourcemaps = require('gulp-sourcemaps');
var browserSync = require('browser-sync');
// var merge = require('merge2');

var tsProject = typescript.createProject({
  typescript: require('typescript'),
  target: 'ES5',
  module: 'commonjs',
  sortOutput: true,
  declarationFiles: true
});

module.exports = function(options) {
  gulp.task('compile', function () {
    var tsResult = gulp.src(options.src + '/**/*.ts')
      .pipe(sourcemaps.init())
      .pipe(typescript(tsProject));

    var pipe = tsResult.js
      .pipe(sourcemaps.write({ sourceRoot: '/'}))
      .pipe(gulp.dest(options.tmp + '/serve'))
      .pipe(browserSync.reload({ stream: true }));

    return pipe;
  });
};
