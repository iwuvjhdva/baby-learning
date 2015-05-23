'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync');
var typescript = require('gulp-tsc');

module.exports = function(options) {
  gulp.task('compile', function () {
    var pipe = gulp.src(options.src + '/**/*.ts')
      .pipe(typescript({
        target: 'ES5',
        sourceMap: true,
        declaration: true,
        keepTree: false,
        sourceRoot: '/',
        outDir: options.tmp + '/serve'
      }))
      .pipe(gulp.dest(options.tmp + '/serve'))
      .pipe(browserSync.reload({ stream: true }));

    return pipe;
  });
};
