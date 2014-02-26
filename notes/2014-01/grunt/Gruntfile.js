'use strict';

module.exports = function(grunt) {
	//grunt config
	grunt.initConfig({
		task: {
			target: {

			}
		}
		sass: {
			prod: {
				options: {
					style: 'compressed'
				},
				files: {

				}
			}
		}
	})

	grunt.registerTask('css', ['sass', 'minify', 'gzip'])
}

grunt
grunt sass
grunt sass:dev

module.exports = function()
{
	grunt.registerTask(taskName, [description, ], function() {
		var done = this.async(); //async!!

		//run tasks
		grunt.task.run('bar');

		done(false //return failure to grunt);//async!! return control after async completes

		return false; //failure to grunt
	}
};

function task(arg1, arg2){
	arguments.len == 0 //strange way to check arguments of registered task

	grunt.log.writeln(); //do this for logging to console

	grunt.fail.warn(‘error message’ [,error code]);//errors
	grunt.fail.fatal(‘error message’ [, error code])
}

aliases e.g. initConfig == grunt.config.init

https://github.com/gruntjs/grunt-contrib-watch
http://blog.parkji.co.uk/2013/08/12/jekyll-build-and-serve-using-grunt.html