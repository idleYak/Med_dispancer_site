const {src, dest} = require ('gulp');
const sass = require ('gulp-sass');
const csso = require ('gulp-csso');
const include = require ('gulp-file-include');
const htmlin = require ('gulp-htmlin');
const del = require ('del');
const sync = require ('browser-sync').create();
const header = require('gulp-header');
const footer = require('gulp-footer');

function html(){
    src('blocks/**.html')
      .pipe(include({
        prefix: '@@'
      }))
}