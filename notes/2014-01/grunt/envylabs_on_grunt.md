###EnvyLabs on Grunt
####January 15, 2014

GULP is better

- Grunt has an ecosystem of modules
- grunt should be a devDependency ONLY

Gruntfile.js

- 'use strict' is best practice
- 3 methods
  - initConfig({});
  - loadNpmTasks(‘grunt-contrib-whatever’);
  - registerTask(‘default’, ‘whatever’);

initconfig

- task:sass
- targets: 
- options can be nested in targets

**Tasks**  
see npm to search for them

**-contrib-**  
written by grunt core team

**Creating tasks**

Can add build banner <%= grunt.template.today(“yy-mm-dd) %> to an option 
messages: 
grunt.fail.warn(‘error message’ [,error code]);
grunt.fail.fatal(‘error message’ [, error code])

grunt.file.read[JSON,YAML]
grunt.file.copy(srcpath, destpath [,options])
options = [encoding, options function(){}

file.expand(‘./**/*.js); //returns array (globbing)
grunt.template.process(‘<%= baz %>, {data: obj})

Interesting modules

- “concurrent” module
- “watch” //changes are live updated like meteor

Github repo
node-orlando org

markdowns files can be generated with markdown task

tasks should be programs that run without grunt, but then a module makes it gruntable

conditionally change targets depending on environmental variable

shrinkwrap to hardcode your dependencies